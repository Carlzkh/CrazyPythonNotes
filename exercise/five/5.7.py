"""
7. 定义 个函数，该函数可接收 list 作为参数，该函数用于去除 list 中重复的元素
"""


def list_removal_duplicates(list_to_be_removal_duplicates):
    list_removed_duplicate = []
    for i in range(len(list_to_be_removal_duplicates)):
        if list_to_be_removal_duplicates[i] in list_removed_duplicate:
            continue
        else:
            list_removed_duplicate.append(list_to_be_removal_duplicates[i])
    return list_removed_duplicate


list1 = [1, 1, 2, 5, 2, 5, 6, 8]
list2 = ['a', 1, 2, 'a', 2, 5, 'c', 8]
list3 = ['!', 1, 2, 5, '!', 5, '!', 8]
print(list_removal_duplicates(list1))
print(list_removal_duplicates(list2))
print(list_removal_duplicates(list3))
