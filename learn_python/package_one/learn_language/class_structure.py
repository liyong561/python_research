class ClassA():
    # （）表示继承，默认是Object，
    # 这里还有一个问题就是类变量和实例变量
    _info = "this is a protected variable"
    __info1 = "this is private varible,just in the class"
    info2 = "good for it"

    # self.info2="sdf"这种做法是错误的

    def __init__(self):
        self.info2  # 声明一个实例变量

    def _get(self):
        print(ClassA._info)

    def __get1(self):
        print(ClassA.__info1)

    def get2(self):
        print(ClassA.__info1)


def f1(a1, a2, a3=21,*argsss):
    f2.a='fd'   # 给方法随便增加一个变量。
    print(f2.a)
    def f_in(f_a1,f_a2,f_a3,*argsss):  # 在方法里定义方法。
        print(a1)
        print(a2)

    def f_in2():
        print("I am from the f1's sub function")

    # return f_in2() # 一般方法作为返回值,有括号和没有括号的区别。
    return f_in2

def f2():
    print("It's ok")


a=f1(12,12)
print(type(a))
a()