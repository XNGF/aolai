from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class HomePage(BaseAction):
    # 我
    me_button = By.ID,"com.yunmall.lc:id/tab_me"

    def click_me(self):
        self.click(self.me_button)

    def login_if_not(self,page):
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        #没有登陆就去登陆
        page.register.go_register()

        page.login.login_upc()
