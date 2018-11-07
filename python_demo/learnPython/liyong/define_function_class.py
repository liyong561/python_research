"""
     import  math
"""
import math


def my_add(x, y):
    return x+y


def keyword_param(name, age, *, job, city):          # 关键字参数
    print("name="+name+",age="+str(age)+",job="+job+",city="+city)


def multi_param(name, **args):
    print(name)
    print(args)


def quadratic(a, b, c):
    """解标准一元二次方程ax^2+bx+c=0,练习python语法"""
    if a == 0:
        print("二次系数不能为零")
        return
    delta = b*b-4*a*c
    if delta < 0:
        print("方程无解")
        return "方程无解"
    x1 = (math.sqrt(delta)-b)/(2*a)
    x2 = (math.sqrt(delta)+b)/(2*a)
    return x1, x2                    # 可以返回多个值


#  print(math.cos(3))                   # 什么情况下可以不使用math前缀？规范：注释#后空一格
#  print(quadratic(1, 2, 1))
#  print(quadratic(1, 5, 9))
print(keyword_param("liyong", 25, job="engineer", city="chengdu"))     # need all keyword
dic_info = {"name": "liyong", "hobby": "reading"}
print(multi_param(dic_info))
print(id(dic_info))    # id函数

