# # 桶排序
# # def bucket_sort():
# #     a = [95, 45, 56, 45, 3, 60]
# #     b = []
# #     for i in range(1001):
# #         b.append(0)
# #     for i in a:
# #         b[i] += 1
# #     for i in range(1000, -1, -1):
# #         for j in range(b[i]):
# #             print(i)
# #
# #
# # bucket_sort()
#
#
# # 冒泡排序
# # def bubble_sort():
# #     a = [95, 45, 56, 45, 3, 60]
# #     for i in range(len(a)-1):
# #         for j in range(len(a)-i-1):
# #             if a[j] > a[j+1]:
# #                 a[j], a[j+1] = a[j+1], a[j]
# #     print(a)
# #
# #
# # bubble_sort()
#
#
# # 快速排序
# # def quick_sort(a):
# #     if len(a) < 2:
# #         return a
# #     mid = a[len(a) // 2]
# #     left, right = [], []
# #     a.remove(mid)
# #     for item in a:
# #         if item >= mid:
# #             right.append(item)
# #         else:
# #             left.append(item)
# #     return quick_sort(left) + [mid] + quick_sort(right)
# #
# #
# # print(quick_sort([95, 45, 56, 45, 3, 60]))
#
#
# # 队列
# # def sequence():
# #     a = [6, 3, 1, 7, 5, 8, 9, 2, 4, 9]
# #     b = []
# #     j = 0
# #     for i in range(len(a)):
# #         b.append(a[j])
# #         try:
# #             a.append(a[j+1])
# #         except Exception as e:
# #             print(e)
# #         j += 2
# #     print(b)
# #
# #
# # sequence()
#
#
# # 选择排序
# # def selection_sort(arr):
# #     for i in range(len(arr) - 1):
# #         min_index = i
# #         for j in range(i + 1, len(arr)):
# #             if arr[j] < arr[min_index]:
# #                 min_index = j
# #         arr[min_index], arr[i] = arr[i], arr[min_index]
# #     return arr
# # a = [6, 3, 1, 7, 5, 8, 9, 2, 4, 9]
# # print(selection_sort(a))
#
#
# # 插入排序
# # def insertion_sort(arr):
# #     for i in range(1, len(arr)):
# #         current = arr[i]
# #         pre_index = i - 1
# #         while pre_index >= 0 and arr[pre_index] > current:
# #             arr[pre_index + 1] = arr[pre_index]
# #             pre_index -= 1
# #         arr[pre_index + 1] = current
# #     return arr
# # a = [6, 3, 1, 7, 5, 8, 9, 2, 4]
# # print(insertion_sort(a))
# # 希尔排序
# # def shell_sort(arr):
# #     gap = len(arr) // 2
# #     while gap > 0:
# #         for i in range(gap, len(arr)):
# #             j = i
# #             current = arr[i]
# #             while j - gap >= 0 and current < arr[j - gap]:
# #                 arr[j] = arr[j - gap]
# #                 j -= gap
# #             arr[j] = current
# #         gap //= 2
# #     return arr
# # a = [6, 3, 1, 7, 5, 8, 9, 2, 4]
# # print(shell_sort(a))
#
# # 归并排序
# # def merge_sort(arr):
# #     if len(arr) == 1:
# #         return arr
# #     mid = len(arr) // 2
# #     left = arr[:mid]
# #     right = arr[mid:]
# #     return marge(merge_sort(left), merge_sort(right))
# #
# #
# # def marge(left, right):
# #     result = []
# #     while len(left) > 0 and len(right) > 0:
# #         if left[0] <= right[0]:
# #             result.append(left.pop(0))
# #         else:
# #             result.append(right.pop(0))
# #     result += left
# #     result += right
# #     return result
# # a = [6, 3, 1, 7, 5, 8, 9, 2, 4]
# # print(merge_sort(a))
#
# # 基数排序
# # def radix_sort(s):
# #     i = 0
# #     max_num = max(s)
# #     j = len(str(max_num))
# #     while i < j:
# #         bucket_list = [[] for _ in range(10)]
# #         for x in s:
# #             bucket_list[int(x / (10 ** i)) % 10].append(x)
# #         s.clear()
# #         for x in bucket_list:
# #             for y in x:
# #                 s.append(y)
# #         i += 1
# #     return s
# #
# #
# # a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
# # print(radix_sort(a))
#
# # 计数排序
# # def count_sort(l, max_value):
# #     result = []
# #     container = [0 for _ in range(0, max_value + 1)]
# #     for one in l:
# #         container[one] += 1
# #     for index in range(0, len(container)):
# #         while container[index] > 0:
# #             result.append(index)
# #             container[index] -= 1
# #     return result
#
# # a = [2, 5, 3, 0, 2, 3, 0, 3]
# # print(count_sort(a, max(a)))
#
# # 堆排序
# # 拓扑排序
