import shutil
import tarfile
import time

# 压缩文件
ret = shutil.make_archive(
    base_name="模块对象_%s" % time.strftime("%Y-%m-%d"),
    format='gztar',
    base_dir='file'
)


# 解压文件
t = tarfile.open('/code/python基础/简单基础/模块对象_2020-10-12.tar.gz',
                 'r')
t.extractall(r'/Users/yang/deepLearning/python基础/code/python基础/extract')
t.close()