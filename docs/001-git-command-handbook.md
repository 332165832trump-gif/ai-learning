# 001 - Git 命令完整手册：从本地记录到 GitHub 上传

> 面向零基础初学者。每个命令按「是什么→为什么→怎么写→参数含义→正常输出→常见错误→Debug→怎么记住」组织。

---

## `cd` — 进入文件夹

### 是什么
切换当前工作目录（Change Directory）。

### 什么时候用
每次要操作某个项目文件夹时，先 `cd` 进去。Git 命令默认只对当前目录生效。

### 基本写法
```powershell
cd C:\ai-work\oc-test
```

### 正常输出
没有输出（光标跳到下一行，但提示符前面会变成新路径）。

### 常见错误
- 路径有空格没加引号 → `cd "C:\my folder"`
- 路径不存在 → `系统找不到指定的路径`

### 怎么记住
`cd` = **C**hange **D**irectory。你要去哪个文件夹，就跟在 `cd` 后面。

---

## `pwd` — 看当前在哪

### 是什么
打印当前工作目录（Print Working Directory）。PowerShell 中也可以用 `Get-Location`。

### 什么时候用
不确定自己"站"在哪个文件夹时。

### 基本写法
```powershell
pwd
```

### 正常输出
```
Path
----
C:\ai-work\oc-test
```

### 怎么记住
`pwd` = 告诉我"我在哪"。类似于手机地图的"当前位置"按钮。

---

## `git init` — 初始化仓库

### 是什么
把普通文件夹"升级"为 Git 仓库。在当前文件夹创建隐藏目录 `.git`。

### 名字含义
**init** = initialize（初始化）。

### 什么时候用
每个新项目只执行一次。在项目文件夹里跑。

### 基本写法
```powershell
cd C:\ai-work\oc-test
git init
```

### 正常输出
```
Initialized empty Git repository in C:/ai-work/oc-test/.git/
```

### 本质
删除 `.git` 文件夹 = 仓库变回普通文件夹。`.git` 里存了所有版本历史。

### 常见错误
- 在已有 `.git` 的文件夹里再执行 → 一般不报错，但可能搞乱配置
- 在非项目文件夹执行 → 会把整个大文件夹变成仓库（不推荐）

### 怎么记住
`git init` = 项目的"出生证明"。不 init，Git 不认识这个文件夹。

---

## `git status` — 查看仓库状态

### 是什么
查看当前仓库里什么文件改过、什么文件没被跟踪。

### 名字含义
**status** = 状态。

### 什么时候用
**每次动手前都要跑一次**。`git add` 之前跑，`git commit` 之前再跑。

### 基本写法
```powershell
git status
```

### 参数解释
不需要参数。裸跑就够。

### 正常输出解读
```
On branch main
Changes not staged for commit:
  modified:   notes.md        ← 红色：改了但还没 add

Untracked files:
  newfile.py                   ← 红色：新文件，Git 不认识

no changes added to commit     ← 提示：该 add 了
```

```
On branch main
Changes to be committed:
  modified:   notes.md        ← 绿色：已经 add，准备 commit
```

```
On branch main
nothing to commit, working tree clean   ← 没有新变化，一切干净
```

### 本质
这是一个**只读**命令，不会修改任何文件。可以无限次跑。

### 常见错误
没有常见错误。它是安全的。

### 怎么记住
`git status` = 给仓库拍一张 X 光片，看里面有什么变化。**每次动手前必跑。**

---

## `git add .` — 暂存所有改动

### 是什么
把当前目录所有改动加入"暂存区"（Staging Area）。

### 名字含义
**add** = 添加。**`.` ** = 当前目录所有文件。

### 什么时候用
改完代码、准备存档（commit）之前。

### 基本写法
```powershell
git add .
```

### 参数解释
- `.`：当前目录下所有文件和子文件夹
- 也可以用 `git add notes.md` 只暂存指定文件
- 也可以用 `git add *.md` 暂存所有 .md 文件

### 正常输出
没有输出（静默执行）。

### 本质
`add` 只是"标记"，不是"存档"。它告诉 Git："下一个 commit 请包含这些改动。"

