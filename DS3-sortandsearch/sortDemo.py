"""
插入排序
"""

# def insert_sort(arr):
#     for i in range(1, len(arr)):
#         preIndex = i - 1
#         current = arr[i]
#         while preIndex >= 0 and arr[preIndex] > current:
#             arr[preIndex + 1] = arr[preIndex]
#             preIndex -= 1
#         arr[preIndex + 1] = current
#     return arr
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(insert_sort(alist))

"""
选择排序
"""

# def select_sort(arr):
#     for i in range(len(arr) - 1):
#         # 记录最小数的索引
#         minIndex = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[minIndex]:
#                 minIndex = j
#         # i 不是最小数时，将 i 和最小数进行交换
#         if i != minIndex:
#             arr[i], arr[minIndex] = arr[minIndex], arr[i]
#
#     return arr
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(select_sort(alist))


"""
冒泡排序
"""

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(1,len(arr)-i):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#     return arr
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(bubble_sort(alist))

# 改进冒泡排序
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         found=False
#         for j in range(1,len(arr)-i):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#                 found=True
#         if not found:
#             break
#     return arr
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(bubble_sort(alist))

"""
希尔排序
"""

# def shell_sort(arr):
#     import math
#     gap = 1
#     while (gap < len(arr) / 3):
#         gap = gap * 3 + 1
#         print(gap)
#     while gap > 0:
#         for i in range(gap, len(arr)):
#             temp = arr[i]
#             j = i - gap
#             while j >= 0 and arr[j] > temp:
#                 arr[j + gap] = arr[j]
#                 j -= gap
#             arr[j + gap] = temp
#         gap = math.floor(gap / 3)
#     return arr
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(shell_sort(alist))

"""
快速排序
"""


# def quick_sort(lst):
#     qsort_rec(lst, 0, len(lst) - 1)
#     return lst
#
# def qsort_rec(lst, l, r):
#     if l >= r:
#         return  # 分段无记录或只有一个记录
#     i = l
#     j = r
#     pivot = lst[i]  # lst[i]是初始空位
#     while i < j:  # 找pivot的最终位置
#         while i < j and lst[j] >= pivot:
#             j -= 1  # 用j向左扫描找小于pivot的记录
#         if i < j:
#             lst[i] = lst[j]
#             i += 1  # 小记录移到左边
#         while i < j and lst[i] <= pivot:
#             i += 1  # 用i向右扫描找大于pivot的记录
#         if i < j:
#             lst[j] = lst[i]
#             j -= 1  # 大记录移到右边
#     lst[i] = pivot  # 将pivot存入其最终位置
#     qsort_rec(lst, l, i - 1)  # 递归处理左半区间
#     qsort_rec(lst, i + 1, r)  # 递归处理右半区间
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(quick_sort(alist))

# def quick_sort1(lst):
#     def qsort(lst, begin, end):
#         if begin >= end:
#             return
#         pivot = lst[begin]
#         i = begin
#         for j in range(begin + 1, end + 1):
#             if lst[j] < pivot:  # 发现一个小元素
#                 i += 1
#                 lst[i], lst[j] = lst[j], lst[i]  # 小元素就位
#         lst[begin], lst[i] = lst[i], lst[begin]  # 枢轴元就位
#         qsort(lst, begin, i - 1)
#         qsort(lst, i + 1, end)
#
#     qsort(lst, 0, len(lst) - 1)
#     return lst
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(quick_sort1(alist))


# def quickSort(arr, left=None, right=None):
#     left = 0 if not isinstance(left, (int, float)) else left
#     right = len(arr) - 1 if not isinstance(right, (int, float)) else right
#     if left < right:
#         partitionIndex = partition(arr, left, right)
#         quickSort(arr, left, partitionIndex - 1)
#         quickSort(arr, partitionIndex + 1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot + 1
#     i = index
#     while i <= right:
#         if arr[i] < arr[pivot]:
#             swap(arr, i, index)
#             index += 1
#         i += 1
#     swap(arr, pivot, index - 1)
#     return index - 1


# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(quickSort(alist))


'''
    归并排序
'''
def mergeSort(alist):
    print('拆分的列表',alist)
    if len(alist) > 1:
        mid = len(alist)//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i = i + 1
            else:
                alist[k] = rightHalf[j]
                j = j + 1

            k = k + 1
        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i = i + 1
            k = k + 1
        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print('合并：',alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)