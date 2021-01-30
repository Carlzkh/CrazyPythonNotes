"""
3. 定义一个 fk_package 并在该包下提供 foo bar 两个模块，在每一个模块 又包含任
意两个函数
"""
import fk_package  # __init__.py导入的模块才可以被import直接导入

fk_package.foo.foo_one()
fk_package.bar.bar_two()
print(fk_package.bar.__file__)
