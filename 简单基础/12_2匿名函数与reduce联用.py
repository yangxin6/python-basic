"""
reduce 可以传三个参数：
    第一个是必传项，合并规则，即函数
    第二个是必传项，可迭代对象
    第三个是可选项，初始的值
"""

# 计算 1+2+3+ ... +100
from functools import reduce

res1 = reduce(lambda x, y: x + y, range(1, 101), 0)
print(res1)

# 不指定初始值
res = reduce(lambda x, y: x + y, range(1, 101))
print(res)

# 字符串合并
list1 = ['Today', 'is', 'the', 'first', 'day', 'of', 'the', 'rest', 'of', 'your', 'life']
res2 = reduce(lambda x, y: x + ' ' + y, list1)
print(res2)


