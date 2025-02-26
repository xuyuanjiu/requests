import logging
import allure
import jsonpath
from tools.send_requests import jdbc_requests


def json_ex(case_data, all, res):
    if case_data["jsonEXData"]:
        with allure.step("5.json数据提取"):
            for key, value in eval(case_data["jsonEXData"]).items():
                value = jsonpath.jsonpath(res.json(), value)[0]
                all[key] = value
            logging.info(f"4.根据{case_data['jsonEXData']}进行json数据提取，存入全局变量{all}")

def sql_ex(case_data, all):
    if case_data["sqlEXData"]:
        with allure.step("6.数据库数据提取"):
            for key, value in eval(case_data["sqlEXData"]).items():
                value = jdbc_requests(case_data)
                all[key] = value
            logging.info(f"4.根据{case_data['sqlEXData']}进数据库数据提取，存入全局变量{all}")
