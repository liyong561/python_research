from functools import reduce
import math


def f_squrt(x):
    return x * x


def f_add(x, y):
    return x + y


"""
 用于filter过滤序列值
"""


def f_is_odd(n):
    return n % 2 == 0


ls = [1, 2, 3, 4, 5]
""""map函数简单理解就是一一映射，reduce是将当前计算结果和序列下一个元素进行计算，故最终结果只有一个
其函数也要求有两个参数"""
ls_sq = list(map(f_squrt, ls))  # 前一个传递的是函数，函数可以作为参数传递，代码很简洁，但是容易搞混
print(ls_sq)  # 它是惰性的，要将列表显示出来
print(reduce(f_add, ls))  # 当然，这个例子可能有点不恰当，直接用sum接完成了，有些情况下它大有用处。返回一个数据
ls_sq2 = list(filter(f_is_odd, ls))  #
print(ls_sq2)
ls_abs = [12, -3, -4, -2]
ls_abs_float= [float(12), float(-3), float(-4)]
print(math.sqrt(23.1))
print(sorted(ls_abs, key=f_squrt))




