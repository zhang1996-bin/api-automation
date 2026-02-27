from base.base_api import BaseApi
from base.base_config import BaseConfig
from base.base_requests import BaseRequests
from base.login_manager import login_manager
from common.logger import logger

class OrderListState3Api(BaseApi):
    def __init__(self, login_type="c"):
        super().__init__()
        self.config = BaseConfig()
        self.requests = BaseRequests()
        self.url = "https://haha.xiaoetong.com/xe.ogw.c_order_list/1.0.0"
        self.method = "POST"
        self.login_type = login_type  # 'b' for B端, 'c' for C端
        
    def _set_headers(self):
        """设置请求头，包含登录态"""
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://haha.xiaoetong.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://haha.xiaoetong.com/p/t/v1/ecommerce/h5_order/order/order_list?order_state=3",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1"
        }
        
        # 根据登录类型设置token
        if self.login_type == "b":
            token = login_manager.get_b_token()
        else:
            token = login_manager.get_c_token()
        
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
    
    def _get_cookies(self):
        """获取登录态cookies"""
        if self.login_type == "b":
            return login_manager.get_b_cookies()
        else:
            return login_manager.get_c_cookies()
    
    def post(self):
        # 设置请求头
        self._set_headers()
        
        # 获取cookies
        cookies = self._get_cookies()
        
        logger.info(f"请求URL: {self.url}")
        logger.info(f"请求方法: {self.method}")
        logger.info(f"请求头: {self.headers}")
        logger.info(f"请求体: {self.data}")
        logger.info(f"请求cookies: {cookies}")
        
        response = self.requests.request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            json=self.data,
            cookies=cookies
        )
        
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应内容: {response.text}")
        
        return response
    
    def get_order_id(self, response):
        """从响应中提取订单号"""
        try:
            resp_json = response.json()
            if resp_json.get("code") == 0:
                order_list = resp_json.get("data", {}).get("order_list", [])
                if order_list:
                    # 假设订单号在order_id字段中
                    order_id = order_list[0].get("order_id")
                    logger.info(f"提取到订单号: {order_id}")
                    return order_id
            logger.warning("未提取到订单号")
            return None
        except Exception as e:
            logger.error(f"提取订单号时出错: {str(e)}")
            return None
