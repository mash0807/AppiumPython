import logging
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import os

def exception_handle(fun):
    def magic(*args,**kwargs):
        _self:BasePage = args[0]
        try:
            result = fun(*args,**kwargs)
            #清空错误次数
            _self._error_count =0
            return result
        except Exception as e:
            #如果次数太多，就退出异常逻辑，直接报错
            if _self._error_count > _self._error_max:
                raise e
            #记录一直异常的次数
            _self._error_count += 1
            #对黑名单里的弹框进行处理
            for element in _self._black_list:
                logging.info(element)
                elements = _self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    #继续寻找原来的正常控件
                    return magic(*args,**kwargs)
            #如果黑名单里也没有，就报错
            logging.warning("black list no one found")
            raise e

class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver:WebDriver
    _black_list =[
        (By.ID,'tv_agree'),
        (By.ID,'image_cancel'),
        (By.XPATH,'//*[@text = "确定"]'),
        (By.XPATH,'//*[@text = "下次再说"]')
    ]
    _error_max = 10
    _error_count = 0
    _steps_yaml_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/test_steps"
    _params = {}

    def __init__(self,driver :WebDriver = None):
        self._driver = driver

    #todo:当有广告、评价等各种弹框出现时，需要进行异常流程处理
    @exception_handle
    def find(self,locator,value: str = None):
        #查找控件
        if isinstance(locator,tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator,value)


    #todo:当有广告、评价等各种弹框出现时，需要进行异常流程处理
    @exception_handle
    def get_text(self,locator,value: str = None):
        self.find(locator,value).text


    def text(self,key):
        return (By.XPATH,"//*[@text='%s']" % key)

    def find_by_text(self,key):
        return self.find(self.text(key))

    def steps(self,path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"],step["locator"])
                if "action" in step.keys():
                    if step["action"] == "find":
                        pass
                    elif step["action"] == "click":
                        element.click()
                    elif step["action"] == "text":
                        element.text
                    elif step["action"] == "attribute":
                        element.get_attribute(step["value"])
                    elif step["action"] in ["send","input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" %key,self._params[key])
                        element.send_keys(content)
