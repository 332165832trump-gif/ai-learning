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

#### 2.7 文件分类器项目 — 路径的本质

**项目当前进度**：可以列出文件、判断类型、创建分类文件夹、计算目标路径，即将实现移动。

**完整代码（classifier.py 当前版本）**：

```python
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
        new_path = os.path.join(images_folder, file)
        print(file + " → " + new_path)
    elif file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx"):
        new_path = os.path.join(docs_folder, file)
        print(file + " → " + new_path)
    elif file.endswith(".py"):
        new_path = os.path.join(code_folder, file)
        print(file + " → " + new_path)
    else:
        print(file + " → 跳过")
```

**核心理解：路径不是普通字符串**

`os.path.join("C:/test", "images", "photo.jpg")` → `"C:/test/images/photo.jpg"`

| 概念 | 是什么 | 例子 |
|---|---|---|
| `path`（用户输入） | 用户指定的文件夹路径 | `"C:/test"` |
| `images_folder` | 分类后的子文件夹路径 | `"C:/test/images"` |
| `file`（循环变量） | 光秃秃的文件名，不是路径 | `"photo.jpg"` |
| `new_path`（目标路径） | 文件搬家后的完整地址 | `"C:/test/images/photo.jpg"` |

**为什么不能用 `path + "/images/" + file` 拼路径？**

三个隐患：
1. **`\` 是 Python 转义符**：`"\images"` 里的 `\i` 可能被吃掉或转义
2. **Windows 和 Linux 分隔符不同**：`\` vs `/`，手写死一个换平台就炸
3. **path 末尾可能有 `/`**：`"C:/test/" + "/images/"` → 双斜杠 `"C:/test//images/photo.jpg"`

**`os.path.join` 的本质**：它是"懂平台规则的路径拼接器"。你把积木块扔给它，它保证拼出合法路径，该加什么分隔符、该不该去重，它全管。

**移动文件的本质**：

文件移动 = 把文件的"地址（路径）"从旧地址改成新地址。

```
旧地址：C:/test/photo.jpg        （文件现在在哪）
新地址：C:/test/images/photo.jpg  （文件要去哪）
```

`os.rename(旧地址, 新地址)` 做的就是这件事——不是复制再删除，是直接改路径。

**搬家需要两个完整路径**：

| 需要 | 怎么拼 | 结果 |
|---|---|---|
| 起点（旧地址） | `os.path.join(path, file)` | `"C:/test/photo.jpg"` |
| 终点（新地址） | `os.path.join(images_folder, file)` | `"C:/test/images/photo.jpg"` |

有了这两个地址，下一步就是 `os.rename(旧地址, 新地址)` 一步搬家。

#### 2.8 创建文件夹 — `os.makedirs` 详解

```python
os.makedirs(images_folder, exist_ok=True)
```

- **`os.makedirs(路径)`**：创建文件夹。`s` 表示可以创建多层（`a/b/c` 一次性全建好）。
- **`exist_ok=True`**：如果文件夹已经存在，安静跳过，不报错。
  - 不加 → 第二次运行时 `FileExistsError` 崩溃。
  - 加了 → 重复运行完全安全，幂等操作。
- **`os.mkdir()` vs `os.makedirs()`**：
  - `mkdir()` 只能建一层，父目录不存在就报错
  - `makedirs()` 自动补全中间每一层，更稳

**为什么放在循环外面创建？**

创建文件夹只需要做一次，放进 `for` 循环里每判断一个文件就建一次，浪费性能。循环里只做"判断 + 打印（未来：移动）"。

| 语法 | 效果 |
|---|---|
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

---

## Git 完整使用流程笔记

### 1. Git 是什么，GitHub 是什么

**Git** 是一个**本地版本控制工具**。它记录你每次修改文件的历史，让你随时可以回到之前的任意版本。

**GitHub** 是一个**远程代码托管网站**。它把 Git 仓库存在云端，方便备份、分享、多设备同步。

| | Git | GitHub |
|---|---|---|
| 运行位置 | 你的电脑 | 互联网服务器 |
| 断网能用吗 | 能 | 不能 |
| 作用 | 记录版本历史 | 备份 + 展示 + 协作 |
| 关系 | 工具 | 使用 Git 的平台 |

**类比**：Git 是 Word 的"修订记录"功能，GitHub 是把这份 Word 文档存到 OneDrive。

---

### 2. 一个项目从 0 开始上传 GitHub 的完整流程

**场景**：你在 Windows 上创建了项目文件夹 `C:\ai-work\oc-test`，现在想把它上传到 GitHub。

```powershell
cd C:\ai-work\oc-test
git init
git status
git add .
git commit -m "first commit"
git remote add origin https://github.com/用户名/仓库名.git
git branch -M main
git push -u origin main
```

---

#### 2.1 `cd C:\ai-work\oc-test`

- **做什么**：进入你的项目文件夹。
- **为什么**：Git 命令默认只对当前目录生效，先走进去才能操作。
- **常见错误**：路径有中文/空格忘记加引号 → 用 `cd "C:\ai-work\oc-test"`。

#### 2.2 `git init`

- **做什么**：初始化 Git 仓库。在当前文件夹创建隐藏目录 `.git`，Git 从此开始跟踪这个文件夹里的变化。
- **为什么**：没有 `.git` 的文件夹只是普通文件夹，`git init` 让它"升级"为仓库。
- **什么时候用**：每个新项目只执行一次。
- **常见错误**：在已有 `.git` 的文件夹里再执行 `git init` → 一般不报错，但可能会搞乱配置。

#### 2.3 `git status`

- **做什么**：查看当前仓库状态——哪些文件改了、哪些没被跟踪。
- **为什么**：动手前的"安全检查"，让你知道接下来 `add` 会暂存什么。
- **输出解读**：
  - 红色文件名 → 改了但还没 `add`
  - 绿色文件名 → 已经 `add`，等待 `commit`
  - `nothing to commit` → 没有新变化
- **本质**：这是一个**只读**命令，不会修改任何文件。放心跑。

#### 2.4 `git add .`

- **做什么**：把当前目录下所有改动加入"暂存区"（Staging Area）。
- **为什么**：Git 只拍你 `add` 过的文件。不改代码，只是在后台做个记号。
- **`.` 的意思**：当前目录所有文件（包括子文件夹）。
- **也可以指定单个文件**：`git add notes.md`
- **常见错误**：`add` 之后又改了文件 → 新改动不在暂存区，需要再 `add` 一次。

#### 2.5 `git commit -m "first commit"`

- **做什么**：把暂存区的改动拍成一个**快照**（版本记录），永久保存到本地仓库历史。
- **`-m`**：message，提交信息。引号里写这次改了什么。
- **`"first commit"`**：第一条提交信息，约定俗成。
- **为什么**：`add` 只是标记，`commit` 才是真正保存。没有 commit 就没有版本。
- **常见错误**：
  - 没有 `add` 就直接 `commit` → 提示 `nothing to commit`
  - `-m` 后面忘记写引号 → 命令失败

#### 2.6 `git remote add origin https://github.com/用户名/仓库名.git`

