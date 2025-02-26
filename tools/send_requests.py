import logging
import allure
import pymysql
import requests
from config import *


@allure.step("2.发起http请求")
def http_requests(res_data):
    res = requests.request(**res_data)
    # 响应结果数据日志
    logging.info(f"2.响应结果数据{res.text}")
    return res

def jdbc_requests(case_data):
    con = pymysql.Connect(host=DB_HOST,
                          port=DB_PORT,
                          user=DB_USER,
                          password=DB_PASSWORD,
                          database=DB_DATABASE,
                          charset="utf8"
                          )
    # 2.创建游标
    cur = con.cursor()
    cur.execute(case_data["sql_check"])
    result = cur.fetchone()
    # 3.关闭游标
    cur.close()
    # 4.关闭连接
    con.close()
    return result
