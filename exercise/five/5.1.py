"""
1. 定义一个函数，该函数可接收一个 list 作为参数，该函数使用直接选择排序对 list
"""


def direct_descending_order(list_to_be_sorted):
    for j in range(len(list_to_be_sorted)):
        for i in range(len(list_to_be_sorted)):
            if i+1 < len(list_to_be_sorted):
                if list_to_be_sorted[i] > list_to_be_sorted[i+1]:
                    continue
                else:
                    list_to_be_sorted[i], list_to_be_sorted[i+1] = list_to_be_sorted[i+1], list_to_be_sorted[i]
    list_sorted = []
    for k in range(len(list_to_be_sorted)):
        list_sorted.append(list_to_be_sorted[k])
    return list_sorted


def direct_ascending_order(list_to_be_sorted):
    for j in range(len(list_to_be_sorted)):
        for i in range(len(list_to_be_sorted)):
            if i+1 < len(list_to_be_sorted):
                if list_to_be_sorted[i] < list_to_be_sorted[i+1]:
                    continue
                else:
                    list_to_be_sorted[i], list_to_be_sorted[i+1] = list_to_be_sorted[i+1], list_to_be_sorted[i]
    list_sorted = []
    for k in range(len(list_to_be_sorted)):
        list_sorted.append(list_to_be_sorted[k])
    return list_sorted


list1 = [8, 3, 1, 4, 6, 5, 9, 7]
list2 = direct_descending_order(list1)
list3 = direct_ascending_order(list1)
print(list1, list2, list3)
