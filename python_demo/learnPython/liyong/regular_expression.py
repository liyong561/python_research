"""
 正则表达式几乎每个语言都支持，并且用法大同小异，python偏向数据处理，正则表达式当然很重要
"""
import re

test1 = re.match(r"\d{3}\-\d{3,8}", "010-12345，010-54321")  # r不用考虑转义问题
print(test1.groups())   # group,返回匹配的字符串
str1 = "34.html"
test2 = re.match("\d.html", str1)
print(test2)  # d后的+表示可以匹配多个字符
if test2:
    print("匹配")
pattern = re.compile('\d+.')  # 正好匹配一个数字，用一个pattern可以匹配多个字符串
# 点表示匹配任意一个字符:转义：\.
test3 = pattern.match('one1two2')
print(test3)
test4 = pattern.match('one123two', 3, 10)
print(test4)
