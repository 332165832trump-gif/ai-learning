import os

path = input("请输入文件夹路径: ")

images_folder = os.path.join(path, "images")
docs_folder = os.path.join(path, "docs")
code_folder = os.path.join(path, "code")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(code_folder, exist_ok=True)

files = os.listdir(path)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        print(file + " → images")
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        print(file + " → docs")
    elif file.endswith(".py"):
        print(file + " → code")
    else:
        print(file + " → 跳过")
