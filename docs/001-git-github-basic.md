# 001 - Git 与 GitHub 基础

## 1. Git 是什么

**一句话**：Git 是**本地版本控制工具**，它记录你每次修改文件的历史，让你随时可以回到之前的任意版本。

它不是"上传工具"，不是"另存为"，不是网盘。它是一个**时间线记录器**。

**类比**：Git 是 Word 里的"修订记录"功能——你能看到谁在什么时候改了什么，还能随时回退到修改之前。

## 2. GitHub 是什么

**一句话**：GitHub 是**云端代码托管网站**。它把 Git 仓库存在互联网上，方便备份、分享、多设备同步。

**类比**：GitHub 是把你的 Word 文档（带着修订记录）存到 OneDrive 上。

## 3. Git 和 GitHub 的区别

| | Git | GitHub |
|---|---|---|
| 运行在哪 | 你的电脑 | 互联网服务器 |
| 断网能用吗 | 能 | 不能 |
| 作用 | 记录版本历史 | 备份 + 展示 + 协作 |
| 关系 | 工具 | 使用 Git 的平台 |

**核心认知**：Git 是锤子，GitHub 是展示柜。你在家用锤子干活，把成果放到展示柜给别人看。

## 4. 从 0 上传项目到 GitHub

**场景**：你在 Windows 上创建了一个项目文件夹 `C:\ai-work\oc-test`。

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

### 4.1 `cd C:\ai-work\oc-test`

- **做什么**：进入项目文件夹。
- **为什么**：Git 命令默认只对当前目录生效。
- **常见错误**：路径有空格/中文忘记加引号 → `cd "C:\my folder"`。

### 4.2 `git init`

- **做什么**：初始化 Git 仓库。创建隐藏目录 `.git`。
- **什么时候用**：每个项目只执行一次。
- **本质**：普通文件夹 → Git 仓库的"升级仪式"。

### 4.3 `git status`

- **做什么**：查看仓库状态——哪些文件改了、哪些没被跟踪。
- **本质**：只读命令，不修改任何东西。它是你的"安全绳"。
- **输出解读**：
  - 红色文件名 → 改了但还没 `add`
  - 绿色文件名 → 已经 `add`，等待 `commit`
  - `nothing to commit` → 没有新变化

### 4.4 `git add .`

- **做什么**：把当前目录所有改动加入**暂存区**。
- **`.` 的意思**：当前目录所有文件。
- **本质**：标记改动。Git 只"拍"你 add 过的文件。
- **常见错误**：add 之后又改了文件 → 新改动需要再 add 一次。

**关键概念：Git 的三个区域**

| 区域 | 说明 |
|---|---|
| Working Directory | 你正在改的文件（还没 add） |
| Staging Area | 你 add 过的文件（准备 commit） |
| Repository | 你 commit 过的文件（已保存到历史） |

### 4.5 `git commit -m "first commit"`

- **做什么**：把暂存区的改动拍成快照，永久保存。
- **`-m`**：message，提交信息。
- **本质**：add 只是准备，commit 才是真正存档。没有 commit 就没有版本。
- **规范**：消息用英文，动词开头，小写。如 `"add file classifier"`。

### 4.6 `git remote add origin https://github.com/用户名/仓库名.git`

- **做什么**：告诉本地仓库"你的远程地址是什么"。
- **`origin`**：远程仓库的昵称（约定俗成）。
- **什么时候用**：每个项目只执行一次。

### 4.7 `git branch -M main`

- **做什么**：把当前分支强制重命名为 `main`。
- **为什么**：旧版 Git 默认 `master`，GitHub 2020 年后改为 `main`。

### 4.8 `git push -u origin main`

- **做什么**：把本地 commit 上传到 GitHub。
- **`-u`**：绑定本地 `main` 和远程 `origin/main`，绑定后下次直接 `git push` 即可。

## 5. 日常更新 GitHub 的固定流程

```powershell
git status              # 1. 看看改了什么
git add .               # 2. 暂存所有改动
git commit -m "message" # 3. 本地存档
git push                # 4. 上传到 GitHub
```

**每步详解**：

| 步骤 | 命令 | 做了什么 | 丢数据吗 |
|---|---|---|---|
| 1 | `git status` | 查看哪些文件变了 | 不丢，只读 |
| 2 | `git add .` | 标记改动，放入暂存区 | 不丢，只标记 |
| 3 | `git commit -m "..."` | 保存版本快照 | 只有这步存档 |
| 4 | `git push` | 上传到 GitHub | 不丢，同步到云端 |

**关键认知**：AI（OpenCode/Codex）改完文件后，GitHub 不会自动更新。**必须手动 add → commit → push**。

## 6. 常见错误

### 6.1 `src refspec main does not match any`

- **原因**：还没做过第一次 commit。
- **解决**：先 `git add .` → `git commit` → 再 `git push`。

### 6.2 `Author identity unknown`

- **原因**：Git 不知道你是谁。
- **解决**：
```powershell
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
```

### 6.3 `nothing to commit, working tree clean`

- **含义**：没有新改动，一切正常。不是报错。

### 6.4 `Everything up-to-date`

- **含义**：没有新的本地 commit 需要 push。
- **注意**：这不代表 GitHub 上一定有你要的内容。以 commit 为准，不以文件为准。

### 6.5 `Failed to connect to github.com port 443`

- **原因**：网络/代理问题，不是 Git 问题。
- **解决**：检查代理是否开启；或配置 SSH（见 003 笔记）。

## 7. 记忆口诀

> **add 是准备，commit 是存档，push 是上传。**
> **本地改了用 push，远程改了用 pull。**
