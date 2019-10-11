from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):
    invit_edit_text = By.XPATH, "//input[@type='tel']"
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    def input_invite(self,text):
        self.input(self.invit_edit_text,text)

    def click_be_vip(self):
        self.click(self.be_vip_button)
