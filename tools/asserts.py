import logging
import allure
import jsonpath
from tools.send_requests import jdbc_requests


@allure.step("3.响应结果断言")
def http_assert(case_data, res, index=0):
    if case_data["check"]:
        # 响应断言日志
        result = jsonpath.jsonpath(res.json(), case_data["check"])[index]
        logging.info(f"3.响应断言：实际结果({result}) == 预期结果({case_data['expected']})")
        assert result == case_data["expected"]

    else:
        logging.info(f"3.响应断言：实际结果({res.text}) in 预期结果({case_data['expected']})")
        assert case_data["expected"] in res.text


def sql_assert(case_data, index=0):
    if case_data["sql_check"] and case_data["sql_expected"]:
        with allure.step("3.数据库断言"):
            result = jdbc_requests(case_data)
            # 数据库断言日志
            logging.info(f"3.数据库断言：实际结果({result[index]}) == 预期结果({case_data['sql_expected']})")
            assert result[index] == case_data["sql_expected"]
