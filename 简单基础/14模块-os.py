import os

res = os.getcwd()
print(res)

res = os.listdir()
print(res)

print(os.sep)
print([os.linesep, ])
print(os.pathsep)

print(os.system('ls'))

# os.path 系列
file_path = r'file/a/b/c/1'
print(os.path.abspath(file_path))

res = os.path.split(r'file/a/b/c/1')
print(res)
print(res[-1])
print(res[0])

print(os.path.isabs(file_path))
print(os.path.isabs(r'/code/python基础/简单基础/file/a/b/c/1'))

BAS_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = r'%s/db/db.txt' % BAS_DIR
print(BAS_DIR)
print(DB_PATH)


# 判断文件存在
print(os.path.exists(r'/code/python基础/简单基础/file/12312'))
print(os.path.exists(r'/Users/yang/deepLearning/python基础/code/python基础/12312'))
print(os.path.isfile(r'/code/python基础/简单基础/file/12312'))

# 判断文件夹是否存在
print(os.path.isdir(r'/code/python基础/简单基础/file'))
print(os.path.join('/code', 'python基础', 'file', '12312'))
print(os.path.join('/code', 'python基础', '/Users/yang', 'code'))
print(os.path.join('file', 'a', 'b', 'c', '1'))

# 得到文件大小
res = os.path.getsize(file_path)
print(res)

