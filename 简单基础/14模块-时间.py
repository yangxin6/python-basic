import time

# 1、时间戳
print(time.time())
start_time = time.time()
time.sleep(3)
end_time = time.time()
print(end_time - start_time)

# 2、格式化的字符串
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
print(time.strftime('%Y-%m-%d %X %p'))

# 3、struct_time 对象
print(time.localtime())  # 上海： 东八区
print(time.localtime().tm_year)
print(time.localtime().tm_mday)
print(time.gmtime())  # UTC时区

print(time.localtime(111).tm_hour)
print(time.gmtime(11111).tm_hour)

print(time.mktime(time.localtime()))

print(time.strftime('%Y/%m/%d', time.localtime()))
print(time.strptime('2017/04/08', '%Y/%m/%d'))

print(time.asctime(time.localtime()))
print(time.ctime(123))

print("~~~~~~~~~~~~~~~~~~~~")


def progress(percent, width=50):
    if percent > 1:
        percent = 1
    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
    print('\r%s %d%%' % (show_str, int(100 * percent)), end='')


recv_size = 0
total_size = 102400
while recv_size < total_size:
    time.sleep(0.1)
    recv_size += 4096
    percent = recv_size / total_size
    progress(percent)

print('============datetime=============')
import datetime

print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=3))
print(datetime.datetime.now() + datetime.timedelta(days=-3))
print(datetime.datetime.now() + datetime.timedelta(hours=3))
print(datetime.datetime.now() + datetime.timedelta(seconds=111))
current_time = datetime.datetime.now()
print(current_time.replace(year=1999))
print(datetime.date.fromtimestamp(1111111))
