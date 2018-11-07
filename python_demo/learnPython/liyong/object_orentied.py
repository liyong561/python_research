"""最简单的类，没有java的extends和new，python的简洁风格，作用基本一样，可以有继承和封装
 动态语言的鸭子类型，只要看起来想（有那个方法就行）
"""
import types
from types import MethodType

class Student(object):
    pass


class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Student3:      # 默认继承object类
    def __init__(self, name, score):
        self.__name = name   # 私有变量
        self.__score = score

    def get_name(self):  # __xx__:特殊变量，一般不定义
        return self.__name

    def get_score(self):
        return self.__score

    def __test(self):   # 私有方法
        pass


class Student4(object):

    @property
    def score(self):
        return self._score   # 变量前面的_是什么意思？双下划线和但下划线的区别，如private 和protected

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("value must in 0 and 100")
        self._score = value   # 这个提示，不管他


class Student5:
    __slots__ = ("name", "age")  # 限制实例的属性，只能动态绑定这个两个属性


def set_name(self, name):
    self.name = name


lihua = Student()
xiaoming = Student2("xiaoming", 89)
s3 = Student3("acer", 90)  # 没有定义空的构造函数

lihua.name = "sd"    # 类中无此属性，对象动态绑定属性
lihua.set_name = MethodType(set_name, lihua)  # 动态绑定方法，class和student均可以
lihua.set_name("lihua")

print(lihua.name)
print(xiaoming.score)
""" print(s3.name) 访问不到name 属性"""
print(s3.get_name())
print(type(s3))  # 很多可以直接使用的函数,isinstance,dir
print(type(len) == types.BuiltinFunctionType)
print(isinstance(s3, Student3))
print(dir("ABC"))
"""len方法是调用了对象的__len__方法，所以说__xx__都是有特殊用途的方法,print(len(s3)),Stuent3 没有__len__方法，所以会报错
"""
print(dir(s3))   # 解析python对象
print(hasattr(s3, "name"))  # 获得一个对象的详细信息, 私有变量会报错
print(hasattr(xiaoming, "name"))
s4 = Student4()
s4.score = 23
print(s4.score)

