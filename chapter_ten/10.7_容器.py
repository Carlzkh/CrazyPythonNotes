from collections import deque
from heapq import *

# 10.7.1 set 和 frozenset
"""
set不记录元素的添加顺序
set元素不允许重复。
set集合是可变容器，程序可以改变容器中的元素 。
frozenset是set的不可变版本，它的元素是不可变的。
"""
# 使用花括号构建set集合
c = {'白骨精'}
# 添加元素
c.add("孙悟空")
c.add(6)
print("c集合的元素个数为:", len(c))  # 输出3
# 删除指定元素
c.remove(6)
print("c集合的元素个数为:", len(c))  # 输出2
# 判断是否包含指定字符串
print("c集合是否包含'孙悟空'字符串:", ("孙悟空" in c))  # 输出True
c.add("轻量级Java EE企业应用实战")
print("c集合的元素：", c)
# 使用set()函数（构造器）来创建set集合
books = set()
books.add("轻量级Java EE企业应用实战")
books.add("疯狂Java讲义")
print("books集合的元素：", books)
# issubset()方法判断是否为子集合
print("books集合是否为c的子集合？", books.issubset(c))  # 输出False
# issubset()方法与<=运算符效果相同
print("books集合是否为c的子集合？", (books <= c))  # 输出False
# issuperset()方法判断是否为父集合
# issubset和issuperset其实就是倒过来判断
print("c集合是否完全包含books集合？", c.issuperset(books))  # 输出False
# issuperset()方法与>=运算符效果相同
print("c集合是否完全包含books集合？", (c >= books))  # 输出False
# 用c集合减去books集合里的元素，不改变c集合本身
result1 = c - books
print(result1)
# difference()方法也是对集合做减法，与用-执行运算的效果完全一样
result2 = c.difference(books)
print(result2)
# 用c集合减去books集合里的元素，改变c集合本身
c.difference_update(books)
print("c集合的元素：", c)
# 删除c集合里的所有元素
c.clear()
print("c集合的元素：", c)
# 直接创建包含元素的集合
d = {"疯狂Java讲义", '疯狂Python讲义', '疯狂Kotlin讲义'}
print("d集合的元素：", d)
# 计算两个集合的交集，不改变d集合本身
inter1 = d & books
print(inter1)
# intersection()方法也是获取两个集合的交集，与用&执行运算的效果完全一样
inter2 = d.intersection(books)
print(inter2)
# 计算两个集合的交集，改变d集合本身
d.intersection_update(books)
print("d集合的元素：", d)
# 将range对象包装成set集合
e = set(range(5))
f = set(range(3, 7))
print("e集合的元素：", e)
print("f集合的元素：", f)
# 对两个集合执行异或运算
xor = e ^ f
print('e和f执行xor的结果：', xor)
# 计算两个集合的并集，不改变e集合本身
un = e.union(f)
print('e和f执行并集的结果：', un)
# 计算两个集合的并集，改变e集合本身
e.update(f)
print('e集合的元素：', e)

# 10.7.2 双端队列 (deque)

# deque可以当作栈使用（使用append和pop）：
# from collections import deque
stack = deque(('Kotlin', 'Python'))
# 元素入栈
stack.append('Erlang')
stack.append('Swift')
print('stack中的元素：', stack)
# 元素出栈，后添加的元素先出栈
print(stack.pop())
print(stack.pop())
print(stack)

# deque也可以当作队列使用（使用append和popleft）：
# from collections import deque
q = deque(('Kotlin', 'Python'))
# 元素加入队列
q.append('Erlang')
q.append('Swift')
print('q中的元素：', q)
# 元素出队列，先添加的元素先出队列
print(q.popleft())
print(q.popleft())
print(q)

q = deque(range(5))
print('q中的元素：', q)
# 执行旋转，使之首尾相连
q.rotate()
print('q中的元素：', q)
# 再次执行旋转，使之首尾相连
q.rotate()
print('q中的元素：', q)

# 10.7.3 Python 的堆操作

# from heapq import *
my_data = list(range(10))
my_data.append(0.5)
# 此时my_data依然是一个list列表
print('my_data的元素：', my_data)
# 对my_data应用堆属性
heapify(my_data)
print('应用堆之后my_data的元素：', my_data)
heappush(my_data, 7.2)
print('添加7.2之后my_data的元素：', my_data)
# 弹出堆中最小的元素
print(heappop(my_data))  # 0
print('弹出0之后my_data的元素：', my_data)
print(heappop(my_data))  # 0.5
print('弹出两个元素之后my_data的元素：', my_data)
# 弹出最小元素，压入指定元素
print(heapreplace(my_data, 8.1))
print('执行replace之后my_data的元素：', my_data)
print('my_data中最大的3个元素：', nlargest(3, my_data))
print('my_data中最小的4个元素：', nsmallest(4, my_data))
