from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


# 定义测试类
class TestMisLogin:
    # 定义类级别的初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建业务方法所在的类的对象
        self.mis_login_proxy = MisLoginProxy()

    # 定义方法级别的初始化 恢复原点
    def setup_method(self):
        self.driver.get("http://ttmis.research.itcast.cn/")

    # 定义测试方法
    def test_mis_login(self):
        # 定义测试数据
        username = "testid"
        password = "testpwd123"
        # 调用业务方法
        self.mis_login_proxy.test_mis_login(username, password)
        # 断言
        assert is_element_exist(self.driver, "退出")

    # 定义类级别的销毁方法
    # 关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
