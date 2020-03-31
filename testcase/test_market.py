from page.app import App


class TestMarket:
    def setup(self):
        self.market = App().start().goto_main().goto_market()

    def test_market_select(self):
        self.market.market_search().search('JD').add_select()
        self.market.search_backto_market()