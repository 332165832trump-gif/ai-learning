# 006 - 文件自动分类器项目完整复盘

> 按照真实学习顺序，从第一行代码到完整可运行项目。

---

## 项目目标

自动把一个文件夹里的文件按类型（图片/文档/代码）移动到对应子文件夹。

```
photo.jpg  →  images/
report.pdf →  docs/
main.py    →  code/
music.mp3  →  跳过（留在原地）
```

## 为什么这个项目适合初学者

- 20 行代码就能跑
- 没有外部依赖（纯 Python 自带模块）
- 结果直观（打开文件夹能看到文件被分类）
- 训练的是编程最核心的思维

## 为什么对自动化和量化有帮助

**文件分类器的底层思维**：

```
读取数据 → 遍历数据 → 判断条件 → 执行动作
```

**量化策略的底层思维**：

```
读取行情 → 遍历股票 → 判断信号 → 记录/提醒/回测/交易
```

**思维一样，数据源不同而已。**

---

## 完整迭代过程

### 第 1 步：读取文件夹（2 行新代码）

```python
import os
path = input("请输入文件夹路径: ")
files = os.listdir(path)
print(files)
```

**学的**：`import os`、`input()`、`os.listdir()`。知道了"路径"和"文件名"的区别。

### 第 2 步：用 for 循环逐个打印（1 行新代码）

```python
for file in files:
    print(file)
```

**学的**：`for` 循环遍历列表。缩进是语法，不是美观。

### 第 3 步：用 if/elif/else + endswith 判断类型（6 行新代码）

```python
for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        print(file + " → 图片")
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        print(file + " → 文档")
    elif file.endswith(".py"):
        print(file + " → 代码")
    else:
        print(file + " → 其他")
```

**学的**：`endswith()`、`if/elif/else` 排队判断、`or` 逻辑或。注意 `elif` 不是 `else if`。

### 第 4 步：用 os.path.join 拼路径 + os.makedirs 建文件夹（6 行新代码）

```python
images_folder = os.path.join(path, "images")
docs_folder = os.path.join(path, "docs")
code_folder = os.path.join(path, "code")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(code_folder, exist_ok=True)
```

**学的**：`os.path.join` 安全拼路径（不用字符串硬拼）、`os.makedirs` 创建文件夹、`exist_ok=True` 防止重复创建。

### 第 5 步：构造 old_path 和 new_path，先 print 验证（3 行新代码）

```python
old_path = os.path.join(path, file)
new_path = os.path.join(images_folder, file)
print(old_path + " → " + new_path)
```

**学的**：`file` 只是文件名，不是完整路径。搬家需要起点和终点两个完整地址。

**关键认知表**：

| 变量 | 含义 | 例子 |
|------|------|------|
| `path` | 用户输入的文件夹 | `"C:/test"` |
| `file` | 文件名（只有名字） | `"photo.jpg"` |
| `old_path` | 文件当前完整地址 | `"C:/test/photo.jpg"` |
| `new_path` | 文件搬家后的地址 | `"C:/test/images/photo.jpg"` |

### 第 6 步：os.rename 真正移动（1 行新代码）

```python
os.rename(old_path, new_path)
```

**学的**：先 `print` 验证，再 `os.rename` 执行。dry run 思维。

---

## 最终完整代码

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
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(images_folder, file)
        print("移动: " + old_path + " -> " + new_path)
        os.rename(old_path, new_path)
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(docs_folder, file)
        print("移动: " + old_path + " -> " + new_path)
        os.rename(old_path, new_path)
    elif file.endswith(".py"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(code_folder, file)
        print("移动: " + old_path + " -> " + new_path)
        os.rename(old_path, new_path)
    else:
        print(file + " -> 跳过")
```

---

## 常见错误

| 错误 | 原因 | 怎么修 |
|------|------|--------|
| `FileNotFoundError` | `old_path` 不存在 | `print(old_path)` 检查路径 |
| `PermissionError` | 文件被打开占用 | 关掉 Excel/Word/编辑器 |
| `FileExistsError` | 目标已存在同名文件 | 检查目标文件夹 |
| 把文件夹也移动了 | `os.listdir` 返回文件夹名 | 加 `os.path.isdir()` 过滤 |
| 重复运行丢文件 | 文件已被移走 | `exist_ok=True` 防重复创建 |

---

## Debug 流程

出问题时按这个步骤排查：

```python
# 1. 在 rename 之前加这些 print
print("用户输入路径:", path)
print("当前文件:", file)
print("旧地址:", old_path)
print("新地址:", new_path)

# 2. 检查路径是否存在
print("旧地址存在吗?", os.path.exists(old_path))

# 3. 先用 dry run 验证
# 把 os.rename 注释掉，先看 print 输出对不对
```

---

## 项目改进方向

| 改进 | 做法 |
|------|------|
| 支持更多扩展名 | 加上 `.jpeg`、`.doc`、`.html` 等 |
| 不区分大小写 | `file.lower().endswith(...)` |
| 跳过文件夹 | `if os.path.isdir(old_path): continue` |
| 处理重名 | 如果目标已存在，加 `_1` 后缀 |
| dry run 开关 | 加一个变量控制是否真正移动 |
| 日志记录 | 把移动记录写入 log 文件 |

---

## 和量化的关系

```
文件分类器：for file in files      →  if 类型判断  →  os.rename
量化策略：  for stock in stocks    →  if 信号判断  →  记录/提醒/交易
```

今天你在 `for file in files` 里写 `if ... else ...`，未来你会在 `for stock in stocks` 里写同样的逻辑。**循环 + 判断 + 执行**，是自动化世界的通用语言。

---

## 复习问题

1. 文件分类器项目的核心代码涉及哪几个 Python 函数？
2. `old_path` 和 `new_path` 分别是什么？为什么都需要完整路径？
3. `os.makedirs` 里的 `exist_ok=True` 有什么用？
4. 什么是 dry run？为什么移动文件前要 dry run？
5. `FileNotFoundError` 在文件分类器里通常在什么情况下出现？
6. 文件分类器的底层思维和量化策略有什么共通之处？
