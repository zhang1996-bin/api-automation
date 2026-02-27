class BaseToken:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseToken, cls).__new__(cls)
            cls._instance._init_token()
        return cls._instance
    
    def _init_token(self):
        self.token = ""
    
    def get_token(self):
        return self.token
    
    def set_token(self, token):
        self.token = token
