import functools


class Data_a():

    def __init__(self):
        self.params = ['I', 'love', 'china']
        self.counter = 0

    def get_data(self):
        return self.params;

    def set_data(self, p):
        self.params = p


def add(a, b):
    return a + b


def append(o1):
    o1.counter = 12;


def use_add(f, a, b):
    # python中函数可以调用函数，这就可以不用定义对象，
    return f(a, b)


add_to_3 = functools.partial(add, 3)
print(add_to_3(5))  # patial对函数今进行了包装。

print(use_add(add, 10, 12))

data_a = Data_a();
append(data_a)
print(data_a.counter)
