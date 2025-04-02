import os
import shutil

def run_test():
    print("\n=== 系统测试开始 ===\n")
    
    # 检查当前目录
    print(f"当前目录: {os.getcwd()}")
    
    # 检查必要文件夹
    print("\n检查必要文件夹:")
    folders = ['input', 'output', 'config', 'scripts', 'templates', 'docs', 'logs']
    all_folders_exist = True
    for folder in folders:
        exists = os.path.exists(folder)
        if not exists:
            all_folders_exist = False
        print(f"- {folder}: {'✓' if exists else '✗'}")
    
    # 检查输入文件
    print("\n检查输入文件:")
    input_file = os.path.join('input', 'test.txt')
    if os.path.exists(input_file):
        print("- 测试文件存在 ✓")
        with open(input_file, 'r') as f:
            content = f.read()
        print(f"- 文件内容: {content}")
    else:
        print("- 测试文件不存在 ✗")
    
    # 测试文件复制
    print("\n测试文件复制:")
    try:
        shutil.copy2(input_file, os.path.join('output', 'test_output.txt'))
        print("- 文件复制成功 ✓")
    except Exception as e:
        print(f"- 文件复制失败 ✗: {e}")
    
    print("\n=== 系统测试完成 ===\n")
    
if __name__ == "__main__":
    run_test()