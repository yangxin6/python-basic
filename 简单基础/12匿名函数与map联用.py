nums = [i for i in range(1, 6)]

# 数字映射
res = map(lambda x: x ** 2, nums)
print(res)
print(list(res))

# 字符串映射
names1 = ['jack', 'tom', 'lucy', 'ming']
res1 = map(lambda x: x + ' is super star', names1)
print(list(res1))

names2 = ['jack', 'tom', 'lucy', 'ming']
res2 = map(lambda x: x + ' is super star' if x == 'ming' else x + ' is referee', names2)
print(list(res2))
