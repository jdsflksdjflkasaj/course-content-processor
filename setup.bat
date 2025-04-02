@echo off
echo 正在设置课程处理环境...

:: 创建虚拟环境
python -m venv venv
if errorlevel 1 (
    echo 创建虚拟环境失败！
    pause
    exit /b 1
)

:: 激活虚拟环境
call venv\Scripts\activate
if errorlevel 1 (
    echo 激活虚拟环境失败！
    pause
    exit /b 1
)

:: 安装依赖
pip install -r requirements.txt
if errorlevel 1 (
    echo 安装依赖失败！
    pause
    exit /b 1
)

:: 运行测试脚本
python scripts\test.py
if errorlevel 1 (
    echo 运行测试脚本失败！
    pause
    exit /b 1
)

echo 环境设置完成！
pause