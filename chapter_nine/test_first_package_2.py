# 导入 fk package 包，实际上就是导入包下的 init .py 文件
import first_package
# 导入 fk package 包下的 pri t_shape 模块
# 实际上就是导入 fk_package 目录下的 print_shape py
import first_package.print_shape
# 导入 fk package 包下的 billing 模块
# 实际上就是导入 fk_package 目录下的 billing.py
from first_package import billing
# 导入 fk_package 包下的 arithmetic_chart 模块
# 实际上就是导入 fk package 目录下的 arithmetic_cha.rt. py
import first_package.arithmetic_chart
first_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
first_package.arithmetic_chart.print_multiple_chart(5)

'''
上面程序 第一行粗体字代码是“ import fk package ”，由于导入包 本质只是加载并执行包里
的一init .py 文件，因此执行这条导入语句之后，程序只能使用 fk_package 目录下的一init_.py
件中定义的程序单元。对于本例而言，由于 fk_package＼一init_.py 件内 容为空，因此这条导入语
句没有任何作用。
第二行粗体字代码是 impo盯住_package. print_ shape 飞这条导入语句的本质就是加载并执行
fk_package 包下的 print shape.py 文件，并将其赋值给 fk_package.print shape 变量。因此执行这条
导入语句之后 程序可访 fk_package\print_ shape. py 文件所定义的程序单元，但需要添加
fk _package.print_ shape 前缀。
行粗体字代码是“ om fk_package imp01t billing 飞这条导入语句的本质是导入 fk_package
包（也是模块〉下的 illing 成员（其实是模块）。因此执行这条导入语句之后，程序可使用
fk _package\bil I ing. py 文件定义的程序单元，而且只需要添加 billing 前缀
第四行粗体字代码与第 行粗体字代码 导入效果相同。
该程序后面分别测试了 fk_package 包下的 print_shape billing arithmetic chart 个模块的
功能。运行上面程序，可以看到 个模块的功能完全可以正常显示
上面程序虽然可以正常运行，但此时存在两个 题。
〉为了调用包内模块中的程序单元，需要使用很长的前缀，这实在是太麻烦了
〉包内一init py 文件的功能完全被 略了。
'''