**Git 的三个区域**：
```
工作区（你改的文件）
    ↓ git add
暂存区（准备 commit 的文件）
    ↓ git commit
仓库（已存档的历史版本）
```

### 常见错误
- `add` 之后又改了文件 → 新改动不在暂存区，需要再 `add` 一次
- 忘记 `add` 直接 `commit` → 提示 `nothing to commit`

### 怎么记住
`git add .` = "这张照片里包含这些改动，准备拍快照。"

---

## `git commit -m "message"` — 保存版本

### 是什么
把暂存区的改动拍成**快照**，永久保存到本地仓库历史。

### 名字含义
**commit** = 提交、存档。**-m** = message（提交信息）。

### 什么时候用
`git add` 之后，确认要把这些改动存档时。

### 基本写法
```powershell
git commit -m "add file classifier"
```

### 参数解释
- `-m "..."`：提交信息（commit message）。**必须写**，否则 Git 会弹出编辑器让你写。
- 信息约定：英文、动词开头、小写、简洁描述改了啥。

### 正常输出
```
[main a1b2c3d] add file classifier
 1 file changed, 10 insertions(+)
```

- `main`：当前分支
- `a1b2c3d`：这次 commit 的 ID
- `1 file changed`：改了 1 个文件
- `10 insertions(+)`：新增了 10 行

### 常见错误
| 错误 | 原因 |
|------|------|
| `nothing to commit` | 没先 `add`，或文件没改动 |
| 忘记写 `-m` | 弹出 vim 编辑器，按 `:q!` 退出 |

### 怎么记住
`git commit` = 拍一张带日期的快照。`-m` = 给这张快照写标题。**只存档在本机，还没上传。**

---

## `git config --global user.name / user.email` — 设置身份

### 是什么
告诉 Git 你是谁。commit 记录里会附上这个身份信息。

### 什么时候用
安装 Git 后第一次用，或换电脑时。一台电脑只设一次。

### 基本写法
```powershell
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
```

### 参数解释
- `--global`：全局设置，这台电脑所有 Git 仓库都用这个身份

### 正常输出
没有输出。

### 常见错误
| 错误 | 原因 |
|------|------|
| `Author identity unknown` | 没设过，commit 时 Git 不知道你是谁 |

### 怎么记住
`git config --global` = 在 Git 的"身份证"上写名字和邮箱。只写一次。

---

## `git remote add origin <URL>` — 关联远程仓库

### 是什么
告诉本地仓库：你的代码要推送到 GitHub 上哪个地址。

### 名字含义
**remote** = 远程。**add** = 添加。**origin** = 远程仓库的昵称（约定俗成）。

### 什么时候用
`git init` 之后，第一次 `push` 之前。每个项目只执行一次。

### 基本写法
```powershell
git remote add origin https://github.com/用户名/仓库名.git
```

### 参数解释
- `origin`：远程仓库的昵称。大家都用 `origin`，你也可以改成别的。
- `<URL>`：GitHub 上你的仓库地址（HTTPS 或 SSH 格式）。

### 正常输出
没有输出。

### 常见错误
- URL 写错 → push 时提示 `repository not found`
- 重复添加 → 提示 `remote origin already exists`

### 怎么记住
`git remote add origin` = 给本地仓库一个 GitHub 的"收货地址"。之后 `push` 就是往这个地址发货。

---

## `git remote -v` — 查看远程地址

### 是什么
看当前仓库关联的远程地址是什么。

### 名字含义
**remote** = 远程。**-v** = verbose（详细模式）。

### 基本写法
```powershell
git remote -v
```

### 正常输出
```
origin  https://github.com/332165832trump-gif/ai-learning.git (fetch)
origin  https://github.com/332165832trump-gif/ai-learning.git (push)
```

- `fetch`：从哪拉取
- `push`：推送到哪
- 如果看到 `git@github.com:...` → 用的是 SSH

### 怎么记住
`git remote -v` = 看你的仓库绑定的 GitHub 地址是什么。

---

## `git remote set-url origin <URL>` — 修改远程地址

### 是什么
把仓库的远程地址换成新的（比如从 HTTPS 改 SSH）。

