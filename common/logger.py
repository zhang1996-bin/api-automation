import logging
import os
from datetime import datetime

class Logger:
    def __init__(self):
        self.log_dir = "log"
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        
        self.log_file = os.path.join(self.log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
        
        self.logger = logging.getLogger("api_auto")
        self.logger.setLevel(logging.DEBUG)
        
        # 控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 文件输出
        file_handler = logging.FileHandler(self.log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        
        # 格式化
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        # 添加处理器
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)
    
    def get_logger(self):
        return self.logger

logger = Logger().get_logger()
