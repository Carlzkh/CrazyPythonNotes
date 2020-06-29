# 导入 fk_package 包，实际上就是导入该包下的＿in py 文件
import first_package
# 直接使用 fk_package 前缀即可调用它所包含的模块内的程序单元
first_package.print_blank_triangle(5)
im = first_package.Item(4.5)
print(im)
first_package.print_multiple_chart(5)

print('dir(first_package):', dir(first_package))
# print(first_package.__all__)
print('Item:', first_package.Item)
# print('__builtins__:', first_package.__builtins__)
print('__cached__:', first_package.__cached__)
print('__doc__:', first_package.__doc__)
print('__file__:', first_package.__file__)
print('__loader__:', first_package.__loader__)
print('__name__', first_package.__name__)
print('__package__:', first_package.__package__)
print('__path__:', first_package.__path__)
print('__spec__:', first_package.__spec__)



