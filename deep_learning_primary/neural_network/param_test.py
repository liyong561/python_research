# -*- coding: utf-8 -*-
class Test:
	def __init__(self,l):
		self.l = l
	def getList(self):
		print(self.l)
	def param_change(self,x):
		x = x
		x.append("op")
	def param_change01(self,x):
		x.append("opp")
	def param_change02(self,x):
		x = x.copy() # 这个就不会改变了
		x.append(x)
def getDictionry(dictionary):
	for key in dictionary.keys():
		print(dictionary[key])
		
l=["apple", "orange","banana"]
lx=["apple", "orange","banana","melon"]
dictionary = {"apple": "fruit","rice":"food"}
test = Test(l)
test.getList()  #方法或者变量。都会提示没改Attribute
#l.append("cherry")  
#test.getList()  # 很奇怪，可能指针指向这个变量
# test.param_change(lx) 传入的lx也改变了，就相当于过滤器
test.param_change02(lx)
print(lx)