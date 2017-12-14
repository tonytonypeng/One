from timeit import Timer

'''
a = 1
print(a)
timer = Timer('print(a)','a = 1')
print(timer.timeit(number=6))
'''

'''
# 函数
def func():
    print(121)

timer = Timer('func()','from __main__ import func')
print(timer.timeit(number=3))
'''


# +,append,列表生成式 ,list 比较

def test1():
    list = []
    for i in range(100):
        list += [i]


def test2():
    list = []
    for i in range(100):
        list.append(i)


def test3():
    list = [x for x in range(100)]


def test4():
    li = list(range(100))


timer1 = Timer('test1()','from __main__ import test1')
print('+:',timer1.timeit(number=100000))


timer2 = Timer('test2()','from __main__ import test2')
print('append:',timer2.timeit(number=100000))


timer3 = Timer('test3()','from __main__ import test3')
print('列表生成式:',timer3.timeit(number=100000))


timer4 = Timer('test4()','from __main__ import test4')
print('list:',timer4.timeit(number=100000))