- **做什么**：告诉本地仓库"你的远程仓库地址是什么"。
- **`origin`**：远程仓库的昵称（约定俗成，可以改，但没人改）。
- **为什么**：本地和远程是两个独立的东西，这条命令把它们关联起来。
- **什么时候用**：每个项目只执行一次。
- **常见错误**：URL 写错 → push 时提示 `repository not found`。

#### 2.7 `git branch -M main`

- **做什么**：把当前分支重命名为 `main`。
- **`-M`**：强制重命名（即使目标名已存在也覆盖）。
- **为什么**：旧版 Git 默认分支叫 `master`，2020 年后 GitHub 改为 `main`。这条命令确保你用的是 `main`。
- **常见错误**：如果没有旧分支名的问题，可以跳过。不执行这条不影响使用。

#### 2.8 `git push -u origin main`

- **做什么**：把本地 `main` 分支的所有 commit 上传到 GitHub。
- **`-u`**：把本地 `main` 和远程 `origin/main` **绑定**。绑定后下次只需 `git push`，不用再写完整命令。
- **`origin`**：远程仓库名。
- **`main`**：分支名。
- **为什么**：至此，本地代码才真正出现在 GitHub 网页上。
- **常见错误**：push 前没有 commit → `Everything up-to-date` 但实际上什么都没推。

---

### 3. 日常更新 GitHub 的固定流程

**场景**：你改了 `notes.md` 或 `classifier.py`，想把改动同步到 GitHub。

```powershell
git status          # 看看改了什么
git add .           # 暂存所有改动
git commit -m "update notes"   # 生成本地版本
git push            # 上传到 GitHub
```

**每步的细节**：

