# 函数

def testFucntion():
    print("this is function")

def test2(str):
    print("param = ", str)

def test3():
    test2("调用test2")

def test4():
    return "ok"

testFucntion()

test3()

print(test4())