def dict_m0():
    d = dict()
    d[1] = ' I love China'
    ls = ['ds1', 'ds2', 'ds3', 'ds4']
    # ls[2] = 'Ds',这种写法就是错的。
    ls.insert(2, 'ds')
    print(d[1])
    print(ls)


def dict_m1():
    if 4 > 3 and 5 > 4 or 4 > 9:
        print('It is true')
        ls = ['sd']
        ls.append('sddd')
        print(ls)
    if 90 > 14 or 4 > 3 and 3 > 4:
        print('It is true')
    else:
        print("It is false")


def dict_m2(ls, idx):
    length = len(ls)
    ls1 = ls.copy()
    ls[0:length - idx] = ls1[idx:length]
    # ls.append(ls1[0:idx]) # 当成一个元素防止后面
    ls[length - idx + 1:length] = ls1[0:idx]  # 含前面索引，不含后面索引

    # ls1 = ls[1:-1:1]
    print(ls)


def list_insert():
    dict1 = {'name': 'liyong', 'age': 32}
    ls = []
    ls.insert(2, "2")  # 不能顺利
    ls.insert(3, '3')
    print(ls)
    print(len(dict1))


def dict_ref(dic1):
    dic1.clear()
    dic1[1] = 12
    print(dic)


def dic_merge(dic1):
    dic2 ={'names':[['liyong','liqiang'],['dayang','xiaoyang']],'income':[[10,12],[213,12]]}
    dic2 = {'names': [['liyong', 'liqiang'], ['dayang', 'xiaoyang']], 'income': [[10, 12], [213, 12]]}



dic = {'name': 'liyong', 'age': 32}
dict_ref(dic)
print(dic)
