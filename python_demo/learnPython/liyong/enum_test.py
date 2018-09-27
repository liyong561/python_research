from enum import Enum

Month = Enum("Month", ("Jan", "Feb", "Mar"))

class Gender(Enum):

    Male = 0
    Female = 1


print(Month.Jan)
# gender = Gender() ,枚举类不用创建
print(Gender.Female)

