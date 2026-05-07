# 005 - Python 文件系统与路径完整手册

> 面向零基础初学者。每个函数按「是什么→名字含义→为什么要学→写法→参数→返回值→项目例子→常见错误→Debug→怎么记住」组织。

---

## 文件系统是什么

### 用图书馆类比

文件系统 = 操作系统管理硬盘的**目录索引**。就像图书馆的卡片索引——书在书架上不动，卡片告诉你每本书在哪。

| 操作 | 图书馆类比 | Python 函数 |
|------|-----------|-------------|
| 看一个架子上有什么书 | 翻卡片 | `os.listdir()` |
| 新增一个书架 | 加新卡片 | `os.makedirs()` |
| 把书移到另一个书架 | 改卡片上的位置 | `os.rename()` |
| 查看自己在哪个区域 | 看地图 | `os.getcwd()` |

**本质**：Python 通过 `os` 模块读写操作系统维护的这张"卡片索引"。你的程序真的在操作电脑里的文件——不是沙箱模拟。

---

## 路径（path）是什么

### 定义
路径是文件在硬盘上的**地址**。就像每个人有一个家庭住址，每个文件有一个路径地址。

### 绝对路径
从磁盘根目录开始的完整地址。**不依赖当前工作目录**。

```
C:/ai-work/oc-test/notes.md
C:/Users/16068/Desktop/photo.jpg
```

### 相对路径
相对于"当前工作目录"的地址。**依赖程序站在哪里**。

```
notes.md              # 当前目录下的文件
../other/file.txt     # 上一级目录下的文件
./images/photo.jpg    # 当前目录下 images 子文件夹里的文件
```

- `.` = 当前目录
- `..` = 上一级目录

### Windows 路径转义问题

**问题代码**：
```python
path = "C:\Users\16068\桌面"
```

**报错**：
```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
```

**原因**：`\` 在 Python 字符串里是转义符开头。`\U` 被当成 Unicode 转义。

**三种正确写法**：
```python
path = "C:/Users/16068/桌面"          # 方法 1：正斜杠（最推荐）
path = "C:\\Users\\16068\\桌面"       # 方法 2：双反斜杠
path = r"C:\Users\16068\桌面"         # 方法 3：原始字符串
```

---

## `os.getcwd()` — 获取当前工作目录

### 是什么
返回程序当前的"站立位置"（Current Working Directory）。

### 名字含义
**get**cwd = **get** **C**urrent **W**orking **D**irectory。

### 基本写法
```python
import os
print(os.getcwd())    # → C:\ai-work\oc-test
```

### 返回值
一个字符串，表示当前工作目录的绝对路径。

### 为什么重要
- 相对路径从"当前工作目录"开始推算
- `notepad notes.md` 能打开当前目录的文件，就是因为相对路径基于当前工作目录
- 如果 `cd` 换了文件夹，`os.getcwd()` 的值也变了

### 常见错误
依赖相对路径 + 在错误文件夹运行程序 → 找不到文件。

**解决方案**：程序里用 `input()` 让用户指定绝对路径，或代码里写死绝对路径。

### 怎么记住
`getcwd` = "我在哪？" 就像手机地图的"当前位置"。

---

## `os.listdir(path)` — 列出文件夹内容

### 是什么
读取指定文件夹里的内容，返回文件名列表。

### 名字含义
**list** **dir** = **list** **dir**ectory（列出目录）。

### 基本写法
```python
files = os.listdir("C:/test")
print(files)
# → ['a.jpg', 'b.pdf', 'c.py', 'subfolder']
```

### 参数
- `path`：文件夹路径（字符串）。`"."` 表示当前目录，`".."` 表示上一级。

### 返回值
一个**列表**。每个元素是**文件名（含扩展名）**，**不是完整路径**。可能包含子文件夹名。

### 在我们项目里的例子
```python
path = input("请输入文件夹路径: ")
files = os.listdir(path)
for file in files:
    print(file)
