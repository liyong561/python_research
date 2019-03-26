import math
import random

def m1():
    ae = -123
    ae_abs = int(math.fabs(ae))  # 只有这样的方法。
    print(ae_abs)
    a = 9 // 4
    a1 = 9 % 4
    print(a)
    print(a1)


def rand_tt():
    counter = random.randint(1,10)
    sin90 = math.sin(90)  # sin（90）,知道python中使用的是弧度制
    sinpi = int(math.sin(math.pi/2))
    print(counter)
    print(sin90)
    print(sinpi)


rand_tt()
