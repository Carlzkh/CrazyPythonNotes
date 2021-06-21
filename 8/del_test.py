class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 定义析构函数
    def __del__(self):
        print('del 删除对象')


# 创建一个 Item 对象，将之赋值给 im 变量
im = Item('鼠标', 29.8)  # 创建对象，并赋给im
x = im  # ①将im赋给x，此时程序有im和x两个变量引用对象
# 打印 im 所引用的 Item 对象
del im  # 不会删除对象，等对象的所有引用均结束时，才会删除对象
print('程序最后，但不代表最后执行，看删除对象')