```

### 常见错误

| 错误 | 原因 |
|------|------|
| `FileNotFoundError` | 路径不存在 |
| 把文件夹当成文件处理 | `os.listdir` 返回的列表包含子文件夹名 |
| 以为返回完整路径 | 只返回 `"a.jpg"`，不是 `"C:/test/a.jpg"` |

### Debug 方法
```python
print("路径:", path)
print("文件列表:", files)
```

### 怎么记住
`listdir` = 拉开一个抽屉，看里面有什么。但只看到**名字**，看不到完整地址。

---

## `os.path.join(a, b, ...)` — 安全拼接路径

### 是什么
把多个路径段安全地拼成完整路径。

### 名字含义
**path.join** = **join**（拼接）**path**（路径）。

### 基本写法
```python
os.path.join("C:/test", "images", "photo.jpg")
# → "C:/test/images/photo.jpg"
```

### 参数
任意多个字符串，每个是一段路径。

### 返回值
拼接后的完整路径字符串。

### 为什么不用字符串硬拼

```python
# 不好的写法 ❌
new_path = path + "/images/" + file

# 三个隐患：
# 1. \ 是 Python 转义符
# 2. Windows 用 \，Linux 用 /，硬写死换平台就炸
# 3. path 末尾可能有 /，拼出双斜杠 "test//images/photo.jpg"
```

**`os.path.join` 的本质**：它是"懂平台规则的路径拼接器"。你把积木块扔给它，它保证拼出合法路径。

### 在我们项目里的例子
```python
images_folder = os.path.join(path, "images")       # 目标文件夹路径
old_path = os.path.join(path, file)                # 文件当前地址
new_path = os.path.join(images_folder, file)       # 文件目标地址
```

### 关键认知：四个变量的区别

| 变量 | 含义 | 例子 |
|------|------|------|
| `path` | 用户输入的文件夹 | `"C:/test"` |
| `file` | 文件名（只有名字） | `"photo.jpg"` |
| `old_path` | 文件当前完整地址 | `"C:/test/photo.jpg"` |
| `new_path` | 文件搬家后的地址 | `"C:/test/images/photo.jpg"` |

### 怎么记住
`os.path.join` = 拼地址积木。把好几段扔给它，它帮你拼出完整路径。

---

## `os.makedirs(path, exist_ok=False)` — 创建文件夹

### 是什么
创建文件夹。`s` 表示可以一次性创建多层（如 `a/b/c`）。

### 名字含义
**make** **dir**s = **make** **dir**ectories（创建目录们）。

### 基本写法
```python
os.makedirs("C:/test/images", exist_ok=True)
```

### 参数
- `path`：要创建的文件夹路径
- `exist_ok=True`：如果文件夹已存在，**安静跳过**，不报错

### `exist_ok=True` 为什么重要

```python
# 第一次运行 ✅
os.makedirs("C:/test/images")   # 创建成功

# 第二次运行 ❌
os.makedirs("C:/test/images")   # FileExistsError!
```

加了 `exist_ok=True`，第二次也不会报错。这叫**幂等操作**（重复做同样的事，结果一样）。

### `mkdir()` vs `makedirs()`

| 函数 | 行为 |
|------|------|
| `os.mkdir("a")` | 只建一层。`a/b` 时如果 `a` 不存在 → 报错 |
| `os.makedirs("a/b/c")` | 自动补全中间层。`a` 不存在 → 先建 `a`，再建 `b`，再建 `c` |

**建议**：用 `makedirs` 更稳。

### 为什么放循环外面

创建文件夹只需做一次。放进 `for` 循环里每判断一个文件就建一次 → 浪费性能。

### 怎么记住
`makedirs` = 创建文件夹。`exist_ok=True` = 已经有了也没事。**放循环外面。**

---

## `os.rename(old, new)` — 移动/重命名文件

### 是什么
修改文件的路径记录。既可以重命名，也可以移动文件。

### 名字含义
**rename** = 重命名。但实际上它也能用来移动文件（因为移动 = 改路径 = 改"文件住址"）。

### 基本写法
```python
os.rename(old_path, new_path)
```

### 参数
- `old_path`：文件**当前的完整路径**（起点）
- `new_path`：文件**要去哪的完整路径**（终点）

### 本质
`os.rename` 在操作系统层面修改文件的路径记录。**文件数据在硬盘上没动**，只是"地址变了"。

### 为什么必须提供完整路径

```python
# 错误 ❌ 只有文件名，操作系统不知道这个文件在哪
os.rename("a.jpg", "images/a.jpg")

