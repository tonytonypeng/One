# 如果a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有a,b,c可能的组合

import time

time1 = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print('[%s,%s,%s]'%(a,b,c))
time2 = time.time()
time3 = time2 - time1
print('用时%s秒'%time3)


























