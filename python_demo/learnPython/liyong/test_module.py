#!usr/bin/env/ python3
# -*- coding:utf-8 -*-
'a test module'
__author__ = "liyong"

import sys
from PIL import Image


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello,world")
    elif len(args) == 2:
        print("Hello,world:"+args[1])
    else:
        print("Hello,%s"+args[1])


test()
im = Image.open("E:/TestFile/test01.jpg", 'r')
print("图片宽{0}px,高{1}px".format(im.size[0], im.size[1]))  # 使用string的format函数
print(im.mode)
print(im.format)
print(im)
print(im.show())
