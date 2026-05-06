import os

path = input("请输入文件夹路径: ")

files = os.listdir(path)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        print(file + " → 图片")
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        print(file + " → 文档")
    elif file.endswith(".py"):
        print(file + " → 代码")
    else:
        print(file + " → 其他")
