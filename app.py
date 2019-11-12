"""
app封装数据：
    框架搭建：
    核心：api + case + data
    api---封装请求业务（requests）
    case -- 集成unittest 实现，调用api以及参数化解析data
    data--- 等着测试数据
    报告： report + tools + run_suite.py
    report---保存测试报告
    tools--封装工具文件
    run_suite.py--组织测试套件
    配置： app.py
    app.py--封装程序常量以及配置信息
    日志： log
    log--保存日志文件

"""
import logging
import os
import logging.handlers

# 封装接口的URL前缀

BASE_URL = 'http://182.92.81.159'

# 封装项目路径

FTLE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FTLE_PATH)
print('动态获取的绝对路径', PRO_PATH)

# 定义一个变量
TOKEN = None
USER_ID = None


# USER_ID1 = None

# 日志模块实现
# 配置日志，默认的日志配置不能满足需求
def my_log_config():
    # 获取日志对象
    login = logging.getLogger()
    # 配置输出级别  -- info 以上
    login.setLevel(logging.INFO)
    # 配置输出目标  --控制台和磁盘文件
    t1 = logging.StreamHandler()
    # 配置输出格式  --年分秒 用户 级别 python文件 函数 行号
    # 导包 import logging.handlers
    t2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + '/log/hello.log',
                                                   when='h',
                                                   interval=10,
                                                   backupCount=10,
                                                   encoding='utf-8')

    # 组织配置并添加进日志对象
    a = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    t1.setFormatter(a)
    t2.setFormatter(a)
    login.addHandler(t1)
    login.addHandler(t2)


# 调用 在需要的位置调用日志输出
# 需求 为测试类的测试函数添加日志输出
# 步骤1 import app   app.my_log_config
# 步骤2 在测试函数中调用logging.xxx(日志信息)
my_log_config()
logging.info('hhh')
