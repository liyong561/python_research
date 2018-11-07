print(5/2)  # 和java中的不同之处
print(5//2)
for i in range(0, 10, 2):  # 0不能少
    print(i)
ls = ['one', 'two', 'three', 'four', 'five']  # ls.append(' ')
for i in range(0, len(ls), 2):
    if i+1 >= len(ls):
        break
    print(ls[i+1])
"""
不规范的list数据的提取问题
规范：ls1 = ['姓名', 'liyong', '年龄', '28', '职业', '医生']
不规范 ： ls1 = ['姓名', 'liyong', '年龄', '职业', '医生'] # 数据缺失
提取成字典数据 dics = {'姓名': 'liyong', '年龄': '28', '职业': '医生'}
怎么解决这个问题？
"""

