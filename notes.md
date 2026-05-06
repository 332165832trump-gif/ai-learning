# Python 学习笔记

---

## 1. Git 基础操作

### 1.1 初始化仓库 — `git init`

**作用**：把普通文件夹变成 Git 仓库（让 Git 开始跟踪这个文件夹里的变化）。

```bash
# 在项目文件夹里执行
git init
# 输出：Initialized empty Git repository in ...
```

**发生了什么**：Git 在文件夹里悄悄创建了一个隐藏目录 `.git`，所有的版本历史、快照信息都存在里面。删除 `.git` = 仓库变回普通文件夹。

**什么时候用**：新项目的第一条命令。只执行一次。

---

### 1.2 查看状态 — `git status`

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

### 1.3 暂存改动 — `git add`

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

### 1.4 提交版本 — `git commit -m "..."`

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

### 1.5 关联远程仓库 — `git remote add origin <URL>`

**作用**：告诉本地仓库，你的代码要推送到 GitHub 上哪个仓库。

```bash
git remote add origin https://github.com/16068/oc-test.git
```

- `origin`：远程仓库的昵称（约定俗成用 origin，你也可以叫别的）。
- 这条命令只执行一次。

**通俗类比**：本地仓库 = 你的电脑，`git remote add` = 给它一个 GitHub 的"收货地址"。之后 push 就是往这个地址发货。

---

### 1.6 推送到远程 — `git push -u origin main`

**作用**：把本地 commit 上传到 GitHub。

```bash
git push -u origin main
```

- `-u`：把本地 `main` 分支和远程 `origin/main` 绑定。绑定后下次直接 `git push` 就行，不用再写 `origin main`。
- `origin`：远程仓库名。
- `main`：分支名。

**新手注意**：push 之前必须至少有一次 commit，否则 Git 说"没什么可推的"。

---

### 1.7 完整工作流总结

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

## 2. Python 基础

### 2.1 输入输出 — `input()` 和 `print()`

```python
name = input("请输入你的名字: ")    # 等待用户输入，返回字符串
print("Hello " + name)              # 输出拼接后的字符串
```

- `input()` 返回的**永远是字符串**，即使用户输入 `25`，`name` 里也是 `"25"`（文字），不是数字。
- `+` 在字符串之间是拼接，在数字之间是加法。不能混用。
- `print()` 不会自动加空格，拼接时空格要自己加（`"Hello "` 末尾有空格）。

### 2.2 导入模块 — `import os`

```python
import os
```

- `import` = "把这个工具箱拿进来"。
- `os` 是 Python 自带的操作系统工具模块（不需要安装）。
- 用模块里的函数必须加前缀：`os.listdir()`，光写 `listdir()` 会报 `NameError`。

### 2.3 列出文件 — `os.listdir(path)`

```python
files = os.listdir(".")   # "." = 当前目录
print(files)              # 输出：['classifier.py', 'main.py', '.git']
```

- 返回一个**列表**，包含该路径下所有文件和文件夹的名字。
- `.` 表示当前目录，`..` 表示上一级目录。
- 路径不存在 → `FileNotFoundError`。

### 2.4 Windows 路径 + Python 字符串 = SyntaxError

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

---

## 3. Markdown 记笔记

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

## 4. AI 辅助学习方法

- **不直接要答案，要思路**：让 AI 拆步骤、解释原因、纠正理解偏差。
- **出错是更好的学习**：错误信息是线索，不是终结。AI 帮你拆解报错比直接给你正确答案更有价值。
- **坚持记笔记**：自己写一遍理解比看十遍教材更深刻。这份文件就是你三个月后最有效的复习材料。
