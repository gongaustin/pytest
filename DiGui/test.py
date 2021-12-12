
#递归测试

def func1(x):
    print(x)
    func1(x-1)



def func2(x):
    if x > 0:
        print(x)
        func2(x+1)


def func3(x):
    if x > 0:
        print(x)
        func3(x-1)

def func4(x):
    if x > 0:
        func4(x-1)
    print(x)

func4(4)

#函数是从上往下执行，fun4打印顺序是从小到大打印