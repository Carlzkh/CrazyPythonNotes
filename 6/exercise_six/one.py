"""
1. 个学生类，提供 name age gender phone address 、email 等属性，为学生类提供
带所有成员变量的构造器，为学生类提供方法，用于描绘吃、喝、玩、睡等行为。
"""


class Student:
    def __init__(self, name, age, gender, phone, address, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email

    def eat(self, food):
        print('%s在吃%s' % (self.name, food))

    def drink(self, drinks):
        print('%s在喝%s' % (self.name, drinks))

    def play(self):
        print('%s在玩%s' % (self.name, self.phone))

    def sleep(self):
        print('%s在睡觉' % self.name)


stu = Student('张三', 18, '二年级', 18325632542, '顾景路7号', '45213568854@qq.com')
stu.eat('米饭')
stu.play()








