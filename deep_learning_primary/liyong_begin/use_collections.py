import collections


# pycharm会自动在*test使用nosetest。
def tt_uple():
    Point = collections.namedtuple('Point1', ['x', 'y'])  #
    p = Point('df', [12, 10])  # 名称为y的对象的是【12，10]的列表,还是要亲手实践一下一下，才知道其中的奥秘。
    p1 = (12, 30)
    print(p.x)
    print('I have a name')
    print(p)
    print(p1[1])


def tt_counter():
    # Counter类也是dictionary的子类，特殊之处它的value类型是int，并提供了统计方法
    ct = collections.Counter({'dfd': 11, 'dfs': 13})
    print(ct.elements())
    print(ct.get('dfs'))
    print(len(ct))  # 其实调用的是ct的__len__方法


def tt_dict():
    # 关于dictionary的操作，
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    dq = collections.deque(['a','b','c','d']) # deque('a','b','c','d')
    print(dq.pop()+':df')  # pop和popleft.
    print(d.get('a'))
    print(d['a'])


# tt_tuple()
# tt_counter()
tt_dict()