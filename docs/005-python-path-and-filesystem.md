# 005 - Python 路径与文件系统

## 1. 路径是什么

路径是文件在电脑硬盘上的**地址**。

就像每个人有一个家庭住址，每个文件在硬盘上也有一个唯一的路径地址。Python 通过这个地址找到文件、移动文件、删除文件。

## 2. Windows 路径为什么容易出错

你在代码里写了：

```python
path = "C:\Users\16068\桌面"
```

Python 报错：

```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
```

**原因**：反斜杠 `\` 在 Python 字符串里是**转义字符的开头**。

- `\n` → 换行
- `\t` → Tab
- `\U` → Python 以为你要写 Unicode 转义，但后面不是合法内容 → 崩溃

**三种正确写法**：

```python
# 方法 1：用正斜杠（最推荐）
path = "C:/Users/16068/桌面"

# 方法 2：双反斜杠
path = "C:\\Users\\16068\\桌面"

# 方法 3：原始字符串（前面加 r）
path = r"C:\Users\16068\桌面"
```

**最佳实践**：Python 代码里永远用 `/` 写路径。用户通过 `input()` 输入的路径天然安全，不会触发转义。

## 3. `os.listdir()` — 读取文件夹内容

```python
files = os.listdir("C:/test")
# 返回：['a.jpg', 'b.pdf', 'c.py']
```

- **做什么**：读取文件夹里的文件列表。
- **返回**：一个列表，只包含文件名（如 `"a.jpg"`），**不包含完整路径**。
- **常见错误**：路径不存在 → `FileNotFoundError`。

## 4. `os.path.join()` — 安全拼接路径

```python
os.path.join("C:/test", "images", "photo.jpg")
# 结果："C:/test/images/photo.jpg"
```

- **本质**：它是"懂平台规则的路径拼接器"。你把积木块扔给它，它保证拼出合法路径。
- **为什么不用 `path + "/images/" + file`？**
  1. `\` 是 Python 转义符，可能被解释成特殊字符
  2. Windows 和 Linux 路径分隔符不同
  3. 如果 path 末尾已有 `/`，会拼出双斜杠

## 5. `file`、`path`、`old_path`、`new_path` 的区别

| 变量 | 含义 | 例子 |
|------|------|------|
| `path` | 用户输入的文件夹路径 | `"C:/test"` |
| `file` | 光秃秃的文件名 | `"a.jpg"` |
| `old_path` | 文件当前完整地址 | `"C:/test/a.jpg"` |
| `new_path` | 文件目标完整地址 | `"C:/test/images/a.jpg"` |

**关键**：`file` 只是名字，不带路径信息。要移动文件，必须有完整的起点和终点地址。

**搬家类比**：
- `file` = 小明（只有名字）
- `path` = 小区名
- `old_path` = `os.path.join(path, file)` → 小明现在住址
- `new_path` = `os.path.join(images_folder, file)` → 小明新住址
- `os.rename` = 去派出所改户口地址

## 6. `os.makedirs()` — 创建文件夹

```python
os.makedirs("C:/test/images", exist_ok=True)
```

- **`os.makedirs(路径)`**：创建文件夹。`s` 表示可以一次性创建多层（如 `a/b/c`）。
- **`exist_ok=True`**：如果文件夹已经存在，安静跳过，不报错。
  - 不加这个参数 → 第二次运行会报 `FileExistsError` 崩溃
  - 加了 → 重复运行完全安全
- **`os.mkdir()` vs `os.makedirs()`**：`mkdir` 只能建一层，`makedirs` 自动补全中间层。
- **为什么放循环外面**：创建文件夹只需做一次，放循环里每判断一个文件就建一次，浪费性能。

## 7. `os.rename()` — 移动文件

```python
os.rename(old_path, new_path)
```

- **本质**：在操作系统层面**修改文件的路径记录**。文件数据在硬盘上没动，只是"地址变了"。
- **不是"改名"**：虽然叫 rename，但你可以用它把文件从 `C:/test/a.jpg` 移到 `C:/test/images/a.jpg`，路径完全不同。
- **为什么移动后 `os.listdir(path)` 会变化**：`os.listdir` 读的是文件夹的目录索引。文件移走后，原文件夹的目录条目消失。

## 8. 绝对路径 vs 相对路径

**绝对路径**：从磁盘根目录开始的完整地址。
```
C:/ai-work/oc-test/notes.md
```
不依赖当前工作目录，在哪个文件夹运行结果都一样。

**相对路径**：相对于"当前工作目录"的地址。
```
notes.md               ← 当前目录下的文件
../other/file.txt      ← 上一级目录下的文件
```
依赖程序"站在哪里"，换文件夹运行结果可能不同。

**`os.getcwd()`**：获取程序当前的"站立位置"（Current Working Directory）。

**工程建议**：正式项目用绝对路径，行为可预测。或者用 `input()` 让用户指定绝对路径。

## 9. 文件系统是什么

文件系统是操作系统管理硬盘上文件的**目录索引**。

**类比**：图书馆卡片索引。书在书架上不动，卡片告诉你每本书在哪。Python 的 `os` 模块通过操作系统查询和修改这张"卡片索引"。

| 操作 | 本质 |
|------|------|
| `os.listdir()` | 读卡片索引 |
| `os.makedirs()` | 新增目录卡片 |
| `os.rename()` | 修改卡片上的位置 |
| `os.remove()` | 删除卡片 |

## 10. Debug 方法 — 路径类 bug 怎么查

```python
print("用户输入的路径:", path)
print("当前文件:", file)
print("旧地址:", old_path)
print("新地址:", new_path)
```

任何涉及路径的操作，**先 print 验证，再执行**。这是工程师的金科玉律。

## 11. 三种常见路径错误

| 错误 | 原因 | Debug |
|------|------|------|
| `FileNotFoundError` | `old_path` 不存在 | `print(old_path)` |
| `PermissionError` | 文件被占用/无权限 | 关掉占用程序 |
| `FileExistsError` | `new_path` 已有同名 | 检查目标文件夹 |

## 12. 记忆口诀

> **路径 = 文件在硬盘上的地址。**
> **`os.path.join` = 安全拼地址。**
> **`file` 只有名字，`old_path` 才是完整地址。**
> **`os.rename` = 改户口地址，不是搬家具。**
