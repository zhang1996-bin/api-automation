from base.base_api import BaseApi
from base.base_config import BaseConfig
from base.base_requests import BaseRequests
from common.logger import logger

class TestApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.config = BaseConfig()
        self.requests = BaseRequests()
        self.url = f"{self.config.base_url}/test"
        self.method = "GET"
    
    def get(self):
        logger.info(f"请求URL: {self.url}")
        logger.info(f"请求方法: {self.method}")
        logger.info(f"请求参数: {self.params}")
        
        response = self.requests.request(
            method=self.method,
            url=self.url,
            params=self.params,
            headers=self.headers
        )
        
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应内容: {response.text}")
        
        return response
