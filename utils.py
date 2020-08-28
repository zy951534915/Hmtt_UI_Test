import json
import time
import selenium.webdriver
import appium.webdriver

# 定义浏览器驱动的工具类-自定义
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtils:
    # 自媒体驱动对象私有属性
    __mp_driver = None
    # 后台管理系统
    __mis_driver = None
    # APP
    __app_driver = None
    # mp关闭浏览器驱动的开关
    __mp_key = True
    # 后台管理系统关闭驱动对象开关
    __mis_key = True

    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()  # 窗口最大化
            cls.__mp_driver.implicitly_wait(30)  # 隐式等待
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 自媒体-关闭浏览器驱动的方法
    @classmethod
    def quit_mp_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mp_driver is not None and cls.__mp_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mp_driver.quit()
            # 将__driver设置为空
            cls.__mp_driver = None

    # 定义类方法重新定义浏览器开关的默认值
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # 后台管理系统获取驱动对象得方法
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()  # 窗口最大化
            cls.__mis_driver.implicitly_wait(30)  # 隐式等待
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    # 定义类方法重新定义浏览器开关的默认值
    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_mis_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mp_driver is not None and cls.__mis_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mis_driver.quit()
            # 将__driver设置为空
            cls.__mis_driver = None

    # app系统获取驱动对象得方法
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            desired_caps['noReset'] = True
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.get_app_driver().implicitly_wait(30)
        return cls.__app_driver

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_app_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__app_driver is not None:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__app_driver.quit()
            # 将__driver设置为空
            cls.__app_driver = None


# 根据文本判断元素是否存在的公用方法
def is_element_exist(driver, text):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(text(),'{}')]".format(text)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        NoSuchElementException("找不到文本为{}的元素对象".format(text))
        return False

# 根据属性和属性值判断元素是否存在的公用方法
def is_element_by_attribute(driver, attr_name, attr_value):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(@{},'{}')]".format(attr_name, attr_value)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        NoSuchElementException("找不到属性为{}值为{}的元素对象".format(attr_name, attr_value))
        return False

# 频道选择的公用方法(web)
def check_channel_option(driver, channel_text, channel_name):
    """
    :param driver: 浏览器驱动对象
    :param channel_text:选择框元素对象
    :param channel_name:选项名称
    :return:
    """
    # 选择框的定位xpath表达式
    str_xpath = "//*[contains(@placeholder, '{}')]".format(channel_text)
    # 点击选择框
    driver.find_element_by_xpath(str_xpath).click()
    # 获取所有选项的频道名称
    channel_option = driver.find_elements_by_css_selector(".el-select-dropdown__wrap span")
    # 定义一个是否找到的标识 默认为False
    is_suc = False
    # 对获取的频道名称遍历
    for optin_element in channel_option:
        # 判断当前遍历的元素文本信息是否等于我们想选择的频道名称
        if optin_element.text == channel_name:
            # 如果相等 则点击 跳出
            optin_element.click()
            is_suc = True
            break
        # 如果不是 悬停当前的元素对象 并按 向下方向键
        else:
            ActionChains(driver).move_to_element(optin_element).send_keys(Keys.DOWN).perform()

    if is_suc is False:
        NoSuchElementException("can't find name is {} channel option".format(channel_name))


# 封装读取数据并组装成parameteriz所要求数据格式函数
def get_case_data(file_path):
    # 定义一个空列表
    test_data = []
    # 1.读取数据文件中的数据
    with open(file=file_path, encoding="utf-8")as f:
        str_dict = json.load(f)
        # 2.遍历所有的键值
        for i in str_dict.values():
            # 3.一次性获取键值所有键值,并且把返回的结果直接追加到空列表中
            test_data.append(list(i.values()))
            print(test_data)
    return test_data
