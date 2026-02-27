@echo off
chcp 65001 > nul
echo ========================
echo 🔧 激活虚拟环境并安装依赖
echo ========================
call .venv\Scripts\activate.bat
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install PyHamcrest -i https://pypi.tuna.tsinghua.edu.cn/simple

echo.
echo ========================
echo 🚀 执行测试用例
echo ========================
pytest --alluredir=./allure-results --clean-alluredir

echo.
echo ========================
echo 📊 生成并打开Allure报告
echo ========================
allure serve ./allure-results

pause