# 006 - 文件自动分类器项目

## 1. 项目目标

自动把一个文件夹里的文件按类型（图片/文档/代码）移动到对应子文件夹。

```
photo.jpg  →  images/
report.pdf →  docs/
main.py    →  code/
music.mp3  →  跳过（留在原地）
```

## 2. 为什么这个项目重要

它训练的是**编程的底层思维**：

```
读取数据 → 遍历数据 → 判断条件 → 执行动作
```

这也是自动化系统和量化系统的核心逻辑。学会了文件分类器，以后做：
- 行情数据自动整理（同一条思维）
- 网页数据定时抓取（同一条思维）
- 财务文件批量处理（同一条思维）

**思维是可以迁移的**。

## 3. 项目迭代过程（按学习顺序）

### 第 1 步：读取文件夹

```python
import os
path = input("请输入文件夹路径: ")
files = os.listdir(path)
print(files)
```

**学的**：`os.listdir()` 返回文件名列表，但只是文件名，不带路径。

### 第 2 步：逐个打印文件

```python
for file in files:
    print(file)
```

**学的**：`for` 循环遍历列表。

### 第 3 步：判断文件类型

```python
for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file + " → 图片")
    elif file.endswith(".pdf"):
        print(file + " → 文档")
    elif file.endswith(".py"):
        print(file + " → 代码")
    else:
        print(file + " → 其他")
```

**学的**：`endswith()`、`if/elif/else`、`or`。

### 第 4 步：创建目标文件夹

```python
images_folder = os.path.join(path, "images")
os.makedirs(images_folder, exist_ok=True)
```

**学的**：`os.path.join()` 拼接路径、`os.makedirs()` 创建文件夹、`exist_ok=True` 防止重复创建报错。

### 第 5 步：构造完整路径

```python
old_path = os.path.join(path, file)          # 起点
new_path = os.path.join(images_folder, file) # 终点
print(old_path + " → " + new_path)
```

**学的**：`file` 只是文件名，`old_path` 才是完整路径。移动文件需要起点和终点两个完整地址。

### 第 6 步：真正移动文件

```python
os.rename(old_path, new_path)
```

**学的**：`os.rename()` 在操作系统层面修改文件路径记录。先 print 验证，再 rename 执行。

## 4. 最终完整代码

```python
import os

path = input("请输入文件夹路径: ")

# 构造目标文件夹路径
images_folder = os.path.join(path, "images")
docs_folder = os.path.join(path, "docs")
code_folder = os.path.join(path, "code")

# 创建文件夹（已有则跳过）
os.makedirs(images_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(code_folder, exist_ok=True)

# 遍历所有文件
files = os.listdir(path)

for file in files:
    # 图片
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(images_folder, file)
        print("移动: " + old_path + " → " + new_path)
        os.rename(old_path, new_path)

    # 文档
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(docs_folder, file)
        print("移动: " + old_path + " → " + new_path)
        os.rename(old_path, new_path)

    # 代码
    elif file.endswith(".py"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(code_folder, file)
        print("移动: " + old_path + " → " + new_path)
        os.rename(old_path, new_path)

    # 其他
    else:
        print(file + " → 跳过")
```

## 5. 常见错误

| 错误 | 原因 | 怎么修 |
|------|------|--------|
| `FileNotFoundError` | `old_path` 对应的文件不存在 | `print(old_path)` 检查路径 |
| `PermissionError` | 文件被其他程序占用 | 关掉 Excel/Word/编辑器 |
| `FileExistsError` | 目标已存在同名文件 | 检查目标文件夹 |
| 把文件夹也当文件处理了 | `os.listdir` 返回文件和文件夹 | 用 `os.path.isfile()` 过滤 |
| 重复运行丢文件 | 文件已被移走 | 用 `exist_ok=True` 防重复创建 |

## 6. 工程思维

### dry run（模拟执行）

在真正移动之前，先只打印不执行：

```python
if dry_run:
    print("将要移动: " + old_path + " → " + new_path)
else:
    os.rename(old_path, new_path)
```

### 先验证再批量

1. 创建测试文件夹（3-5 个文件）
2. 验证逻辑正确
3. 再对真实文件夹执行

### 危险操作清单

- `os.remove()` — 删除文件
- `os.rename()` 覆盖已有文件
- `shutil.rmtree()` — 递归删除整个文件夹
- 批量操作 — 10000 个文件改错没有 Ctrl+Z

### 黄金法则

> **任何会修改文件系统的操作，先 print 验证，再真正执行。**

## 7. 和量化的关系

文件分类器的本质是：

```
读取数据 → 遍历判断 → 执行动作
```

量化策略的本质也是：

```
读取行情/财报 → 判断信号 → 记录/提醒/回测/交易
```

今天写的 `for file in files: if ... else ...`，未来就是 `for stock in stocks: if signal ... else ...`。

**思维不变，数据源不同而已。**
