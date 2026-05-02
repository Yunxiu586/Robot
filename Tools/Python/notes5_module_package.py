# 模块Module
# 是一个Python文件，以.py结尾
# [from 模块名] import [模块|类|变量|函数|*][as 别名]

# Ctrl+左键 查看模块源代码
import time
time.sleep(1) # 程序休眠1sec
print("1 sec")

# 单独导入sleep函数
from time import sleep
sleep(1)
print("2 sec")

# 导入模块全部模块
from time import *
sleep(1)
print("3 sec")

# 别名
import time as tm
tm.sleep(1)
print("4 sec")

from time import sleep as slp
slp(1)
print("5 sec")

# 自定义模块
import demo_module as dm
print(f'1+2={dm.plus(1,2)}')
print(f'1-2={dm.minus(1,2)}')

# 当导入多个模块的同名功能时，后调用的会将先调用的代码覆盖

# 包Package
# 是一个文件夹，包含一个__init__.py，可以包含多个模块文件
# 从逻辑上看，包的本质依然是模块

import demo_Package.module1
demo_Package.module1.module1_func1()
demo_Package.module1.module1_func2()

from demo_Package import module2
module2.module2_func1()
module2.module2_func2()

from demo_Package.module2 import module2_func1
module2_func1()

from my_utils.str_util import *
print(str_revers('abcd'))
print(substr('abcdefg',1,3))

from my_utils.file_util import *
print_file_info('D:/Python_study/PythonProject/demo1.txt')
print_file_info('D:/Python_study/PythonProject/demo3.txt')
append_to_file('D:/Python_study/PythonProject/demo2.txt','\nappend')