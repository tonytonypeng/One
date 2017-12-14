def select_sort(list):
    n = len(list)
    for j in range(n-1):
        tmp = j
        for i in range(j+1,n):
            if list[i] < list[tmp]:
                tmp = i
        list[j],list[tmp]= list[tmp],list[j]

list = [2, 8, 1, 4, 7, 3, 5, 6]
select_sort(list)
print(list)








