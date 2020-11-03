import subprocess
cmd = input('>>:')  # ls
obj = subprocess.Popen(
    cmd,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print(obj)

res1 = obj.stdout.read()  # 输出正确结果
print('正确结果：', res1.decode('utf-8'))

res2 = obj.stderr.read()  # 输出错误结果
print('错误结果：', res2.decode('utf-8'))