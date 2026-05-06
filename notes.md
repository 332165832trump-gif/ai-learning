# 编程学习笔记

---

## 学习路线总纲

### 核心认知

未来真正值钱的不是"比 AI 敲代码快"，而是：

> 懂业务 + 会拆问题 + 会指挥 AI + 会验证结果 + 能把流程自动化

### 三条主线

| 主线 | 方向 | 核心能力 |
|---|---|---|
| 数据获取 | 爬虫 / API / 多网站数据采集 | requests、BeautifulSoup、pandas、正则、JSON |
| 自动化执行 | 浏览器自动化 / 文件自动化 / 任务调度 | Playwright、Selenium、定时任务、日志 |
| 金融建模 | 数据清洗 → 指标构造 → 策略回测 → 风险控制 | pandas、numpy、回测框架、可视化 |

### 边界声明

- **能做的**：自动填表、监控余票/课程状态、提醒手动操作、抓取公开数据、调用官方 API、金融数据分析
- **不能碰的**：绕过验证码、绕过排队、批量抢票、规避平台限制、自动下单抢购

> 真正高级的路线不是"写抢票外挂"，而是学会：**监控信息变化 → 快速提醒 → 合规辅助决策 → 人来确认执行**

---

### 第一阶段：Python 自动化基础

**待掌握**：
- 文件操作
- 定时任务
- 读取网页
- 解析 HTML
- 保存 CSV / Excel
- 异常处理
- 日志记录

**目标项目**：
- 自动整理文件
- 批量下载公开网页数据
- 定时抓取价格并保存
- 检测网页变化后提醒

---

### 第二阶段：网页数据采集

**待掌握**：
- `requests`
- `BeautifulSoup`
- `pandas`
- 正则表达式
- API 请求
- JSON 数据
- 反爬基础认知

**合法方向**：
- 财经新闻抓取
- 上市公司公告抓取
- 基金净值抓取
- 宏观经济指标抓取
- 币价行情抓取

---

### 第三阶段：浏览器自动化

**待掌握**：
- Playwright
- Selenium
- 表单自动填写
- 网页状态监控
- 截图
- 自动登录自己的账号

**合规项目**：
- 自动打开选课页面
- 自动检测课程是否有余量
- 有变化就微信/邮件/桌面提醒
- 由你自己点击确认

---

### 第四阶段：金融数据能力

**数据流**：数据源 → 清洗 → 因子 → 回测 → 风控 → 报告

**可做项目**：
- A股/美股/加密货币价格监控系统
- 宏观数据自动更新仪表盘
- ETF 轮动策略回测
- 财报公告情绪分析
- 新闻事件驱动策略
- 投资组合风险监控

---

## 技术笔记

### 1. Git 基础操作

#### 1.1 初始化仓库 — `git init`

**作用**：把普通文件夹变成 Git 仓库（让 Git 开始跟踪这个文件夹里的变化）。

```bash
# 在项目文件夹里执行
git init
# 输出：Initialized empty Git repository in ...
```

**发生了什么**：Git 在文件夹里悄悄创建了一个隐藏目录 `.git`，所有的版本历史、快照信息都存在里面。删除 `.git` = 仓库变回普通文件夹。

**什么时候用**：新项目的第一条命令。只执行一次。

---

#### 1.2 查看状态 — `git status`

**作用**：看当前仓库里什么文件改过、什么文件没被跟踪。

```bash
git status
# 红色文件名 = 改过但还没 add
# 绿色文件名 = 已经 add，准备 commit
# 提示 "nothing to commit" = 没有新变化
```

**本质**：这是一个"只读"命令，不会改任何东西。它是你的安全绳——每次动手前先看一眼，心里有数。

**新手习惯**：`git add` 之前和 `git commit` 之前各跑一次，养成肌肉记忆。

---

#### 1.3 暂存改动 — `git add`

**作用**：告诉 Git "这些文件的改动我要放到下一个 commit 里"。

```bash
# 暂存单个文件
git add classifier.py

# 暂存当前文件夹所有改动
git add .
```