### 什么时候用
- 仓库搬家了（GitHub 改名/转移）
- 切 HTTPS 到 SSH 或反过来

### 基本写法
```powershell
# 改成 SSH
git remote set-url origin git@github.com:332165832trump-gif/ai-learning.git
```

### 正常输出
没有输出。跑完用 `git remote -v` 验证。

### 怎么记住
`git remote set-url` = 给仓库换一个新的"收货地址"。

---

## `git branch -M main` — 重命名分支

### 是什么
把当前分支强制重命名为 `main`。

### 名字含义
**branch** = 分支。**-M** = move/rename（强制模式）。

### 什么时候用
旧版 Git 默认分支叫 `master`，GitHub 2020 年后改为 `main`。新项目跑一次对齐。

### 基本写法
```powershell
git branch -M main
```

### 正常输出
没有输出。

### 常见错误
- 如果不确定当前分支叫什么，先跑 `git branch` 查看

### 怎么记住
`git branch -M main` = 把分支名改成 main（只做一次）。

---

## `git push -u origin main` — 首次上传

### 是什么
把本地 `main` 分支的所有 commit 上传到 GitHub，并绑定本地和远程分支。

### 名字含义
**push** = 推送。**-u** = set upstream（绑定上游）。**origin** = 远程仓库。**main** = 分支名。

### 什么时候用
第一次 push 时，需要绑定本地分支和远程分支。

### 基本写法
```powershell
git push -u origin main
```

### 参数解释
- `-u`（或 `--set-upstream`）：绑定后下次只需 `git push`，不用再写 `origin main`

### 正常输出
```
Enumerating objects: 5, done.
Writing objects: 100% (5/5), done.
To https://github.com/用户/仓库.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### 常见错误
| 错误 | 原因 |
|------|------|
| `src refspec main does not match any` | 还没做过第一次 `commit` |
| `failed to connect to github.com port 443` | 网络/代理问题 |

### 怎么记住
`git push -u origin main` = "首次上传，绑定通道"。以后只需 `git push`。

---

## `git push` — 上传到 GitHub

### 是什么
把本地 commit 推送到 GitHub 远程仓库。

### 名字含义
**push** = 推送（本地→远程）。

### 什么时候用
每次 `commit` 之后，想把改动同步到 GitHub 上时。

### 基本写法
```powershell
git push
```

### 正常输出
```
Enumerating objects: 5, done.
To github.com:用户/仓库.git
   a1b2c3d..e4f5g6h  main -> main
```

- `a1b2c3d..e4f5g6h`：从旧 commit 到新 commit
- `main -> main`：本地 main 推到了远程 main

### 常见错误
| 错误 | 原因 |
|------|------|
| `Everything up-to-date` | 本地没有新 commit 可推（不是报错） |
| `Your branch is ahead ... by 1 commit` | 还没 push，Git 在提醒你 |
| 连接失败 | 网络/代理/SSH 问题 |

### 本质
`push` 之前，改动只在你电脑上。**push 之后，GitHub 上才看得到。**

### 怎么记住
`git push` = 把本地的新版本"推送"到 GitHub 云端。

---

## `git pull` — 从 GitHub 拉取

### 是什么
把 GitHub 远程仓库的最新内容下载到本地。

### 名字含义
**pull** = 拉取（远程→本地）。

### 什么时候用
- 你在 GitHub 网页上改了什么
- Codex 在云端改了文件或创建了新分支
- 你在另一台电脑 push 了代码

### 基本写法
```powershell
git pull
```

### 正常输出
```
Already up to date.           ← 本地和远程一致，没有新内容
```
或
```
Updating a1b2c3d..e4f5g6h    ← 有新内容，已拉到本地
Fast-forward
 notes.md | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

### 关键认知
| 情况 | 用哪个 |
|------|--------|
| 你改了本地 → 上传 | `git push` |
| GitHub 上改了 → 下载 | `git pull` |

### 常见错误
| 输出 | 意思 |
|------|------|
| `Already up to date` | 没有新内容，正常 |
| `Already up to date` + 但文件看起来没更新 | 因为只看 commit 记录，不看工作区文件 |

### 怎么记住
`git pull` = 从 GitHub 云端"拉"最新代码到本地。

