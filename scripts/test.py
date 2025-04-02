import os
import sys

def main():
    print("测试脚本运行成功！")
    print(f"当前工作目录: {os.getcwd()}")
    print(f"Python 版本: {sys.version}")
    print("\n可用目录:")
    for dir_name in ['input', 'output', 'config', 'scripts', 'templates', 'docs', 'logs']:
        path = os.path.join(os.getcwd(), dir_name)
        exists = os.path.exists(path)
        print(f"- {dir_name}: {'存在' if exists else '不存在'}")

if __name__ == "__main__":
    main()