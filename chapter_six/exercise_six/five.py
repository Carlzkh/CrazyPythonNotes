"""
5. 定义交通工具、汽车、火车、飞机这些类，注意它们的继承关系 ，为这些类提供构造器
Vehicles, cars, trains, airplanes
"""


class Vehicles:
    def __init__(self, name, speed, ticket_price, price):
        self.name = name
        self.speed = speed
        self.ticket_price = ticket_price
        self.price = price


class Cars(Vehicles):
    pass


class Trains(Vehicles):
    pass


class Airplanes(Vehicles):
    pass


c = Cars('bmw', 200, 100, 200000)
print(c.name, c.price, c.ticket_price, c.speed)
