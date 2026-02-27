import requests

class BaseRequests:
    def __init__(self):
        self.session = requests.Session()
    
    def request(self, method, url, headers=None, params=None, data=None, json=None, cookies=None):
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                cookies=cookies,
                timeout=30
            )
            return response
        except Exception as e:
            print(f"请求出错: {str(e)}")
            raise
