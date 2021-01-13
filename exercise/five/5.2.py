"""
2. 定义一个函数，该函数可接收一个 list 作为参数，该函数使用冒泡排序对 list
"""


def bubble_ascending_sort(list_to_be_sorted):
    list_sorted = []
    for i in range(len(list_to_be_sorted)):
        list_min = min(list_to_be_sorted)
        list_sorted.append(list_min)
        list_to_be_sorted.remove(list_min)
    return list_sorted


def bubble_descending_sort(list_to_be_sorted):
    list_sorted = []
    for i in range(len(list_to_be_sorted)):
        list_max = max(list_to_be_sorted)
        list_sorted.append(list_max)
        list_to_be_sorted.remove(list_max)
    return list_sorted


list1 = [8, 3, 1, 4, 6, 9, 2, 7]
list2 = bubble_ascending_sort(list1)
list3 = [8, 3, 1, 4, 6, 9, 2, 7]
list4 = bubble_descending_sort(list3)
print(list1, list2, list3, list4, sep='\n')
