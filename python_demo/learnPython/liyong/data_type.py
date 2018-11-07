"""
dictionary=["name":"liyong","age":25] python重要中的符号（括号）很重要,并且符号后有空格。
"""


def add(x, y):         # add(int x, int y),python变量可以不声明类型，和java的差别,从java转过来有点不适应
    return x+y


list_type = ["class1", "class2", "class3"]
tuple_type = ("Apple", "Google", "Microsoft")
"""对于列表和元组来说，索引整数就是其key，只不过这个key是默认的"""
"""print(tuple_type[1]),这个不是获得元组长度的方法"""
print(len(tuple_type))
print(tuple_type.count(2))
name_array = ["liyong", "liqiang", "lihua"]
score_array = (89,92,79)  # list和tuple又可以归为sequence类型
name_score_dic = {"liyong": 89, "liqiang": 92, "lihua": 79}
name_dic = {'姓名': '', '年龄': ''}
name_dic['姓名'] = '黎勇'
print(name_score_dic["liyong"])
c = "c++"
b = "c++"
d=c+"  "
d_blank =c+""  # 没有空格
cstr = c + "c jia jia"
print(id(c), id(cstr))
print(c is b)
print(c is d)
print(c is d_blank)


def multi(a, b):
    return a*b


def abs_liyong(x):
    if not isinstance(x, (int, float)):
        raise TypeError("类型错误")  # raise，新的关键字
    if x>0:
        return x
    if x<0:
        return -x   # 很清晰


print(multi(2, 4))  # 定义函数要空两行
