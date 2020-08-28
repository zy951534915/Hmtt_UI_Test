from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.mp_base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtils, check_channel_option


class PubAriPage(BasePage):
    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # iframe
        self.ari_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 内容
        self.ari_context = (By.CSS_SELECTOR, "body")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道选择框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 发表
        self.pub_bth = (By.XPATH, "//*[text()='发表']")

    # 找标题
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 找iframe
    def find_ari_iframe(self):
        return self.find_elt(self.ari_iframe)

    # 找内容
    def find_ari_context(self):
        return self.find_elt(self.ari_context)

    # 找封面
    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    # 找频道选择框
    def find_channel(self):
        return self.find_elt(self.channel)

    # 找发表按钮
    def find_pub_bth(self):
        return self.find_elt(self.pub_bth)


# 操作层
class PubAriHandle(BaseHandle):
    def __init__(self):
        self.pub_page = PubAriPage()
        self.driver = DriverUtils.get_mp_driver()

    # 标题输入
    def input_ari_title(self, title):
        self.input_text(self.pub_page.find_ari_title(), title)

    # 切换
    def switch_ari_iframe(self):
        self.driver.switch_to.frame(self.pub_page.find_ari_iframe())

    # 内容输入
    def input_ari_context(self, context):
        self.input_text(self.pub_page.find_ari_context(), context)
        self.driver.switch_to.default_content()

    # 封面点击
    def click_ari_cover(self):
        self.pub_page.find_ari_cover().click()

    # 下拉框点击
    def click_channel(self, channel_name):
        check_channel_option(self.driver, "请选择", channel_name)

    # 发表点击
    def click_pub_bth(self):
        self.pub_page.find_pub_bth().click()


# 业务层
class PubAriProxy:
    def __init__(self):
        self.pub_handle = PubAriHandle()

    # 跳转发布文章页面
    def to_pub_ari_tab(self, title, context, channel_name):
        # 输入标题
        self.pub_handle.input_ari_title(title)
        # 切换
        self.pub_handle.switch_ari_iframe()
        # 输入内容
        self.pub_handle.input_ari_context(context)
        # 点击封面
        self.pub_handle.click_ari_cover()
        # 点击下拉框
        self.pub_handle.click_channel(channel_name)
        # 点击发表
        self.pub_handle.click_pub_bth()
