from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.market import Market
from page.profile import Profile
from page.search import Search
from appium.webdriver.common.mobileby import MobileBy

class Main(BasePage):

    def goto_search_page(self):
        self.steps(self._steps_yaml_path+"/main_search.yaml")
        return Search(self._driver)

    #进入行情页面
    def goto_market(self):
        self.find(By.XPATH, "//*[@text='行情']").click()
        return Market(self._driver)

    def goto_trade(self):
        pass

    #进入我的页面
    def goto_profile(self):
        self.find(By.XPATH,"//*[@text='我的']").click()
        return Profile(self._driver)


    def goto_message(self):
        pass