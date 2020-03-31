import yaml

from page.app import App
import pytest


class TestSearch:
    def setup(self):
        self.main = App().start().goto_main()

    def test_search(self):
        assert self.main.goto_search_page().search("阿里巴巴").get_price("BABA") > 100

    @pytest.mark.parametrize("key,stock_type,price",yaml.safe_load(open("D:/AppiumPython/test_data/search_data.yaml")))
    def test_search_data(self,key,stock_type,price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) > price

    def test_select(self):
        assert "已添加" in self.main.goto_search_page().search("JD").add_select().get_msg()