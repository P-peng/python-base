# 类面向对象编程

class AClass:
    name = ""
    __age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print(self.age)


b = AClass("222",123)
print(b.age,b.name,end="")

