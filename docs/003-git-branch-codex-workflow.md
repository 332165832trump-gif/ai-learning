# 003 - Git 分支、合并与 Codex 工作流

> 面向零基础初学者。解释分支是什么、Codex 为什么创建分支、怎么审核和合并。

---

## branch 是什么

### 用"平行世界"比喻

- `main`：**真实世界**（正式版本），你代码的稳定版本
- `codex/xxx`：**平行世界**（AI 实验版本），AI 在一个独立空间里改代码

你在平行世界里随便折腾，不影响真实世界。实验满意了就"合并"（merge）回来，不满意就删掉。

### 本质

分支 = Git 里的一个**指针**，指向某条 commit 时间线上的最新节点。不同分支可以指向不同的节点，各自发展，互不影响。

```
main:     ●──●──●──●──●  (稳定版本)
                       
codex/分支: ●──●──●  (AI 实验版本，从 main 分叉出去的)
```

### 为什么 Codex 会创建新分支

AI 不应该直接改你的正式版本。万一改错了怎么办？

所以 Codex 的默认行为是：**在新分支里改代码，让你审核后再合并到 main**。

---

## 关键概念速查

| 概念 | 含义 | 在哪里 |
|------|------|--------|
| `main` | 主分支（正式版本） | 本地 + GitHub |
| `origin/main` | GitHub 上的 main 分支 | GitHub |
| `remotes/origin/xxx` | GitHub 上的远程分支 | GitHub |
| `codex/xxx` | Codex 创建的实验分支 | GitHub |

---

## 查看分支

### `git branch` — 只看本地分支

```powershell
git branch
```

输出：
```
* main
```

前面的 `*` 表示你当前在哪个分支。

### `git branch -a` — 看所有分支（本地+远程）

```powershell
git branch -a
```

输出：
```
* main
  remotes/origin/main
  remotes/origin/codex/enhance-note.md-content-with-details
```

- `remotes/origin/` 开头的 = GitHub 上的远程分支
- `* main` = 你当前在 main

---

## 切换分支

### `git checkout main` — 回到主分支

```powershell
git checkout main
```

**什么时候用**：
- 看完 Codex 分支，想回到 main
- 合并之前，必须站在目标分支上

### `git checkout -b 本地名 远程分支` — 从远程创建本地副本

```powershell
git checkout -b codex-review origin/codex/enhance-note.md-content-with-details
```

**参数解释**：
- `-b`：创建新分支并切换过去
- `codex-review`：你起的本地分支名（随便起）
- `origin/codex/...`：远程分支路径

**本质**："把远程那个分支复制一份到本地，取名 codex-review，然后切过去看。"

---

## 查看 Codex 改了什么

### `git diff` — 比较两个分支的差异

```powershell
git diff main..origin/codex/enhance-note.md-content-with-details -- notes.md
```

**参数解释**：
- `main..远程分支名`：比较 main 和这个分支的差异
- `-- notes.md`：只看这个文件（可省略，不加就看所有文件差异）

**输出解读**：

```
+这是 Codex 新增的内容               ← 绿色，+ 开头 = 新增
-这是 Codex 删除的内容               ← 红色，- 开头 = 删除
```

**出现 `(END)` 怎么办**：
这是 Git 在用分页器（less）显示长内容。**按 `q` 退出**。这不是报错。

---

## 合并 Codex 分支

### 完整流程

```powershell
# 第 1 步：切回 main
git checkout main

# 第 2 步：把 Codex 分支合并到 main
git merge origin/codex/enhance-note.md-content-with-details

# 第 3 步：上传到 GitHub
git push
```

**每步解释**：

1. **切回 main**：你要把东西合到 main，所以必须站在 main 上操作
2. **合并**：把 Codex 分支的改动"融入"到 main
3. **push**：合并发生在本地，GitHub 还不知道。必须 push 才能让远程 main 更新

---

## merge 是什么

**merge** = 合并。把两个分支的改动合到一起。

**可能的结果**：

| 结果 | 说明 |
|------|------|
| `Fast-forward` | 没有冲突，直接合入 |
| `Already up to date` | 远程分支没有新东西，已是最新 |
| 冲突 | 同一文件同一位置被两边都改了 |

---

## 合并冲突

### 什么时候会冲突

同一个文件的**同一行**被两个分支**同时修改**，Git 不知道该听谁的。

### 什么情况下**不会**冲突

- Codex 在文件末尾加了新内容，你在文件开头改了 → 不冲突（位置不同）
- Codex 新增了一个文件，你没碰它 → 不冲突
- **重复内容不等于冲突**。冲突是指"同一行两个版本不一样"。

### 冲突长什么样

```
<<<<<<< HEAD
这是 main 分支的内容（你当前的版本）
=======
这是 codex 分支的内容（AI 改的版本）
>>>>>>> origin/codex/xxx
```

**怎么处理**：
1. 不要乱删
2. 看清楚两段内容，决定保留哪一段
3. 手动删除标记（`<<<<<<<`、`=======`、`>>>>>>>`）
4. 保留你想要的内容
5. `git add` → `git commit`

### 如果不想现在处理

```powershell
git merge --abort
```

回到合并前的状态，一切恢复原样。

---

## 我的 AI 协作完整工作流

### 三种典型场景

**场景 A：OpenCode 改本地文件**

```
OpenCode 改完文件
    ↓
git status              ← 确认改了哪些文件
    ↓
git add .               ← 暂存
    ↓
git commit -m "..."     ← 存档
    ↓
git push                ← 同步到 GitHub
```

**场景 B：Codex 云端改了文件**

```
git pull                ← 拉取远程更新
```

**场景 C：Codex 创建了新分支**

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

## 记忆口诀

> **分支 = 平行世界，main = 真实世界。**
> **diff 是审查，merge 是批准。**
> **冲突不一定是坏事，重复不等于冲突。**
> **不满意就 `--abort`，满意就 merge + push。**

---

## 复习问题

1. `main` 和 `origin/main` 有什么区别？
2. Codex 为什么要创建新分支而不是直接改 main？
3. `git diff` 的输出里，绿色 `+` 和红色 `-` 分别代表什么？
4. 出现 `(END)` 时怎么办？
5. 合并分支的三步流程是什么？
6. "合并冲突"和"重复内容"有什么区别？
7. `git merge --abort` 什么时候用？
8. `git checkout -b 本地名 远程分支` 这条命令做了什么？
