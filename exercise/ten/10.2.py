"""
2. 给定 1个字符串，该宇符~只包含数字 、英文逗号、英文点号，请使用英文逗号、英
文点号将它们分割成多个子串
"""


def split_string(to_be_split_string):
    list1 = to_be_split_string.split(',')
    for i in range(len(list1)):
        list2 = list1[0].split('.')
        del list1[0]
        list1 = list1 + list2
    return list1


print(split_string('12,.,44..324.325.5,45,3,.45,4'))








