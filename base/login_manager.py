import requests
import json
from common.logger import logger

class LoginManager:
    """登录态管理类，管理B端与C端的登录态"""
    
    def __init__(self):
        self.b_token = ""
        self.c_token = ""
        self.b_cookies = {}
        self.c_cookies = {}
    
    def login_b(self, username, password):
        """B端登录"""
        try:
            # 这里需要根据实际的B端登录接口进行修改
            login_url = "https://haha.xiaoetong.com/api/b/login"
            data = {
                "username": username,
                "password": password
            }
            response = requests.post(login_url, json=data)
            if response.status_code == 200:
                resp_json = response.json()
                if resp_json.get("code") == 0:
                    self.b_token = resp_json.get("data", {}).get("token", "")
                    self.b_cookies = response.cookies.get_dict()
                    logger.info("B端登录成功")
                    return True
            logger.error(f"B端登录失败: {response.text}")
            return False
        except Exception as e:
            logger.error(f"B端登录出错: {str(e)}")
            return False
    
    def login_c(self, phone, code):
        """C端登录"""
        try:
            # 这里需要根据实际的C端登录接口进行修改
            login_url = "https://haha.xiaoetong.com/api/c/login"
            data = {
                "phone": phone,
                "code": code
            }
            response = requests.post(login_url, json=data)
            if response.status_code == 200:
                resp_json = response.json()
                if resp_json.get("code") == 0:
                    self.c_token = resp_json.get("data", {}).get("token", "")
                    self.c_cookies = response.cookies.get_dict()
                    logger.info("C端登录成功")
                    return True
            logger.error(f"C端登录失败: {response.text}")
            return False
        except Exception as e:
            logger.error(f"C端登录出错: {str(e)}")
            return False
    
    def get_b_token(self):
        """获取B端token"""
        return self.b_token
    
    def get_c_token(self):
        """获取C端token"""
        return self.c_token
    
    def get_b_cookies(self):
        """获取B端cookies"""
        return self.b_cookies
    
    def get_c_cookies(self):
        """获取C端cookies"""
        return self.c_cookies
    
    def set_b_token(self, token):
        """设置B端token"""
        self.b_token = token
    
    def set_c_token(self, token):
        """设置C端token"""
        self.c_token = token
    
    def set_b_cookies(self, cookies):
        """设置B端cookies"""
        self.b_cookies = cookies
    
    def set_c_cookies(self, cookies):
        """设置C端cookies"""
        self.c_cookies = cookies

# 创建单例实例
login_manager = LoginManager()
