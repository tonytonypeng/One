def insert(list):
    n = len(list)
    for j in range(n):
        for i in range(j,0,-1):
            if list[i] < list[i-1]:
                list[i],list[i-1] = list[i-1],list[i]
            else:
                pass


list = [2, 8, 1, 4, 7, 3, 5, 6]
insert(list)
print(list)





























