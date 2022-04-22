import pizza
# 导入特定的函数
from pizza import make_pizza
# 使用as起别名
from pizza import make_pizza as mp
# 给模块起别名
import pizza as p
# 导入模块中的所有函数
from pizza import *

pizza.make_pizza(20, 'curry', 'harden')
make_pizza(20, 'curry', 'harden')
mp(20, 'curry', 'harden')
p.make_pizza(20, 'curry', 'harden')
