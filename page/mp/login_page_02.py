from selenium.webdriver.common.by import By
from base.mp_base.base_page import BasePage, BaseHandle


# mp自媒体登录页面类
class LoginPage(BasePage, BaseHandle):

    def __init__(self):  # 每个类属性 都是一个对象
        super().__init__()
        # 账号输入框
        self.username = self.find_elt((By.CSS_SELECTOR, "[placeholder*='手机号']"))
        # 验证码
        self.code = self.find_elt((By.CSS_SELECTOR, "[placeholder*='验证码']"))
        # 登录按钮
        self.login_btn = self.find_elt((By.CSS_SELECTOR, ".el-button--primary"))

    # 登录的方法
    def test_login(self, username, code):
        self.input_text(self.username, username)
        self.input_text(self.code, code)
        self.login_btn.click()