**本质**：Git 的 commit 不是自动拍所有改动，而是只拍你"add 过的"。这让你可以把一个大改动拆成多个逻辑清晰的 commit。

**关键对比**：

| 状态 | 含义 |
|---|---|
| Working Directory | 你正在改的文件（还没 add） |
| Staging Area | 你 add 过的文件（准备 commit） |
| Repository | 你 commit 过的文件（已保存到历史） |

---

#### 1.4 提交版本 — `git commit -m "..."`

**作用**：把你 add 过的改动拍成一个快照，永久保存到仓库历史里。

```bash
git commit -m "add file classifier"
```

- `-m`：message（消息），引号里写这次改了什么的说明。
- 不加 `-m`，Git 会弹出一个编辑器让你写消息（初学者直接用 `-m` 更简单）。

**工程规范**：
- 消息用英文，动词开头，小写。
- 好例子：`"add user login feature"`
- 烂例子：`"改了点东西"`、`"fix"`

---

#### 1.5 关联远程仓库 — `git remote add origin <URL>`

**作用**：告诉本地仓库，你的代码要推送到 GitHub 上哪个仓库。

```bash
git remote add origin https://github.com/16068/oc-test.git
```

- `origin`：远程仓库的昵称（约定俗成用 origin，你也可以叫别的）。
- 这条命令只执行一次。

**通俗类比**：本地仓库 = 你的电脑，`git remote add` = 给它一个 GitHub 的"收货地址"。之后 push 就是往这个地址发货。

---

#### 1.6 推送到远程 — `git push -u origin main`

**作用**：把本地 commit 上传到 GitHub。

```bash
git push -u origin main
```

- `-u`：把本地 `main` 分支和远程 `origin/main` 绑定。绑定后下次直接 `git push` 就行，不用再写 `origin main`。
- `origin`：远程仓库名。
- `main`：分支名。

**新手注意**：push 之前必须至少有一次 commit，否则 Git 说"没什么可推的"。

---

#### 1.7 完整工作流总结

```
1. git init              ← 仓库初始化（只做一次）
2. git remote add ...    ← 关联 GitHub（只做一次）
3. 写代码 / 改文件 ...
4. git status            ← 看看改了什么
5. git add .             ← 暂存改动
6. git commit -m "..."   ← 提交快照
7. git push              ← 推上 GitHub
8. 回到第 3 步，循环
```

---

### 2. Python 基础

#### 2.1 输入输出 — `input()` 和 `print()`

```python
name = input("请输入你的名字: ")    # 等待用户输入，返回字符串
print("Hello " + name)              # 输出拼接后的字符串
```

- `input()` 返回的**永远是字符串**，即使用户输入 `25`，`name` 里也是 `"25"`（文字），不是数字。
- `+` 在字符串之间是拼接，在数字之间是加法。不能混用。
- `print()` 不会自动加空格，拼接时空格要自己加（`"Hello "` 末尾有空格）。

#### 2.2 导入模块 — `import os`

```python
import os
```

- `import` = "把这个工具箱拿进来"。
- `os` 是 Python 自带的操作系统工具模块（不需要安装）。
- 用模块里的函数必须加前缀：`os.listdir()`，光写 `listdir()` 会报 `NameError`。

#### 2.3 列出文件 — `os.listdir(path)`

```python
files = os.listdir(".")   # "." = 当前目录
print(files)              # 输出：['classifier.py', 'main.py', '.git']
```

- 返回一个**列表**，包含该路径下所有文件和文件夹的名字。
- `.` 表示当前目录，`..` 表示上一级目录。
- 路径不存在 → `FileNotFoundError`。

#### 2.4 Windows 路径 + Python 字符串 = SyntaxError

**报错信息**：
```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
```

**原因**：反斜杠 `\` 是 Python 字符串的转义字符。`\n` 是换行，`\t` 是 Tab。`C:\Users` 里的 `\U` 被当成 Unicode 转义 → 崩溃。

**3 种正确写法**：
```python
# 方法 1：用正斜杠（最推荐）
path = "C:/Users/16068/桌面"

