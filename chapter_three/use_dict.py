"""
字典是key-value对，有一一映射的关系
key不允许重复

"""

'''
1、
key不可重复，不可变
元组可以做key，列表不可以
'''

'''
2、创建字典
{}赋值或dict()函数
'''
score1 = {'Chinese': 89, 'math': 98, 'English': 86}
score2 = dict()
score3 = dict(a=89, b=67)
print(score1)
print(score2)
print(score3)


'''
3、字典的基本用法
访问
增加
删除
修改
in 和 not in
'''
score1['语文'] = 89
print(score1)
score1['语文'] = 102
print(score1)
print(score1['语文'])
del score1['语文']
print(score1)
print('math' in score1)

'''
4、字典的常用方法
clear():情况键值对，变成空字典
get()：访问到没有的key时返回none，不会报错，直接用[]会报错的
update():用一个字典更新已有字典,key存在会覆盖，key不存在会新增
items()：返会所有键值对
keys()：返回所有key
values()：返回所有值
pop():获取指定key的值，并删除键值对
popitem()，获取最后一个键值对，并删除键值对
setdefault(),返回key对应的值，若没有，返回默认值，在字典新增键值对
fromkeys()使用键创建字典，值是None，也可以指定默认值
'''
print(score1.get('math'))
print(score1.get('matwdh'))
score1.update({'new': 76})  # 返回None
print(score1)

'''
5、使用字典格式化字符串

'''
print(score1)
print('语文是：%(Chinese)d分,数学是：%(math)d分,英语是：%(English)d分' % score1)














