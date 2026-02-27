#!/usr/bin/env python3
"""
运行测试用例的脚本，确保正确的Python路径
"""
import sys
import os

# 设置Python路径为项目根目录
sys.path.insert(0, os.path.abspath('.'))

# 初始化登录态
from config.login_config import init_login_state
init_login_state()

# 导入并运行测试
import pytest

if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        # 运行指定的测试文件
        test_files = sys.argv[1:]
        pytest.main(["-s"] + test_files + ["--alluredir=report"])
    else:
        # 运行所有测试用例
        pytest.main(["-s", "test_case/", "--alluredir=report"])
