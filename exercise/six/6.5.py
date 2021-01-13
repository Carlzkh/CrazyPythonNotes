"""
5. 定义交通工具、汽车、火车、飞机这些类，注意它们的继承关系 ，为这些类提供构造器
"""


class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        print('%s以%s的速度跑着！' % (self.name, self.speed))


class Car(Vehicle):
    pass


class Train(Vehicle):
    def __init__(self, carriage, name, speed):
        super().__init__(name, speed)
        self.carriage = carriage


class Plant(Vehicle):
    def __init__(self, company, name, speed):
        super().__init__(name, speed)
        self.company = company


a_vehicle = Vehicle('bus', 60)
a_car = Car('BMW', 120)
a_train = Train(16, '复兴号', '240km/h')
a_plant = Plant('东方航空', '波音747', 1000)

print(a_vehicle.name, a_car.speed, a_train.carriage, a_plant.company)
a_train.run()
