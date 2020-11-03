import logging

logging.basicConfig(
    filename='access.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=20
)

logging.debug('debug...')
logging.info('info...')
logging.warning('快着火了...')
logging.error('着火了...')
logging.critical('火月着越大')

# logging 模块的四种对象
# 1 logger：负责产生日志
logger1 = logging.getLogger('xxx')

# 2 flitter 过滤日志（不常用）

# 3 handler: 控制日志打印到文件 or 终端
fh1 = logging.FileHandler(filename='a1.log', encoding='utf8')
fh2 = logging.FileHandler(filename='a2.log', encoding='utf8')
sh = logging.StreamHandler()

# 4 formatter: 控制日志的格式
formatter1 = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

formatter2 = logging.Formatter(fmt='%(asctime)s - %(message)s')

# 为 logging 对象绑定 handler
logger1.addHandler(fh1)
logger1.addHandler(fh2)
logger1.addHandler(sh)

# 为 handler 绑定日志格式
fh1.setFormatter(formatter1)
fh2.setFormatter(formatter1)
sh.setFormatter(formatter2)

# 日志级别： 两层关卡，必须都通过，才能正常记录
logger1.setLevel(30)
fh1.setLevel(10)
fh2.setLevel(10)
sh.setLevel(10)

# 调用 logging1 对象下的方法，产生日志，然后交给不同的handler，控制日志记录到不同的地方
logger1.debug('调试信息')
logger1.info('使用中')
logger1.warning('警告')
logger1.critical('问题很严重')
