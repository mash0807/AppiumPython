import string
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Search(BasePage):

    def search(self,key:string):
        #self.find(MobileBy.ID,"search_input_text").send_keys(key)
        #self.find(MobileBy.ID,"name").click()
        self._params = {}
        self._params["key"] = key
        self.steps(self._steps_yaml_path+"/search.yaml")
        return self

    def get_price(self,key:string) -> float:
        return float(self.find(MobileBy.ID,"current_price").text)

    def add_select(self):
        element = self.find_by_text("加自选")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_text("已添加")
        element.click()
        return self

    def get_msg(self):
        return self.get_text(By.ID,"followed_btn")