# 004 - Python 基础语法完整手册

> 面向零基础初学者。每个语法点按「是什么→为什么要学→怎么写→在项目里的例子→常见错误→Debug→怎么记住」组织。

---

## `import` / `import os` — 导入模块

### 是什么
把 Python 的"工具箱"拿进来用。

### 名字含义
**import** = 导入、引进。

### 为什么要学
Python 自带很多功能（数学、文件操作、网页请求），但不是自动加载的。你需要什么就 `import` 什么。

### 基本写法
```python
import os       # 导入操作系统工具箱
```

### 本质
`import os` 之后，你才能用 `os.listdir()`、`os.path.join()`。不 `import` 就写这些函数 → `NameError`。

### 常见错误
```python
os.listdir(".")     # 正确 ✅
listdir(".")        # 错误 ❌ NameError: name 'listdir' is not defined
```
**原因**：忘了写 `os.` 前缀。Python 需要通过 `os.` 知道你在用 `os` 模块里的函数。

### 怎么记住
`import` = 去仓库取工具箱。`os.` = 从工具箱里拿工具。

---

## `input()` — 获取用户输入

### 是什么
等待用户从键盘输入文字，按回车后返回。

### 名字含义
**input** = 输入。

### 基本写法
```python
name = input("请输入你的名字: ")
```

### 参数解释
- `"请输入你的名字: "`：提示语，显示在屏幕上引导用户
- 返回值：**永远是字符串**。用户输入 `25`，得到的是 `"25"`（文字），不是数字 `25`

### 在我们项目里的例子
```python
path = input("请输入文件夹路径: ")
```

### 常见错误
```python
name = Input("...")    # 错误 ❌ Python 严格区分大小写
```
必须是全小写 `input`。

### 怎么记住
`input()` = 程序的"耳朵"。它听用户说什么，然后告诉你。

---

## `print()` — 输出内容

### 是什么
把内容打印到屏幕上。

### 名字含义
**print** = 打印。

### 基本写法
```python
print("Hello World")
print("结果: " + result)
```

### 注意
- `print()` **不会自动加空格**。拼接时空格要自己加。
- `+` 在字符串之间是拼接，在数字之间是加法。**不能混用**。

### 怎么记住
`print()` = 程序的"嘴巴"。它把结果说出来给你看。

---

## 变量赋值 — 给数据起名字

### 是什么
把数据存到一个带名字的容器里。

### 基本写法
```python
name = "张三"        # 字符串
age = 25             # 数字
files = ["a.jpg"]    # 列表
```

### 本质
`=` 不是数学里的"等于"，而是"**把右边的值装进左边的盒子**"。

### 常见错误
```python
name = "张三"
print(Name)          # 错误 ❌ Python 区分大小写
```
`name` 和 `Name` 是两个不同的变量。

### 怎么记住
变量名 = 一个标签，贴在数据上。你想用什么名字都行，但要见名知义。

---

## 字符串 — 文字数据

### 是什么
用引号包起来的文字。

### 基本写法
```python
"Hello"              # 双引号
'Hello'              # 单引号（效果一样）
```

### 字符串拼接 `+`
```python
"Hello " + "World"   # → "Hello World"
```

### 常见错误
```python
"年龄: " + 25        # 错误 ❌ 不能拼接字符串和数字
"年龄: " + str(25)   # 正确 ✅ 先把数字转字符串
```

### 怎么记住
字符串 = 人类说的话。数字可以加减，字符串只能拼接。

---

## `list` 列表 — 装东西的容器

### 是什么
用 `[]` 包起来的一组数据，按顺序排列。

### 基本写法
```python
files = ["a.jpg", "b.pdf", "c.py"]
print(files[0])      # → "a.jpg"（第一个，索引从 0 开始）
```

### 在我们项目里的例子
```python
files = os.listdir(path)   # 返回一个列表
# ['a.jpg', 'b.pdf', 'c.py']
```

### 本质
当你有"很多个东西"时，用列表把它们装在一起，一个一个处理。

### 怎么记住
列表 = 一个盒子，里面可以放很多东西。`[0]` 是第一个，`[1]` 是第二个。

---

## `for` 循环 — 一个一个处理

### 是什么
从列表/集合里按顺序取每一个元素，对每个元素执行一段代码。

### 基本写法
```python
for file in files:
    print(file)
```

### 执行流程
```
第 1 轮：file = files[0]  →  执行缩进里的代码
第 2 轮：file = files[1]  →  执行缩进里的代码
...
列表走完，循环结束
```

### 关键语法
- `for 变量 in 列表:` → **冒号必须写**
- 循环体 **必须缩进**

### 常见错误
```python
for file in files    # 错误 ❌ 少了冒号
    print(file)
```

### 怎么记住
`for` = "每一个都做一遍"。就像点名，点到谁谁站起来回答。

---

## `if` / `elif` / `else` — 条件判断

### 是什么
让程序根据条件做不同的事情。

### 基本写法
```python
if file.endswith(".jpg"):
    print("图片")
elif file.endswith(".pdf"):
    print("文档")
else:
    print("其他")
```

### 执行逻辑
- **从上到下检查**，第一个满足的就执行，后面跳过
- `if`：第一个条件
- `elif`：前面的不满足，再判断这个（注意是 `elif`，不是 `else if`）
- `else`：所有条件都不满足时的兜底

### 常见错误
```python
else if file.endswith(".pdf"):    # 错误 ❌ Python 必须写 elif
elif file.endswith(".pdf"):       # 正确 ✅
```

### 怎么记住
`if` = 如果。`elif` = 否则如果。`else` = 否则。**从上到下排队判断。**

---

## `or` — 逻辑"或"

