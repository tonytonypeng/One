# 归并排序


def merge_sort(list):
    if len(list) == 1:  # 调用递归函数结束点
        return list   # 最终列表长度都会是1
    n = len(list)
    mid = n // 2    # 分割点，每次列表长度取一半
    left_list = list[:mid]     # 分割成左边列表
    right_list = list[mid:]     # 分割成右边列表
    left_result = merge_sort(left_list)  # 调用递归函数对左边列表再次分割
    right_result = merge_sort(right_list)  # 调用递归函数对右边列表再次分割
    merge_list = merge(left_result,right_result)  # 调用排序函数返回排序好的列表
    return merge_list


def merge(left,right):  # 定义排序函数
    left_addr = 0  # 左边列表最左位
    right_addr = 0  # 右边列表最左位
    result = []   # 最终列表
    while (left_addr < len(left)) and (right_addr < len(right)):  # 循环条件：遍历位不能唱过列表的长度
        if left[left_addr] <= right[right_addr]:  # 当左边列表的数小于右边的时，左数在result的靠左位置放置
            result.append(left[left_addr])     # 左右列表默认都是有序的，只是需要按照大小将他们依次封装到最终列表
            left_addr += 1
        else:
            result.append(right[right_addr])  # 与上面相反
            right_addr += 1
    result += left[left_addr:]   # 当上面没有遍历完所有数据所做的操作，继续将终止位之后的数据添加到进去
    result += right[right_addr:]
    return result

list = [2,5,1,6,3,7,8,4]
print(merge_sort(list))



































