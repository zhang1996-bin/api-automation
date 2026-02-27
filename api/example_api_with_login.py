from base.base_api import BaseApi
from base.base_config import BaseConfig
from base.base_requests import BaseRequests
from base.login_manager import login_manager
from common.logger import logger

class ExampleApiWithLogin(BaseApi):
    def __init__(self, login_type="c"):
        super().__init__()
        self.config = BaseConfig()
        self.requests = BaseRequests()
        self.url = f"{self.config.base_url}/example"
        self.method = "POST"
        self.login_type = login_type  # 'b' for B端, 'c' for C端
        
    def _set_headers(self):
        """设置请求头，包含登录态"""
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
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
