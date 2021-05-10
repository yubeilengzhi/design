#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''

'''
import sys
from importlib import reload

from lib.core.Spider import SpiderMain
from lib.core import common
from lib.core import outputer


# reload(sys)
# sys.setdefaultencoding('utf-8')


def main():
    # root = "https://www.shiyanlou.com/"
    root = "http://www.ampak.com.tw/" #正基科技测试成功
    domain = common.w8urlparse(root)
    threadNum = 10
    output = outputer.outputer()


    # spider
    w8 = SpiderMain(root, threadNum)
    w8.craw()
    output.show()
    output.build_html(domain)



if __name__ == '__main__':
    main()