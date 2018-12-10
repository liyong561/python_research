class TestClass(object):
    '''
    类名也使用大写（camel），对象名使用小写
    python类对象没有一下子全部列出来，按需创建，这点和java不同。
    __dict__，类和对象分别有此方法
    __init__方法之前还有一个new方法，只是隐藏了，不需要了，同理还有__call__方法。
    '''
    name03 = "df"
    _name04 = 'df'  # 在import是有作用

    def __init__(self, name, age, income): # self不是关键字，也可以默认不传入
        self.__name01__ = 'dj'
        self.__name = name  # 这个是私有变量，是具有特殊意义的,一双下划线开头，且不以双下划线结束。
        self.age = age
        self._income = income  # 这是一个protected变量,和private及public的差别又在哪里呢？主要是类变量的区别
        name02 = 'df'

    @classmethod
    def f2(name):  # 这个也是，默认是cls,不使用也可以不传递
        # 不要理解的过生，也不要理解的太简单，要恰到好处。
        print(name)

    @staticmethod
    def f3(name):  # 静态方法不用闯入类方法。
        print(name)


print(TestClass._name04)
liyong = TestClass('liyong', '45', '100')
print(liyong.age)
print(liyong._income)
print(liyong.__name01__)  # 在用法上有些约定俗成的习惯，还是可以访问到。