# 方法 2：双反斜杠
path = "C:\\Users\\16068\\桌面"

# 方法 3：原始字符串
path = r"C:\Users\16068\桌面"
```

**最佳实践**：Python 代码里永远用 `/` 写路径；用户通过 `input()` 输入的路径天然安全，不会触发转义。

#### 2.5 Python 缩进的作用

**我遇到的问题**：不理解 `for`、`if`、`print` 的缩进关系，不知道缩进的作用。

**代码示例**：
```python
for file in files:
    if file.endswith(".py"):
        print(file + " 是代码文件")
    else:
        print(file + " 是其他文件")
```

**错误示例**：
```python
for file in files:
    if file.endswith(".py"):
print(file + " 是代码文件")    # 没缩进
```

**错误原因**：`IndentationError: expected an indented block`。Python 用缩进判断"这个 `print` 属于 `if` 还是属于 `for`"。`if` 后面需要至少一行缩进的代码，但你跳到了行首，Python 不知道你想让它执行什么。

**正确理解（重点）**：

- **缩进 = 层级结构**：缩进越多，所属层级越深。就像大纲：
  ```
  for                         → 第 1 层
      if                      → 第 2 层（属于 for）
          print("A")          → 第 3 层（属于 if）
  ```

- **决定代码属于哪个逻辑块**：
  ```python
  for file in files:          # 循环体开始
      print(file)             # 属于 for，每轮都执行
      if file.endswith(".py"): # 属于 for
          print("代码")       # 属于 if，条件成立才执行
  print("循环结束")            # 没有缩进，不属于 for，只执行一次
  ```

- **控制执行范围**：缩进 = 冒号下面"谁听谁的"。缩进 4 格是 Python 约定，Tab 也行但别混用。

**我的理解**：缩进就是"代码的身份证"，告诉 Python "我属于谁"。`if` 下面缩进的代码 = `if` 的小弟，条件成立时才干活。不缩进的代码 = 自由人，不受任何条件约束，每次都执行。

**下次如何避免**：
- 任何以 `:` 结尾的行（`for`、`if`、`elif`、`else`），下一行必须缩进 4 个空格。
- 同一层级的代码缩进格数必须一致。
- 写完 `:` 按回车，大多数编辑器自动帮你缩进。

#### 2.6 文件类型判断 — `endswith()` + `for` + `if/elif/else`

**代码（classifier.py 当前版本）**：
```python
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
```

**关键知识点**：

- **`str.endswith("尾巴")`**：判断字符串是否以指定内容结尾，返回 `True` 或 `False`。
- **`or`**：逻辑"或"。`a or b` → 两者有一个是 `True` 就通过。
- **`if` / `elif` / `else` 是排队判断**：从上到下，第一个满足的就执行，后面全部跳过。`else` 是兜底。
- **`elif` 不是 `else if`**：Python 里必须连写成 `elif`，空格会报 `SyntaxError`。

**常见错误**：

| 错误写法 | 后果 |
|---|---|
| `if .endswith(".jpg")` 忘写 `file` | `NameError` |
| `elif` 写成 `else if` | `SyntaxError` |
| `else:` 后面还写条件 | `SyntaxError` |
| `file.endswith(".jpg" or ".png")` | 语法不报错，但逻辑错误——只检查 `.jpg` |

| 语法 | 效果 |
|---|---|
| `# 标题` | 一级标题 |
| `## 标题` | 二级标题 |
| `**粗体**` | **粗体** |
| `` `代码` `` | 行内代码 |
| ` ``` ... ``` ` | 代码块 |
| `- 条目` | 无序列表 |
| `| 列1 | 列2 |` | 表格 |
| `---` | 分割线 |

---

### 4. AI 辅助学习方法

- **不直接要答案，要思路**：让 AI 拆步骤、解释原因、纠正理解偏差。
- **出错是更好的学习**：错误信息是线索，不是终结。AI 帮你拆解报错比直接给你正确答案更有价值。
- **坚持记笔记**：自己写一遍理解比看十遍教材更深刻。这份文件就是你三个月后最有效的复习材料。
