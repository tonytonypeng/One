# 计算下列各函数的复杂度


def fun(n):   # O(logn)
    """对数"""
    i = 1
    while i <= n:
        i *= 2
# 1*2*2*2*2*....*2=n(2的个数即步骤数等于N), 对数：2^N=n---->N = logn


def func(n):  # O(logn)
    """对数"""
    x = 2
    while x < (n/2):
        x *= 2
# # 2*2*2*2*2*....*2=n(2的个数等于N)，对数：2^(N-1) = n/2


def fund(n):   # O(n^2)
    li = []
    for i in range(n):   # n
        li.append(n)
    if 100 in li:
        print("100 in list")
    else:
        print("100 not in list")
    for i in range(n):   # n
        li.pop(0)

