### 是什么
连接两个条件，有一个是 `True` 整体就是 `True`。

### 基本写法
```python
if file.endswith(".jpg") or file.endswith(".png"):
    print("图片")
```

### 常见错误
```python
file.endswith(".jpg" or ".png")    # 逻辑错误！只检查 .jpg
```
**原因**：`".jpg" or ".png"` 先被计算 → 结果是 `".jpg"`。所以 `file.endswith(".jpg")` 只检查 jpg。

**正确写法**：
```python
file.endswith(".jpg") or file.endswith(".png")    # 方法 1
file.endswith((".jpg", ".png"))                    # 方法 2（更优雅）
```

### 怎么记住
`or` = 两条路，走通任意一条就算通了。

---

## 缩进 — Python 最重要的语法规则

### 是什么
用空格表示代码的**层级关系**。缩进决定"代码属于谁"。

### 不是美观，是语法
Python 用缩进来判断哪些代码是一起的。**没有大括号 `{}`，全靠缩进。**

### 基本规则
```python
for file in files:              # 第 1 层
    if file.endswith(".py"):    # 第 2 层（属于 for）
        print("代码")            # 第 3 层（属于 if）
    else:                        # 第 2 层（属于 for）
        print("非代码")          # 第 3 层（属于 else）
print("循环结束")                # 第 0 层（不属于任何循环，只执行一次）
```

### 如果 print 没缩进会怎样

```python
for file in files:
    if file.endswith(".py"):
print("代码")       # IndentationError! if 下面必须有缩进的代码
```

### 换 Tab 行不行？
能用 Tab，但**不要和空格混用**。Python 官方推荐 4 个空格。大多数编辑器按 Tab 自动转 4 个空格。

### 常见错误
| 错误 | 原因 |
|------|------|
| `IndentationError` | 该缩进的地方没缩进 |
| 第 1 层 3 个空格，第 2 层 4 个空格 | 不一致，看着对齐了但 Python 不认 |
| 混用 Tab 和空格 | 非常隐蔽，建议编辑器打开"显示空白字符" |

### 怎么记住
**缩进 = 代码的身份证**，告诉 Python "我属于谁"。冒号下面缩进的代码听冒号的话，不缩进的代码谁也不听。

---

## `endswith()` — 判断字符串结尾

### 是什么
判断字符串是否以指定内容结尾。返回 `True`（是）或 `False`（否）。

### 名字含义
**ends with** = 以……结尾。

### 基本写法
```python
"photo.jpg".endswith(".jpg")    # → True
"photo.png".endswith(".jpg")    # → False
```

### 在我们项目里的例子
```python
if file.endswith(".py"):
    print("代码文件")
```

### 常见错误
```python
file.endswith(".jpg" or ".png")    # 错误 ❌ 只检查 .jpg
```
正确写法：
```python
file.endswith((".jpg", ".png"))    # 元组写法，同时检查多个
```

### 怎么记住
`endswith` = 问"这个文件名是不是以 `.jpg` 收尾的？"

---

## `lower()` — 统一转小写

### 是什么
把字符串里所有字母转成小写。

### 为什么重要
`"Photo.JPG"` 和 `"photo.jpg"` 应该被当成同一个类型。`lower()` 让程序不区分大小写。

### 基本写法
```python
file.lower().endswith(".jpg")
# "PHOTO.JPG".lower() → "photo.jpg"
```

### 怎么记住
`lower()` = 把字母全部"压低"成小写。

---

## 注释 `#` — 给人看的说明

### 是什么
`#` 后面的内容 Python 会忽略，不执行。是写给**人**看的。

### 基本写法
```python
# 这是一个注释，解释下面代码在干什么
name = input("请输入名字: ")
```

### 怎么记住
`#` = 对 Python 说"闭嘴，这段不用你跑"。

---

## 函数调用的括号 `()`

### 是什么
调用函数时必须加 `()`，里面放参数。

### 规则
```python
print("hello")       # 有括号 ✅
print "hello"        # Python 3 中错误 ❌
os.listdir(".")      # 函数名(参数) ✅
```

### 怎么记住
函数 = 一台机器，`()` 是启动按钮。不按 `()`，机器不动。

---

## 方法调用的点 `.`

### 是什么
对象后面加 `.方法名()`，调用这个方法。

### 规则
```python
"hello".upper()       # → "HELLO"
file.endswith(".py")  # file 是字符串对象，endswith 是它的方法
os.listdir(".")       # os 是模块，listdir 是它的函数
os.path.join(a, b)    # os.path 是子模块，join 是它的函数
```

### 怎么记住
`.` = 的。`file.endswith()` = "file 的 endswith 方法"。

---

## `continue` — 跳过本轮循环

### 是什么
在 `for` 循环里，遇到 `continue` 时跳过当前这一轮，直接进入下一轮。

### 在我们项目的潜在用法
```python
for file in files:
    if file.startswith("."):     # 跳过隐藏文件
        continue
    if os.path.isdir(file):      # 跳过文件夹
        continue
    # 只处理普通文件...
```

### 怎么记住
`continue` = 这一轮不玩了，下一轮继续。

---

## 复习问题

1. `import os` 之后，为什么写 `listdir()` 会报错？
2. `input()` 返回的是数字还是字符串？如果用户输入 `25` 呢？
3. `=` 和 `==` 有什么区别？
4. `for file in files:` 的冒号可以省略吗？
5. `elif` 和 `else if` 在 Python 里哪个是正确的？
6. `file.endswith(".jpg" or ".png")` 为什么是错的？
7. 缩进在 Python 里是美观要求还是语法要求？
8. `IndentationError` 是什么原因导致的？
9. `#` 后面的内容会被 Python 执行吗？
