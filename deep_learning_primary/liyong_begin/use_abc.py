import abc# 这个是用在注解上的
class A:

    # @abc.abstractclassmethod,这个注解中又class
    @abc.abstractmethod
    def say(self):
        pass

    def do(self):
        print("I Just didn't do anything")

class B(A):

    def say(self):
        print("I write the A say method")

def tt():
    b =B();
    b.say()