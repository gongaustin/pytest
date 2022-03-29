h = 0


def a(h):
    x = 0
    for j in range(2, h):
        if h % j == 0:
            x = 1
            break
        if x == 0:
            return 1


n = int(input("输入任意大于10的偶数："))
for i in range(n, n + 1):
    h = 0
    if i % 2 == 0:
        for k in range(2, i):
            if a(k) == 1 and a(i - k) == 1:
                h = 1
                if h == 0:
                    print("%d can not" % i)
                    break
                else:
                    print("%d=%d+%d" % (i,k,i-k))
                    break
