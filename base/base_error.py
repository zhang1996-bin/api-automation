class BaseError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ApiError(BaseError):
    pass

class ConfigError(BaseError):
    pass
