import time
import pytest

import config
from page.mp.home_page import HomeProxy, HomeHandle
from page.mp.login_page import LoginProxy
from page.mp.publish_artical_page import PubAriProxy
from utils import DriverUtils, is_element_exist, get_case_data


# 定义测试类
@pytest.mark.run(order=3)
class TestMpLogin:
    # 定义初始化方法
    def setup_class(self):
        # 获取驱动的对象
        self.driver = DriverUtils.get_mp_driver()
        # 创建好所需要调用业务方法所在的类的对象
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.pub_proxy = PubAriProxy()

    # 恢复到原点
    def setup_method(self):
        self.driver.get("http://ttmp.research.itcast.cn/")

    # 定义测试方法
    @pytest.mark.parametrize(("ari_title", "ari_context", "ari_channel", "expect"),
                             get_case_data("./data/mp/test_pub_data.json"))
    def test_mp_pub(self, ari_title, ari_context, ari_channel, expect):
        # 定义测试数据
        # username = "13911111111"
        # code = "246810"
        # # 调用业务方法形成完整业务操作
        # self.login_proxy.test_mp_login(username, code)
        # # 断言
        # assert is_element_exist(self.driver, "江苏传智播客")
        config.PUB_ARITCAL_TITLE = ari_title.format(time.strftime("%Y%m%d%H%S%M"))
        self.home_proxy.to_pub_ari_page()
        self.pub_proxy.to_pub_ari_tab(config.PUB_ARITCAL_TITLE, ari_context, ari_channel)
        assert is_element_exist(self.driver, expect)
        # HomeHandle().click_context_tab()

    # 定义销毁的方法
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
