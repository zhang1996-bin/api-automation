import allure
from base.base_config import BaseConfig
from api.test_api import TestApi
from hamcrest import assert_that, is_in

@allure.feature("测试模块")
class TestSample:
    config = BaseConfig()
    
    @allure.story("测试接口")
    @allure.title("测试GET请求")
    def test_get_request(self):
        with allure.step("发送GET请求"):
            test_api = TestApi()
            test_api.params = {"key": "value"}
            resp = test_api.get()
        
        with allure.step("验证响应"):
            assert_that(resp.status_code, is_in((200, 201)))
