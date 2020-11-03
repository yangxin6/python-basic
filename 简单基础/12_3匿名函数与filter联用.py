# 过滤出年龄不小于30的

ages = [18, 19, 20, 40, 24, 99]
res = filter(lambda n: n >= 30, ages)
print(list(res))

# 过滤出裁判
name = ['Jame is super star', 'harden is super star', 'Jack is referee']
res1 = filter(lambda x: x.endswith('referee'), name)
print(list(res1))
