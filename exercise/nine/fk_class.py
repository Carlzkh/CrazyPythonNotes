"""
fk_class模块，在该模块下定义了 Teacher Student Computer 三个类
"""


class Teacher:
    """
    生成一个老师
    """
    def __init__(self, name, course):
        self.name = name
        self.course = course


class Student:
    """
    生成一个学生
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Computer:
    """
    生成一个电脑
    """
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
