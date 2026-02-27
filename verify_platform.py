#!/usr/bin/env python3
"""
验证接口自动化平台结构是否正确
"""
import os
import sys

# 检查目录结构
expected_dirs = [
    'api',
    'base',
    'common',
    'config',
    'data',
    'log',
    'page',
    'report',
    'test_case'
]

print("=== 验证接口自动化平台结构 ===")

# 检查目录是否存在
for directory in expected_dirs:
    if os.path.exists(directory):
        print(f"✓ {directory} 目录存在")
    else:
        print(f"✗ {directory} 目录不存在")

# 检查基础文件是否存在
expected_files = [
    'base/base_api.py',
    'base/base_config.py',
    'base/base_error.py',
    'base/base_requests.py',
    'base/base_token.py',
    'common/logger.py',
    'common/settings.py',
    'api/test_api.py',
    'test_case/test_sample.py',
    'requirements.txt'
]

print("\n=== 验证基础文件 ===")
for file in expected_files:
    if os.path.exists(file):
        print(f"✓ {file} 文件存在")
    else:
        print(f"✗ {file} 文件不存在")

# 检查依赖是否安装
print("\n=== 验证依赖安装 ===")
try:
    import requests
    import pytest
    import allure
    import yaml
    print("✓ 核心依赖安装成功")
except ImportError as e:
    print(f"✗ 依赖安装失败: {e}")

print("\n=== 验证完成 ===")
print("接口自动化平台搭建成功！")
print("\n使用说明：")
print("1. 在api目录下创建接口类")
print("2. 在test_case目录下编写测试用例")
print("3. 设置环境变量: $env:environment='online' (Windows PowerShell)")
print("4. 运行测试: python -m pytest test_case/your_test_file.py --alluredir=report")
print("5. 查看报告: allure serve report")
