import functools
'''
  Python函数也是对象，你能理解吗？
  func和普通的object在使用的时候都有（）
  函数可以作为函数的参数，这也是一般对象都具有的特性，这为函数的调用提供了方便。
'''


def try_it(*args, **kw):
    # args相当于tuple对象，kw是字典，是对另两种参数的拓展，类似于java中的可变参数
    print('args:', args)
    print('kw:', kw)


def sum_args(*args):
    print(args[1])


def sum_tuple(tpl):
    print(tpl)


def ref_sum_args(*args):
    #  这里使用*args还是args呢？事实证明args是错的，args已经打包成一个tuple对象了
    sum_args(*args)  # ref_sum_args(1,3,2)
    sum_tuple(args)  # args相当于已经打包成一个元组了


def log(func):
    # 这个函数很奇怪，我也不知道是什么意思。
    # 接受一个函数作为参数，并返回一个函数，多么奇怪的语法
    @functools.wraps(func)
    def wrapper(*args, **kw):
        # *args,**kw也是一个知识点，叫做非关键字参数和关键字参数，另两个是一般参数和默认参数
        # 分别组装成tuple，和dict
        print('call %s()' % func.__name__)  # 这个函数干的事
        # 这个
        return func(*args, **kw)    # 该部分属性函数定义部分，看懂，在最后调用了func，并返回其值。

    return wrapper


@log  # 带有装饰器的函数now('liyong')等价于log(now)(name) #
#  @log('I am a log')  # 这个（）相当于执行了一次。同时now.__name__也不是now(),是不是很奇怪？
def now(name):
    print(name)
    print('2018-12-10')


def now02(name, age):
    print(name)
    print(age)
    return name


def now01():
    # now02 = now01,有now01自然就有now01()
    # now02(),能理解这个函数的调用吧。
    print('2018-12-10,no log')
    return now02('kk')   # now01 doesn't not return anything,返回该函数执行后的返回值


def now03():
    print('2019')
    return now02   # 直接返回该函数的引用。

'''
aa = now03()
print(aa)
aa('kiki')
'''


def now04(name):  # 这些参数都是普通参数（属性）,接下来尝试传入函数参数。
    def now04_in():
        print('good')
    # now04_in()  调用内部函数
    # return now04() 这个函数会不停地调用自身，陷入死循环和
    now04_in()
    print(name)
    return now04  # 这个函数调用后就会返回自身，非常神奇.


def now06(func):
    def wrapper(*args):
        print(args)
        return func(*args)  # 执行了func函数
    '''
    aa = now06(now02)  返回wrapper函数，向其传值。
    aa('liyong') 调用wrapper函数。aa('liyong','120','df'),wrapper传参只是一个中间，具体类型还是要符合func
    '''
    return wrapper  #返回wrapper函数的引用，并没有执行wrapper函数


def logs(text):

    # 函数里的第一层函数
    def decorator(func):

        # 函数里的第二层函数
        def wrapper(*args, **kw):
            print('%s %s()' %(text, func.__name__))
            # wrapper的函数和func的函数参数一样的，怎么回事？
            # *args,**kw这样的参数可以向任何函数传递，是吗?
            return func(*args,**kw)  # 关键是看这个函数返回了什么。

        return wrapper

    return decorator


class Student(object):
    def __init__(self):
        self.score1 = 'df' # 默认赋值

    @property
    def score(self):
        return self.score1

    @score.setter  # 总之，用该函数装饰了，该函数就具有该属性
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        self.score1 = value


s = Student()
s.score = 30
print(s.score)