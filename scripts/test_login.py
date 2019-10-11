import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        #重置             不充值么  不 --> 充值
        self.driver = init_driver(no_reset=False)

        # self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("login_data.yaml","test_login"))
    def test_login(self,args):
        #yaml数据
        username = args["username"]
        password  =args["password"]
        toast = args["toast"]
        #脚本流程
        self.page.home.click_me()
        self.page.register.go_register()
        self.page.login.login_upc(username,password)
        #toast
        if toast is None:
            assert self.page.me.get_nick_name_text() == username,"登录后的用户名和输入的用户民不一致"
        else:
            assert self.page.login.is_toast_exist(toast)

