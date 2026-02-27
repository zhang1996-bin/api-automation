import allure
from base.login_manager import login_manager
from api.example_api_with_login import ExampleApiWithLogin
from hamcrest import assert_that, is_, is_not

@allure.feature("登录态管理")
class TestLoginManager:
    
    @allure.story("设置登录态")
    @allure.title("验证C端登录态")
    def test_set_c_login(self):
        with allure.step("验证登录态设置成功"):
            # 验证登录态是否已经从配置文件中初始化
            c_token = login_manager.get_c_token()
            c_cookies = login_manager.get_c_cookies()
            assert_that(c_token, is_not(""))
            assert_that(c_cookies, is_not({}))
            assert_that(c_cookies.get("app_id"), is_("appxz3zrnfn4438"))
    
    @allure.story("使用登录态")
    @allure.title("使用C端登录态调用接口")
    def test_use_c_login(self):
        with allure.step("创建带登录态的API实例"):
            api = ExampleApiWithLogin(login_type="c")
            api.data = {"key": "value"}
        
        with allure.step("调用接口"):
            # 这里会使用登录态管理模块中的C端登录态
            response = api.post()
            # 验证响应状态码
            assert_that(response.status_code, is_(200))
