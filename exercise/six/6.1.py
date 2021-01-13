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
        print('%s吃了%s' % (self.name, food))

    def drink(self, drinks):
        print('%s喝了%s' % (self.name, drinks))

    def play(self, games):
        print('%s正在玩%s' % (self.name, games))

    def sleep(self):
        print('%s睡觉了！' % self.name)


student1 = Student('张三', 18, '男', '15215537653', '上海市黄浦区', 'haha@qq.com')
student1.eat('apple')
student1.drink('金徽酒')
student1.play('英雄联盟')
student1.sleep()
