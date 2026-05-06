# 004 - Python 基础语法

## 1. `input()` 和 `print()` — 程序的嘴和耳朵

```python
name = input("请输入你的名字: ")    # 等待用户输入，返回字符串
print("Hello " + name)              # 输出拼接后的字符串
```

### `input()`

- **做什么**：等待用户从键盘输入文字，按回车后返回。
- **返回什么**：**永远是字符串**。即使用户输入 `25`，得到的是文字 `"25"`，不是数字。
- **常见错误**：`name = Input()` — Python 严格区分大小写，必须全小写 `input`。

### `print()`

- **做什么**：把内容输出到屏幕上。
- **`+` 拼接**：字符串之间用 `+` 拼接，数字之间用 `+` 做加法。不能混用。
- **空格**：`print()` 不会自动加空格，`"Hello "` 末尾的空格是手工加的。

## 2. `import os` — 把操作系统工具箱拿进来

```python
import os
```

- **`import`**：导入模块，"把这个工具箱拿进来"。
- **`os`**：Python 自带的操作系统工具模块，不用安装。
- **用的时候加前缀**：`os.listdir()`。光写 `listdir()` 会报 `NameError`。
- **类比**：`import` = 从仓库取一个工具箱，用里面的工具得说"工具箱名.工具名"。

## 3. 列表（list）— 装东西的容器

```python
files = os.listdir(".")   # "." = 当前目录
print(files)              # 输出：['classifier.py', 'main.py', '.git']
```

- **列表**：用 `[]` 包起来的一组东西，按顺序排列。
- **`os.listdir(path)`**：返回一个列表，包含该路径下所有文件和文件夹的名字。
- `.` = 当前目录，`..` = 上一级目录。
- **常见错误**：路径不存在 → `FileNotFoundError`。

## 4. `for` 循环 — 一个一个处理

```python
for file in files:
    print(file)
```

**执行过程**：

```
第1轮：file = "a.jpg"     → print("a.jpg")
第2轮：file = "b.pdf"     → print("b.pdf")
第3轮：file = "c.py"      → print("c.py")
列表走完，循环结束
```

- **`for`**：循环关键字
- **`file`**：你自己起的变量名，代表当前这轮取到的元素
- **`in files`**：从 `files` 列表里取
- **`:`**：冒号**必须写**，不写就 `SyntaxError`

## 5. `if` / `elif` / `else` — 让程序做判断

```python
if file.endswith(".jpg"):
    print("图片")
elif file.endswith(".pdf"):
    print("文档")
else:
    print("其他")
```

- **`if`**：如果条件成立，执行下面缩进的代码。
- **`elif`**：如果上面的条件不成立，再判断这个。注意是 `elif`，不是 `else if`。
- **`else`**：前面所有条件都不成立时执行。兜底。
- **排队判断**：从上到下，第一个满足的就执行，后面全部跳过。

### `endswith()` — 判断字符串结尾

```python
"photo.jpg".endswith(".jpg")   # True
"photo.png".endswith(".jpg")   # False
```

- **做什么**：判断字符串是否以括号里的内容结尾。
- **返回值**：`True`（是）或 `False`（不是）。
- **常见错误**：`file.endswith(".jpg" or ".png")` → 语法不报错但逻辑错误，只检查 `.jpg`。应该写 `file.endswith(".jpg") or file.endswith(".png")`。

### `or` — 逻辑"或"

- `a or b`：两边有一个是 `True`，整体就是 `True`。
- `file.endswith(".jpg") or file.endswith(".png")`：只要文件以 `.jpg` 或 `.png` 结尾，都算图片。

## 6. 缩进 — Python 最重要的语法规则

```python
for file in files:          # 第1层
    if file.endswith(".py"): # 第2层（属于for）
        print("代码")        # 第3层（属于if）
    else:                    # 第2层（属于for）
        print("非代码")      # 第3层（属于else）
print("循环结束")            # 第0层（不属于任何循环）
```

- **缩进 = 层级结构**：缩进越多，层级越深。
- **决定代码属于谁**：`if` 下面缩进的代码 = `if` 的小弟，条件成立才干活。不缩进的代码 = 自由人，每次都执行。
- **必须一致**：同一层级的代码缩进格数必须相同。4 个空格是 Python 约定。
- **常见错误**：`:` 结尾的行下面忘记缩进 → `IndentationError`。

**我的理解**：缩进就是"代码的身份证"，告诉 Python "我属于谁"。冒号下面缩进的代码听冒号的话，不缩进的代码谁也不听。
