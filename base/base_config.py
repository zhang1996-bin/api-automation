import os

class BaseConfig:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseConfig, cls).__new__(cls)
            cls._instance._init_config()
        return cls._instance
    
    def _init_config(self):
        self.environment = os.environ.get('environment', 'online')
        # 可以根据环境加载不同的配置
        if self.environment == 'online':
            self.base_url = "https://api.example.com"
        elif self.environment == 'outer1':
            self.base_url = "https://api.outer1.example.com"
        else:
            self.base_url = "https://api.test.example.com"
