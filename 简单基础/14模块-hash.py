import hashlib

m = hashlib.md5()
m.update('hello'.encode('utf8'))
m.update('world'.encode('utf8'))
m.update('yang'.encode('utf8'))
print('字符串md5值：', m.hexdigest())

# md5 值校验
md = hashlib.md5()
with open('/code/python基础/简单基础/14模块-hash.py', 'rb') as f:
    for line in f:
        md.update(line)
    file_md5 = m.hexdigest()
print('md5_file', file_md5)

# 密码加密
pwd = 'yang123'
mp = hashlib.md5()
mp.update('天王盖地虎'.encode('utf8'))
mp.update(pwd.encode('utf8'))
mp.update('宝塔镇河妖'.encode('utf8'))
print('密码md5值：', mp.hexdigest())