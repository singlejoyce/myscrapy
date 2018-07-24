# -*-coding:utf-8 -*-
# 通过调用命令行进行调试

__author__ = "joyce"
__date__ = "2018/2/26 16:39"
# 调用execute这个函数可调用scrapy脚本
from scrapy.cmdline import execute

# 设置工程命令
import sys
import os

# 设置工程路径，在cmd 命令更改路径而执行scrapy命令调试
# 获取main文件的父目录，os.path.abspath(__file__) 为__file__文件目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "douban_movie_top250"])
