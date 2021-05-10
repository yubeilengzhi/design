"""
sql 检测脚本
"""

import requests
import re
import random

BOOLEAN_TESTS = (" AND %d=%d", " OR NOT (%d=%d)")
# 基于错误消息响应的DBMS识别正则表达式
DBMS_ERRORS = {
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
    "Microsoft SQL Server": (
    r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*",
    r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.",
    r"(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
    "Oracle": (
    r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
    "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*",
               r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
    "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}


def sqlCheck(url):
    """
    进行sql注入漏洞的检查
    :param url:
    :return:
    """
    # 过滤 html网页
    if (not url.find("?")):
        return False
    # 获得报错网页
    _url = url + "%29%28%22%27"  # 先用）（ “ ‘ 使报错
    _content = requests.get(_url).text
    for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
        if (re.search(regex, _content)):
            return True
    content = {}
    content["origin"] = requests.get(_url).text
    for test_payload in BOOLEAN_TESTS:
        # 正确的网页
        RANDINT = random.randint(1, 255)
        _url = url + test_payload % (RANDINT, RANDINT)
        content["true"] = requests.get(_url)
        _url = url + test_payload % (RANDINT, RANDINT + 1)
        content["false"] = requests.get(_url)
        if content["origin"] == content["true"] != content["false"]:
            return "sql found: %ds" % url
