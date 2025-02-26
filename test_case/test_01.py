import logging
import pytest
from jinja2 import Template
from tools.allure_tools import allure_init
from tools.asserts import http_assert, sql_assert
from tools.data_EX import json_ex, sql_ex
from tools.excel_tools import read_excel
from tools.requests_data import requests_data
from tools.send_requests import http_requests


class Test:
    case_data = read_excel()
    all = {}


    @pytest.mark.parametrize("case_data", case_data)
    def test_case(self, case_data):
        all = self.all
        # 根据全局变量的值，渲染case_data
        case_data = eval(Template(str(case_data)).render(all))
        # 编辑allure报告
        allure_init(case_data)
        # 请求数据解析日志
        logging.info(f"0.请求数据解析{case_data}")

        # 1.组装请求数据
        res_data = requests_data(case_data)
        # 2.发起请求
        res = http_requests(res_data)

        # 3.响应断言
        http_assert(case_data, res)

        # 4.数据库断言
        sql_assert(case_data)
        # 5.json数据提取
        json_ex(case_data, all, res)
        # 6.数据库数据提取
        sql_ex(case_data, all)
