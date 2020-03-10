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


def shell_sort(arr):
    import math
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
        print(gap)
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap=math.floor(gap/3)
    return arr

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(shell_sort(alist))
