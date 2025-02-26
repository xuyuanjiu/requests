import logging

import allure
from config import BASE_URL


@allure.step("1.组装请求数据")
def requests_data(case_data):
    # 1.组装数据
    method = case_data["method"]
    url = BASE_URL + case_data["path"]
    params = eval(case_data["params"]) if isinstance(case_data["params"], str) else None
    data = eval(case_data["data"]) if isinstance(case_data["data"], str) else None
    json = eval(case_data["json"]) if isinstance(case_data["json"], str) else None
    headers = eval(case_data["headers"]) if isinstance(case_data["headers"], str) else None
    files = eval(case_data["files"]) if isinstance(case_data["files"], str) else None
    # 2.请求数据
    res_data = {"method": method,
                "url": url,
                "params": params,
                "data": data,
                "json": json,
                "headers": headers,
                "files": files
                }
    # 请求数据日志
    logging.info(f"1.请求数据{res_data}")
    return res_data