| 步骤 | 命令 | 发生了什么 | 丢数据吗 |
|---|---|---|---|
| 1 | `git status` | 查看哪些文件变了 | 不丢，只是读取 |
| 2 | `git add .` | 标记改动，放入暂存区 | 不丢，只是标记 |
| 3 | `git commit -m "..."` | 保存一个本地版本快照 | 只有这一步才正式存档 |
| 4 | `git push` | 把本地版本上传到 GitHub | 不丢，同步到云端 |

**关键认知**：AI（OpenCode/Codex）改完文件后，GitHub 不会自动更新。**必须手动执行 add → commit → push**，GitHub 上才能看到变化。

---

### 4. 如果 GitHub 云端改了内容，本地怎么同步

**场景**：Codex 在 GitHub 上修改了 `notes.md`，你本地还是旧版本。

```powershell
git pull
```

- **`git pull`**：从 GitHub 下载最新内容到本地。
- **核心对比**：
  - **你改了 → `push`** 上传到 GitHub
  - **GitHub 改了 → `pull`** 下载到本地

**`Already up to date.` 是什么意思**：
- 本地的 commit 记录和远程完全一致，没有新内容可以拉。
- **注意**：这不代表远程一定是最新的。如果你在本地改了但还没 `commit`+`push`，`git pull` 不会发现这些改动。它只看 commit 记录，不看工作区文件。

---

### 5. branch 分支是什么

**用比喻理解**：分支就像**平行世界**。

- `main`：真实世界（正式版本）
- `codex/xxx`：平行世界（AI 做的实验）

你在平行世界里随便改，不影响真实世界。实验成功了就"合并"（merge）回来。

**查看分支**：

```powershell
git branch       # 只看本地分支，当前分支前有 *
git branch -a    # 看本地 + 远程所有分支
```

输出示例：
```
* main                                   ← 你当前在 main
  remotes/origin/main                    ← GitHub 上的 main
  remotes/origin/codex/enhance-note...   ← Codex 创建的分支
```

**切换分支**：

```powershell
git checkout main    # 回到 main 分支
```

**从远程分支创建本地分支**：

```powershell
git checkout -b codex-review origin/codex/enhance-note.md-content-with-details
```

- **`-b`**：创建新分支并切换过去
- **`codex-review`**：本地分支名（你自己起）
- **`origin/codex/...`**：远程分支路径
- 这条命令的意思是"把远程那个分支复制一份到我本地，取名 codex-review"

---

### 6. 如何查看 Codex 改了什么

```powershell
git diff main..origin/codex/enhance-note.md-content-with-details -- notes.md
```

- **`git diff A..B`**：比较两个分支的差异
- **`-- notes.md`**：只看这个文件的差异（可选，不加则显示所有文件差异）
- **输出颜色**：
  - **绿色 `+`** → 新增的内容
  - **红色 `-`** → 删除的内容
- **出现 `(END)` 时按 `q` 退出**：这不是报错，是 Git 在用 `less`（分页器）显示长内容。按 `q` 回到命令行。

---

### 7. 如何合并 Codex 分支到 main

```powershell
git checkout main                                              # 1. 切回 main
git merge origin/codex/enhance-note.md-content-with-details    # 2. 合并分支
git push                                                       # 3. 上传到 GitHub
```

**每步解释**：
1. **切回 main**：你要把东西合并到 main，所以必须站在 main 上操作。
2. **合并**：把 Codex 分支的改动"融入"到 main。如果有新东西就加进来，如果没变化就提示 `Already up to date.`
3. **push**：合并发生在本地，GitHub 还不知道。必须 push 才能让远程 main 也更新。

---

### 8. 合并冲突是什么

**什么情况下会冲突**：同一个文件的**同一行**被两个分支**同时修改**，Git 不知道该听谁的。

**不一定会冲突的情况**：
- Codex 在文件末尾加了新内容，你在文件开头改了 → **不冲突**（位置不同）
- Codex 新增了一个文件，你没碰它 → **不冲突**

**冲突长什么样**：

```
<<<<<<< HEAD
这是 main 分支的内容
=======
这是 codex 分支的内容
>>>>>>> origin/codex/xxx
```

- `<<<<<<< HEAD` ~ `=======`：你当前分支（main）的内容
- `=======` ~ `>>>>>>> xxx`：对方分支的内容
- 你需要手动删除标记，保留你想要的那一段。

**遇到冲突怎么办**：
1. **不要乱删**。看清楚两段内容，决定保留哪个。
2. 如果暂时不想处理，可以取消合并：

