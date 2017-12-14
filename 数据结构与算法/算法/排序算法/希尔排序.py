def shell_sort(list):
    n = len(list)
    gap = n // 2  # 步长
    while gap >= 1: # 4，2，1步长
        for i in range(gap,n):
            while (i - gap) >= 0: # 使数据能不断向左插入
                if list[i] < list[i - gap]:
                    list[i],list[i - gap] = list[i - gap],list[i]
                i -= gap

        gap //= 2 # 缩短步长

list = [2, 8, 1, 4, 7, 3, 5, 6]
shell_sort(list)
print(list)

