---

## `git diff` — 查看文件差异

### 是什么
比较两个版本/分支之间的代码差异。

### 基本写法
```powershell
# 看工作区和最后一次 commit 的差异
git diff

# 看两个分支之间的差异（只看指定文件）
git diff main..origin/codex/branch-name -- notes.md
```

### 输出解读
- 绿色 `+` 开头 → 新增的行
- 红色 `-` 开头 → 删除的行
- 出现 `(END)` → 按 `q` 退出

### 怎么记住
`git diff` = "显示不同（**diff**erence）"。在合并 Codex 分支之前必看。

---

## `git checkout` — 切换分支

### 是什么
切换到指定分支。

### 基本写法
```powershell
# 切换到 main 分支
git checkout main

# 从远程分支创建本地分支并切换过去
git checkout -b codex-review origin/codex/branch-name
```

### 参数解释
- `-b`：创建新分支并切换过去
- `codex-review`：你起的本地分支名
- `origin/codex/...`：远程分支路径

### 怎么记住
`git checkout` = "切到那个分支去"。就像切换频道一样。

---

## `git merge` — 合并分支

### 是什么
把指定分支的改动合并到当前分支。

### 基本写法
```powershell
git checkout main                         # 先切到 main
git merge origin/codex/branch-name        # 把 Codex 分支合进来
git push                                  # 同步到 GitHub
```

### 关键规则
合并发生在**本地**。`merge` 之后必须 `push`，GitHub 才知道。

### 常见错误
- 冲突 → 同一文件同一行被两边都改了
- 不确定 → 先 `git merge --abort` 取消

### 怎么记住
`git merge` = 把别的分支的改动"融入"当前分支。

---

## `git merge --abort` — 取消合并

### 是什么
取消正在进行的合并，回到合并前的状态。

### 基本写法
```powershell
git merge --abort
```

### 什么时候用
合并时遇到冲突，不想现在处理。

### 怎么记住
`git merge --abort` = "算了，不合并了，回到之前。"

---

## `git branch` / `git branch -a` — 查看分支

### 是什么
列出分支。`-a` 显示本地+远程所有分支。

### 基本写法
```powershell
git branch        # 只看本地
git branch -a     # 本地 + 远程全部
```

### 输出解读
```
* main                              ← 前面有 * = 当前分支
  remotes/origin/main                ← GitHub 上的 main
  remotes/origin/codex/enhance-note   ← Codex 创建的分支
```

### 怎么记住
`git branch` = 列出所有分支。`-a` = **a**ll（全部）。

---

## `git log --oneline` — 看提交历史

### 是什么
查看 commit 历史，每条一行。

### 基本写法
```powershell
git log --oneline
```

### 正常输出
```
0043b99 docs: reorganize learning notes
c47c045 docs: restructure notes order and add SSH
1730f62 docs: complete file classifier project
```

### 怎么记住
`git log --oneline` = 查看项目的"版本时间线"。

---

## 关键认知速查表

| 概念 | 本质 |
|------|------|
| `git status` | 只读命令，不会改任何文件 |
| `git add .` | 标记改动，不是存档 |
| `git commit` | 本地存档，不是上传 |
| `git push` | 上传到 GitHub |
| `git pull` | 从 GitHub 下载 |
| `Everything up-to-date` | 没有新 commit 要 push |
| `nothing to commit, working tree clean` | 本地没有未提交修改 |
| `Your branch is ahead ... by 1 commit` | 本地比 GitHub 多一个 commit |
| `Already up to date` | 远程没有新变化 |
| `src refspec main does not match any` | 还没做过第一次 commit |
| `Author identity unknown` | Git 不知道你是谁 |

---

## 复习问题

1. `git add` 和 `git commit` 的区别是什么？
2. 为什么 `git status` 可以无限次跑？
3. `Everything up-to-date` 是说 GitHub 上已经有了所有内容吗？
4. `git push -u origin main` 里的 `-u` 是什么意思？
5. `git pull` 什么时候用？它和 `git push` 方向有什么不同？
6. `git merge --abort` 什么时候用？
7. `src refspec main does not match any` 怎么解决？
