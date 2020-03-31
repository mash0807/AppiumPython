from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.search import Search


class Market(BasePage):
    def market_search(self):
        self.find(By.ID,'action_search').click()
        return Search(self._driver)

    def search_backto_market(self):
        self.find_click(By.ID,'action_close').click()