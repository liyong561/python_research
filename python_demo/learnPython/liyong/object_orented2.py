class Employee:
    """
    测试类变量和对象变量，写出优雅的代码
    """
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @staticmethod
    def display_count():  # 方法采用下划线的连接方式, 不操作实例，类和实例均可调用
        print("Total employee is %d" % Employee.count)

    @classmethod
    def display_name(cls, x):
        print(cls.name)
        print(str(x))

    def display(self):
        print("Name=" + self.name, "Salary=" + str(self.salary))
        Employee.count += 1  # it has changed


emp1 = Employee("Zara", 1000)
emp1.display_count()
emp1.display()
emp2 = Employee("Manhatan", 2000)
emp2.display_count()
emp2.display()
