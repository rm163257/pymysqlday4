"""
    封装 unittest 相关实现
"""

# 1 导包
import json
import unittest
import requests
from parameterized import parameterized
import app


# 参数化解析

def read_json():
    with open(app.PRO_PATH + '/data/login_data.json', encoding='utf-8')as f:
        data = json.load(f).values()
        data_list = list()
        for i in data:
            data_list.append((i.get('mobile'),
                              i.get('password'),
                              i.get('success'),
                              i.get('code'),
                              i.get('message'),
                              ))
        return data_list


# 2 创建测试类
from api.login_api import Login


class TestLogin(unittest.TestCase):
    # 3 初始化函数
    def setUp(self) -> None:
        # 初始化session
        self.session = requests.session()
        # 初始化api对象
        self.login_obj = Login()

    # 4资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5 核心 ： 测试函数 -- 登录
    # 5-1 参数化
    # 调用参数化
    @parameterized.expand(read_json())
    def test_login(self, mobile, password, success, code, message):
        print('参数化读取数据', mobile, password, success, code, message)
        # 5-2 请求业务
        response = self.login_obj.login(self.session, mobile, password)
        print('登录响应结果', response.json())
        # 5-3 断言业务
        self.assertEqual(success, response.json().get('success'))
        self.assertEqual(code, response.json().get('code'))
        self.assertIn(message, response.json().get('message'))

    # 编写登录成功的测试函数
    def test_login_success(self):
        # 直接通过提交正向数据发送请求业务
        response = self.login_obj.login(self.session, '13800000002', '123456')
        # 断言业务
        print('登录成功的结果', response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
        # 提取 token
        token = response.json().get('data')
        print('登录后响应的token', token)
        # 预期允许其他文件调用该token 可以扩大token的作用域
        app.TOKEN = token
