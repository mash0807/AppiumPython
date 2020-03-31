import time

from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.main import Main
from appium import webdriver

class App(BasePage):

    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["automationName"] = "uiautomator2"
            caps["deviceName"] = "192.168.237.101:5555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            #caps["noReset"] = True
            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(self._package,self._activity)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def goto_main(self) -> Main:
        def wait_load(driver):
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False
        WebDriverWait(self._driver,30).until(wait_load)
        time.sleep(5)
        return Main(self._driver)