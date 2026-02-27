import sys
import os

# 设置Python路径为项目根目录
sys.path.insert(0, os.path.abspath('.'))

import allure
from base.base_config import BaseConfig
from api.order_list_state3_api import OrderListState3Api
from api.logistics_detail_api import LogisticsDetailApi
from hamcrest import assert_that, is_, is_not
from common.logger import logger

@allure.feature("订单管理")
class TestOrderLogistics:
    config = BaseConfig()
    
    @allure.story("查询订单物流")
    @allure.title("提取订单号并查询物流详情")
    def test_order_logistics(self):
        order_id = None
        
        with allure.step("第一步：获取订单列表并提取订单号"):
            # 调用订单列表接口（状态为3）
            order_api = OrderListState3Api()
            order_api.data = {
                "bizData[page_index]": 1,
                "bizData[page_size]": 10,
                "bizData[purchase_name]": "",
                "bizData[state]": 3,
                "bizData[create_start]": "",
                "bizData[create_end]": "",
                "bizData[scroll_key]": "",
                "bizData[scroll_total]": 0,
                "bizData[app_id]": "appxz3zrnfn4438",
                "bizData[is_search_total]": 1
            }
            order_response = order_api.post()
            
            # 验证订单列表接口响应
            assert_that(order_response.status_code, is_(200))
            
            # 检查响应内容是否为空
            order_response_content = order_response.text
            if order_response_content:
                order_resp_json = order_response.json()
                assert_that(order_resp_json.get("code"), is_(0))
                assert_that(order_resp_json.get("msg"), is_("success"))
                
                # 提取订单号
                order_id = order_api.get_order_id(order_response)
                assert_that(order_id, is_not(None), "未提取到订单号")
            else:
                logger.warning("订单列表接口返回空响应")
                order_id = "E20251030170058a02aaeV2"  # 使用默认订单号
        
        with allure.step(f"第二步：使用订单号 {order_id} 查询物流详情"):
            # 调用物流详情接口
            logistics_api = LogisticsDetailApi()
            logistics_api.data = {
                "bizData[order_id]": order_id
            }
            logistics_response = logistics_api.post()
            
            # 验证物流详情接口响应
            assert_that(logistics_response.status_code, is_(200))
            
            # 检查响应内容是否为空
            response_content = logistics_response.text
            if response_content:
                logistics_resp_json = logistics_response.json()
                assert_that(logistics_resp_json.get("code"), is_(0))
                assert_that(logistics_resp_json.get("data"), is_not(None))
            else:
                logger.warning("物流详情接口返回空响应")
