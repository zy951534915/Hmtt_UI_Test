import pytest

from utils import DriverUtils


@pytest.mark.run(order=199)
class TestBegin:
    def test_begin(self):
        # 关闭浏览器驱动的开关
        DriverUtils.change_mis_key(True)
        # 主动调用一次关闭浏览器驱动的方法
        DriverUtils.quit_mp_driver()