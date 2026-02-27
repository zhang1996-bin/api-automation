import allure
from base.base_config import BaseConfig
from api.order_list_api import OrderListApi
from hamcrest import assert_that, is_, is_not, greater_than_or_equal_to

@allure.feature("订单管理")
class TestOrderList:
    config = BaseConfig()
    
    @allure.story("获取订单列表")
    @allure.title("测试获取订单列表接口")
    def test_order_list(self):
        with allure.step("准备请求参数"):
            order_api = OrderListApi()
            order_api.data = {
                "bizData[page_index]": 1,
                "bizData[page_size]": 10,
                "bizData[purchase_name]": "",
                "bizData[state]": 2,
                "bizData[create_start]": "",
                "bizData[create_end]": "",
                "bizData[scroll_key]": "",
                "bizData[scroll_total]": 0,
                "bizData[app_id]": "appxz3zrnfn4438",
                "bizData[is_search_total]": 1
            }
        
        with allure.step("发送POST请求"):
            resp = order_api.post()
        
        with allure.step("验证响应"):
            assert_that(resp.status_code, is_(200))
            resp_json = resp.json()
            assert_that(resp_json.get("code"), is_(0))
            assert_that(resp_json.get("msg"), is_("success"))
            assert_that(resp_json.get("data"), is_not(None))
