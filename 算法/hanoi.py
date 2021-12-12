# 哈诺塔问题
# 1.把n-1个小盘子经过C移动到B
# 2.把最后第n个大盘子从A移动到C
# 3.把n-1个小盘子从B经过A移动到C
# b的盘子经过a移动到c
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("%s moving from %s to %s" % (n, a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, "A", "B", "C")

#索引和排序算法的，中间数的索引= (left+right) / 2
