"""
    测试套件
        按照需求组合被执行的测试函数
    自动化测试执行顺序
    增---改---查---删
    关于测试套件的组织 -- 接口业务测试中，需要保证测试套件中接口执行顺序
    合法实现suite.addtest(类名（函数名）)逐一添加
    非法实现 suite.addtest(unittest.makesuite(类名))可以一次性添加多个测试函数，单无法保证执行顺序

"""

# 1 导包
import unittest
# 2 实例化套件对象 组织被执行的测试函数
import app
from api.login_api import Login
from case.test_IHPM_login import TestLogin
from case.test_IHRM_emp import TestEmp
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestLogin('test_login_success'))  # 组织登录成功的测试函数
suite.addTest(TestEmp('test_add'))  # 组织员工新增的测试函数
suite.addTest(TestEmp('test_update'))  # 组织员工修改测试函数
suite.addTest(TestEmp('test_get'))     # 组织员工查询测试函数
suite.addTest(TestEmp('test_delete'))  # 组织员工删除测试函数

# 3 执行套件 生成报告
# runner = unittest.TextTestRunner()
# runner.run(suite)


with open(app.PRO_PATH + '/report/report.html','wb')as f:
    runner = HTMLTestRunner(f,title='人力资源管理系统测试报告',
                            description='测试了员工模块')
    runner.run(suite)


