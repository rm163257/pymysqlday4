"""
    测试员工模块的增删改查实现
"""

# 1导包
import unittest
import requests
import logging
# 2 创建测试类
import app
from api.emp_api import EmpCRUD


class TestEmp(unittest.TestCase):
    # 3 初始化函数
    def setUp(self) -> None:
        self.session = requests.session()
        self.emp_obj = EmpCRUD()

    # 4 资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5 测试函数 1 完成员工的新增
    # 测试函数失败 因为要先执行登录 2 还需要提交token
    # 解决1 使用测试套件组织接口的执行顺序
    #     2 如何提交银行卡  如何实现关联
    # token 获取   在提交

    def test_add(self):
        logging.info('登录信息')
        # 1 请求业务
        response = self.emp_obj.test_add(self.session, username='rmrmrm14', mobile='16738749822')
        print('员工新增响应结果', response.json())
        id = response.json().get('data').get('id')
        app.USER_ID = id
        print('新增员工的id', id)
        # 2 断言业务
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 6测试函数 改
    def test_update(self):
        logging.warning('修改信息')
        response1 = self.emp_obj.test_update(self.session, app.USER_ID, 'rmrmrm11')
        print('员工修改响应结果', response1.json())
        self.assertEqual(True, response1.json().get('success'))
        self.assertEqual(10000, response1.json().get('code'))
        self.assertIn('操作成功', response1.json().get('message'))

        # 7测试函数 查

    def test_get(self):
        logging.info('查看信息')
        response2 = self.emp_obj.test_get(self.session, app.USER_ID)
        print('员工查询响应结果', response2.json())
        # 断言业务
        self.assertEqual(True, response2.json().get('success'))
        self.assertEqual(10000, response2.json().get('code'))
        self.assertIn('操作成功', response2.json().get('message'))

    # 8测试函数 删除
    def test_delete(self):
        logging.warning('删除信息')
        response3 = self.emp_obj.test_delete(self.session, app.USER_ID)
        print('员工删除响应结果', response3.json())
        # 断言业务
        self.assertEqual(True, response3.json().get('success'))
        self.assertEqual(10000, response3.json().get('code'))
        self.assertIn('操作成功', response3.json().get('message'))
