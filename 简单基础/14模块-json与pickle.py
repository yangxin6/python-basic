# json序列化
import json

dic = {'name': '杨', 'age': 18}

with open('db1.son', 'wt', encoding='utf-8') as f:
    json.dump(dic, f)

# 反序列化
with open('db1.son', 'r', encoding='utf-8') as f:
    dic = json.load(f)
    print(dic)

# pickle序列化
import pickle

s = {1, 2, 3, 4}
res = pickle.dumps(s)
print(res, type(res))

with open('db2.pkl', 'wb') as f:
    f.write(res)

# 反序列化
with open('db2.pkl', 'rb') as f:
    data = f.read()
    s = pickle.loads(data)
    print(s, type(s))

# dump 与 load
import pickle
s = {7, 8, 9}
with open('db3.pkl', 'wb') as f:
    pickle.dump(s, f)

# 反序列化
with open('db3.pkl', 'rb') as f:
    s = pickle.load(f)
    print(s, type(s))