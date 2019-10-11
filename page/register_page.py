from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Register_Page(BaseAction):
    #已有账号去登陆
    register_op = By.XPATH,"//*[@text='已有账号，去登录']"

    def go_register(self):
        self.click(self.register_op)