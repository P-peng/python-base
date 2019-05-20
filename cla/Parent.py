# 继承关系

class Parent:
    property = "001"

    def __init__(self, property):
        self.property = property

    def func(self):
        print("this is parent func")

class Child(Parent):
    childProperty = "child"
    __shuxing = 666

    def __init__(self, childProperty):
        self.childProperty = childProperty

    def childFunc(self):
        print("this is child func")

    def getShuxing(self):
        return self.__shuxing

child = Child("123123")
child.childFunc()
child.func()
child.getShuxing()