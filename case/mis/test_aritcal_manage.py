import pytest
import config
from page.mis.mis_aaritcal_page import MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestAritcalMana:
    #
    def setup_class(self):
        # 打开的浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建登录页面业务对象
        self.login_page = MisLoginProxy()
        # 创建首页类的对象
        self.home_page = MisHomePage()
        # 创建文章审核页面对象
        self.ad_page = MisAtcalProxy()

    def test_aduit_pass(self):
        # 定义测试数据
        ari_title = config.PUB_ARITCAL_TITLE
        print(ari_title)
        self.home_page.to_aaritcal_page()
        self.ad_page.test_aduit_pass(ari_title)
        assert is_element_exist(self.driver, "驳回")
