# 一次排序


def quick_sort(list,start,end):
    if start >= end:
        return

    n = len(list)
    left = start  # 左游标，即最左那位数开始
    right = end  # 右游标，即最右那位数开始
    mid = list[left]  # 中间值

    while left < right:  # 左游标等于右游标时停止
        while left < right and list[right] >= mid:
            right -= 1
        list[left] = list[right]

        while left < right and list[left] < mid:
            left += 1
        list[right] = list[left]
    list[left] = mid  # 最终左右游标会重叠，将中间值赋值给这里，此处的左边都比中间值小，右边的都比中间值大。

    # 使用递归函数
    quick_sort(list,start,left-1) # 继续排序左边的列表
    quick_sort(list,left+1,end) # 继续排序右边的列表，最终就会得到有序的列表

list = [5, 8, 5, 5, 3, 2, 5, 1]
quick_sort(list,0,len(list)-1)
print(list)






















