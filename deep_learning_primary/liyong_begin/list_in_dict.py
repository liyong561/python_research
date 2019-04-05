'''
在dictionary中，嵌套list是基本的操作。


'''
import string


def tt_table():
    cc_dict = dict()
    cc_dict[0] = []  # 这一步就算是初始化，确定value的类型为list，后面才能使用append方法。
    cc_dict[0].append("china")
    cc_dict[0].append('america')
    cc_dict[0].append('canada')
    print(cc_dict)


def tt_list():
    cc_dict = dict()
    if 0 in cc_dict:  # cc_dict.has_key(0)在py3中取消，直接使用in非常的好。
        print(cc_dict[0])

    cc_dict[0] = []
    cc_dict[0].append(['America', 'China', 'Canada'])  # 列表中嵌套列表
    cc_dict[0].append(['America1', 'China1', 'Canada1'])

    print(cc_dict)  # [] 对应subscriptable


def tt_comma():
    str1 = '(1008, 1, 501, 502, 503, 516, 506, 519, 508, ,522,511,512)'  # 带有连续的， 不标准的数据
    str2 = str1.strip(string.punctuation)
    ls1 = str2.split(',')
    print(str2)
    print(ls1)
    ls2 = [x for x in ls1 if x != ' ']  # 将str转换为int，使用map函数
    print(ls2)

    ls3 = list(map(int, ls2))
    print(ls3)


def list_in_list():
    ls = [
        [12, 21, 12, 100],
        [13, 32, 34, 56],
        [12, 15, 32, 67],
    ]  # 如何选出第二行，根据34最大
    ls2 = [x[2] for x in ls]
    max_v1 = max(ls2)
    ls_index = ls2.index(max_v1)
    ls3 = ls[ls_index]

    print(max_v1)
    print(ls3)


def sort_list():
    ls = [
        [12, 21, 12, 100],
        [13, 32, 34, 56],
        [11, 15, 32, 67],
    ]  # 更距第二列的值进行排序
    ls3 = ls.copy()
    ls2 = [x[2] for x in ls]
    ls.sort(key=lambda x1: x1[2])[0]  # lambda表达式非常的方便,代替小函数,同时注意sort函数没有返回值，在原数据的基础上进行修改
    print(ls)
    print(ls3)


def index_list():
    ls = [123, 13, 32, 13, 12, -1]  # 从0开始索引
    ls_copy = ls.copy()
    index1 = ls.index(123)
    index0 = -1  # /没有修改就表示没有
    if 9 in ls:
        index0 = ls.index(9)  # 没有回报错，所以首先验证一下

    print(index1)
    print(index0)
    print(ls_copy)
    index3 = 42
    if index3 < len(ls):  # 也要先判断一下索引是否超出了长度
        print(ls[index3])

def crud_list():
    ls = [
        [12, 21, 12, 100],
        [13, 32, 34, 56],
        [11, 15, 32, 67],
    ]
    sub_ls = ls[0]
    sub_ls.pop(0)  # 对其原有对象的更改
    print(ls)

sort_list()
