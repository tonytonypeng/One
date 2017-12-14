
def bubble_sort(list):
    n = len(list)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                count += 1
        if count == 0:
            return

list = [2,8,1,4,7,3,5,6]
bubble_sort(list)
print(list)
































