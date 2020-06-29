"""
这是学习包的第一个示例
"""
# 从当前包中导入 pr nt_shape 模块
from . import print_shape
# 从 pr nt_shape 中导入所有程序单元到 fk_package
from .print_shape import *
# 从当前包中导入 billi 呵模块
from . import billing
# 从 billing 中导入所有程序单元到 fk_pa ckage
from . billing import *
# 从当前包中导入 arithmetic_chart 模块
from . import arithmetic_chart
# 从 arithmetic_chart 中导入所有程序单元到 fk_package
from .arithmetic_chart import *
print('this is first package')