# 正确 ✅ 两个都是完整路径
os.rename("C:/test/a.jpg", "C:/test/images/a.jpg")
```

**搬家类比**：去派出所改户口地址，你要说"从 A 小区 3 栋 201 改到 B 小区 5 栋 302"。不能说"把小明搬到 B 小区"——派出所不知道小明现在住哪。

### 为什么移动后 `os.listdir(path)` 会变化

`os.listdir` 读的是文件夹的目录索引。`os.rename` 把文件移走后，原文件夹的目录条目消失。

### 为什么危险

- `os.rename` 是真的改操作系统层面的东西
- 如果 `new_path` 算错 → 文件失踪
- 批量 rename 没有 Ctrl+Z

**黄金法则**：先 `print(old_path + " → " + new_path)` 验证，再 `os.rename`。

### dry run（模拟执行）

```python
dry_run = True    # 开关：True = 模拟，False = 真正执行

if dry_run:
    print("将要移动: " + old_path + " → " + new_path)
else:
    os.rename(old_path, new_path)
```

### 常见错误

| 错误 | 原因 | Debug |
|------|------|------|
| `FileNotFoundError` | `old_path` 不存在 | `print(old_path)` |
| `PermissionError` | 文件被占用/无权限 | 关掉 Excel/Word |
| `FileExistsError` | `new_path` 已有同名 | 检查目标文件夹 |

### 怎么记住
`os.rename` = 改户口地址。两个参数：旧地址、新地址。都必须完整。**先 print，再 rename。**

---

## `os.path.isdir(path)` — 判断是不是文件夹

### 是什么
判断给定路径是不是一个文件夹（目录）。

### 名字含义
**is** **dir** = 是目录吗？

### 基本写法
```python
os.path.isdir("C:/test/images")    # → True（存在且是文件夹）
os.path.isdir("C:/test/a.jpg")     # → False（是文件）
os.path.isdir("C:/notexist")       # → False（不存在）
```

### 在我们项目的潜在用法
`os.listdir` 可能返回文件夹名（如 `images`、`docs`）。如果对文件夹执行 `os.rename`，后果不可预期。用 `isdir` 先过滤：

```python
for file in files:
    full_path = os.path.join(path, file)
    if os.path.isdir(full_path):
        continue     # 跳过文件夹
    # 对文件做分类...
```

### 怎么记住
`isdir` = 问 Python："这个路径是文件夹吗？"

---

## `os.path.exists(path)` — 判断路径是否存在

### 是什么
判断给定路径（文件或文件夹）是否存在。

### 名字含义
**exists** = 存在。

### 基本写法
```python
os.path.exists("C:/test/a.jpg")     # → True 或 False
```

### 什么时候用
- 在创建文件前检查是否重名
- 在 `os.rename` 前检查目标是否已有同名文件
- 检查用户输入的路径是否有效

### 怎么记住
`exists` = "这个东西存在吗？"

---

## Debug 方法总汇

路径类问题最高效的 Debug 方法——**增加 print**：

```python
print("用户输入的路径:", path)
print("当前文件:", file)
print("旧地址 (old_path):", old_path)
print("新地址 (new_path):", new_path)
print("目标文件夹:", images_folder)
```

**记住**：80% 的文件操作 bug 是路径写错了。不要猜，print 出来看。

---

## 记忆口诀

> **`listdir` = 看抽屉里有什么（只有名字）。**
> **`os.path.join` = 拼地址积木（安全拼接）。**
> **`makedirs` = 建文件夹（exist_ok=True 防重复）。**
> **`os.rename` = 改户口地址（先 print 再执行）。**
> **`getcwd` = 我在哪。**
> **路径 = 文件的住址。file 只是人名，old_path 才是完整住址。**

---

## 复习问题

1. `os.listdir()` 返回的是完整路径还是文件名？
2. `os.path.join("C:/test", "images", "a.jpg")` 的结果是什么？
3. `os.makedirs` 里的 `exist_ok=True` 有什么用？不加会怎样？
4. `mkdir` 和 `makedirs` 有什么区别？
5. `os.rename` 为什么需要两个完整路径？只给文件名行不行？
6. 什么是 dry run？为什么文件移动前要做 dry run？
7. `FileNotFoundError`、`PermissionError`、`FileExistsError` 分别是什么原因？
8. `os.path.isdir` 在文件分类器项目里有什么用？
9. 绝对路径和相对路径有什么区别？哪个更安全？
10. Windows 路径 `"C:\Users"` 为什么会报 SyntaxError？