```powershell
git merge --abort
```

这会回到合并前的状态，一切恢复原样。

---

### 9. 常见错误和解释

#### 9.1 `src refspec main does not match any`

**原因**：还没有做第一次 commit，或你不在 main 分支上。

**解决**：
```powershell
git add .
git commit -m "first commit"
git push -u origin main
```

#### 9.2 `Author identity unknown`

**原因**：Git 不知道你是谁（用户名和邮箱没配置）。

**解决**：
```powershell
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
```

**`--global` 的含义**：全局设置，这台电脑上所有 Git 仓库都用这个身份。只设一次。

#### 9.3 `Everything up-to-date`

**含义**：没有新的本地 commit 需要 push。

**注意**：这**不代表** GitHub 上一定有你想要的内容。可能你改的文件没 add/commit，或者你在另一个环境改的。它以 commit 为准，不是以文件为准。

#### 9.4 `nothing to commit, working tree clean`

**含义**：当前文件夹所有文件都被 Git 记录过了，没有新改动。是好事，不是报错。

#### 9.5 `Failed to connect to github.com port 443`

**原因**：网络问题，不是 Git 命令问题。

**常见场景**：
- 没开代理/VPN
- 防火墙拦截
- GitHub 暂时不可达

**解决思路**：
- 换手机热点试试
- 检查代理是否开启

如果使用 Clash，设置代理：
```powershell
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

取消代理：
```powershell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

### 10. OpenCode / Codex / ChatGPT 配合 GitHub 的正确工作流

**角色分工**：

| 角色 | 做什么 |
|---|---|
| **ChatGPT** | 规划方案、解释概念、纠正错误 |
| **OpenCode / Codex** | 修改代码或笔记文件 |
| **Git** | 记录每次修改的版本 |
| **GitHub** | 保存和展示学习过程 |

**工作流 A：本地 OpenCode 改文件后**

```
OpenCode 改完文件
    ↓
git status              ← 确认改了哪些文件
    ↓
git add .               ← 暂存
    ↓
git commit -m "..."     ← 存版本
    ↓
git push                ← 同步到 GitHub
```

**工作流 B：Codex 云端改文件后**

```
git pull                ← 拉取远程更新
```

**工作流 C：Codex 创建了新分支**

```
git branch -a           ← 查看所有分支
    ↓
git diff main..远程分支 -- 文件名   ← 看 Codex 改了什么
    ↓
git checkout main       ← 切回 main
    ↓
git merge 远程分支名     ← 合并 Codex 的改动
    ↓
git push                ← 推上 GitHub
```

---

### 11. 日常 Git 使用速查表

| 场景 | 命令 | 解释 |
|---|---|---|
| 查看当前状态 | `git status` | 看哪些文件变了，是不是干净 |
| 提交所有修改 | `git add .` | 把所有改动加入暂存区 |
| 生成版本 | `git commit -m "message"` | 本地保存一次版本快照 |
| 上传 GitHub | `git push` | 把本地 commit 同步到远程 |
| 从 GitHub 拉取 | `git pull` | 获取远程最新内容到本地 |
| 查看分支 | `git branch -a` | 看本地和远程所有分支 |
| 切换 main | `git checkout main` | 回到正式分支 |
| 合并分支 | `git merge 分支名` | 把其他分支改动合进来 |
| 取消合并 | `git merge --abort` | 合并出问题时撤销，恢复原样 |
| 查看差异 | `git diff A..B -- 文件` | 比较两个分支的差异 |
| 看提交历史 | `git log --oneline` | 简洁列出所有 commit |

---

### 12. 最重要的本质总结

- **Git 不是上传工具**，是**版本管理工具**。它能回到过去任何一次修改。
- **add / commit / push 是三件不同的事**：标记 → 存档 → 上传。少一步都不行。
- **本地和 GitHub 是两个独立的地方**：你在本地改完不 push，GitHub 永远看不到。
- **AI 改完文件 ≠ GitHub 更新**：OpenCode 动了文件只是动了你电脑上的文件，Git 还没记录，GitHub 更不知道。
- **分支是安全试验区**：在分支里随便折腾，不影响 main。试错了删掉就行。
- **merge 是把试验成果合并回来**：分支改满意了，合进 main，成为正式版本。
- **学会 Git 的目的**：让学习过程可追踪、可复盘、可展示。每个项目都是一条清晰的 commit 时间线。
