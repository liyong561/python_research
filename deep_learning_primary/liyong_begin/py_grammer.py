# -*- coding: utf-8 -*-

def test_generator():
	# 而不是 for j in gen01,gen01是一个函数，应该遵循函数的调用规则。
	for j in gen01():
		print(j)
		
def gen01():
	for i in range(10):
		yield i

test_generator()