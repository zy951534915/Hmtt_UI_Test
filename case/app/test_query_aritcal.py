# 导包
import unittest

from parameterized import parameterized

from page.app.index_page import IndexProxy
from utils import DriverUtils, is_element_by_attribute


# 定义测试类
class TestQyAritcal(unittest.TestCase):
    # 定义初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取app驱动对象
        cls.driver = DriverUtils.get_app_driver()
        # 创建首页业务层对象
        cls.index_proxy = IndexProxy()

    def setUp(self):
        self.driver.start_activity("com.itcast.toutiaoApp", ".MainActivity")

    # 定义测试方法
    @parameterized.expand(["架构", "开发者资讯"])
    def test_qy_aritcal(self, channel_name):
        # 组织测试数据
        # channel_name = "架构"
        # 调用根据频道查询文章的业务方法
        self.index_proxy.test_qari_by_channel(channel_name)
        # 断言
        self.assertTrue(is_element_by_attribute(self.driver, "text", "点赞"))

    # 定义销毁方法
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_app_driver()
