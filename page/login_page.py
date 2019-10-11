from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Login_Page(BaseAction):
    #已有账号去登陆
    username = By.ID,"com.yunmall.lc:id/logon_account_textview"
    pwd = By.ID,"com.yunmall.lc:id/logon_password_textview"
    login_btn = By.ID,"com.yunmall.lc:id/logon_button"

    def login_upc(self,username,password):
        self.input(self.username,username)
        self.input(self.pwd,password)
        self.click(self.login_btn)