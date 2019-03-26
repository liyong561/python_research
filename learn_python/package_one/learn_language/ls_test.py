def ls_iterator():
    ls = [-23, -12]
    ls1 = [x for x in ls if x > 0]  # 只会报这个空列表，而不是报错
    print(ls1)
    print(type(ls1))
    ls2 = [x for x in ls1 if x > 0]
    print(type(ls2))
    if 19 >= 110:
        return 1


def lambda_tt():
    eq_tt()
    ls = [121, 12, 90, 43, 2, 89]
    ls3 = [121, 12, 90, 43, 2, 89]
    ls_copy = ls.copy()
    ls2 = [x for x in ls if x <= 50]
    print(ls == ls2)  # 是不相等的
    print(ls == ls_copy)
    print(ls == ls3)
    print(ls2)
    print(ls)


def eq_tt():
    ls = [1, 2, 3]
    ls2 = [1, 2, 3]
    print(ls == ls2)  # 元素相等即相等
    print(id(ls))
    print(id(ls2))


def lll():
    # 如何用lambda表达式在嵌套列表中筛选出 可
    ls = [[1, 34, 54, 65],
          [21, 32, 34, 54],
          [32, 43, 90, 32]]
    ls1 = [x for x in ls if x[0] > 3]
    ls1[0][0] = 100  # 对于数组仍然是引用。
    ls1[1] = [1, 34, 54, 65]
    ls2 = [32, 32]
    ls1.append([12, 121, 2, 1])
    # ls.append([12, 14, 34, 566])
    print(ls1)
    print(ls)


def reference_tt():
    ls1 = [[12, 2, 3],
           [212, 32, 435],
           [132, 434, 32, 4],
           [4, 55, 432]
           ]

    ls2 = []
    sub_ls = [12, 2, 3]
    ls2.append(ls1[0])
    ls2.append(ls1[2])
    print(ls1)
    ls1.remove(sub_ls)  # python对象相等的判断
    print(ls2)
    print(ls1)  # ls1并没有失去引用


eq_tt()
