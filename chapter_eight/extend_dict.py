"""
扩展字典元组列表

"""


# 定义 ValueDict 类，继承 diet
class ValueDict(dict):
    # 定义构造函数
    def __init__(self, *args, **kwargs):
        # 调用父类的构造函数
        super().__init__(*args, **kwargs)

    # 新增 get_keys 方法
    def get_keys(self, val):
        result = []
        for key, value in self.items():
            if value == val:
                result.append(key)
        return result


my_dict = ValueDict(语文=92, 数学=89, 英语=92)
# 获取 92 对应的所有 key
print(my_dict.get_keys(92))  # 语文 英语
my_dict['编程'] = 92
print(my_dict.get_keys(92))  # 语文 英语 编程
