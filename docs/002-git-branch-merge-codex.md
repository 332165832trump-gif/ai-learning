# 002 - Git 分支、合并与 Codex 工作流

## 1. branch 是什么

**用比喻理解**：分支就像**平行世界**。

- `main`：真实世界（正式版本），你电脑上稳定可用的代码
- `codex/xxx`：平行世界（AI 做的实验），AI 在一个独立空间里改代码

你在平行世界里随便折腾，不影响真实世界。实验成功了就"合并"（merge）回来，失败了就删掉。

**本质**：分支 = Git 里的一个指针，指向某条 commit 时间线上的最新节点。不同分支可以指向不同节点，各自发展。

## 2. 为什么 Codex 会创建新分支

AI 不应该直接改你的正式版本。万一改错了怎么办？

所以 Codex/OpenCode 的默认行为是：**在新分支里改代码，让你审核后再合并**。这和你自己先在"副本"里改、确认无误再覆盖原文件是同一个道理。

## 3. 查看分支

```powershell
git branch        # 只看本地分支，当前分支前有 *
git branch -a     # 看本地 + 远程所有分支
```

**输出示例解读**：

```
* main                                    ← 你当前在 main（前面有 *）
  remotes/origin/main                     ← GitHub 上的 main
  remotes/origin/codex/enhance-note...    ← Codex 创建的分支
```

## 4. 切换分支

```powershell
git checkout main    # 回到 main 分支
```

## 5. 从远程分支创建本地副本

```powershell
git checkout -b codex-review origin/codex/enhance-note.md-content-with-details
```

- **`-b`**：创建新分支并切过去
- **`codex-review`**：你起的本地分支名
- **`origin/codex/...`**：远程分支路径

这句话的意思是："把远程那个分支复制一份到本地，取名 codex-review，然后切过去。"

## 6. 查看 Codex 改了什么

```powershell
git diff main..origin/codex/enhance-note.md-content-with-details -- notes.md
```

- **`git diff A..B`**：比较两个分支的差异
- **`-- notes.md`**：只看这个文件（可省略，看所有文件）
- **输出颜色**：
  - 绿色 `+` → 新增的内容
  - 红色 `-` → 删除的内容
- **出现 `(END)` 时按 `q` 退出**：这不是报错，是分页器，按 `q` 退出。

## 7. 合并 Codex 分支到 main

```powershell
git checkout main                                              # 1. 切回 main
git merge origin/codex/enhance-note.md-content-with-details    # 2. 合并分支
git push                                                       # 3. 上传到 GitHub
```

**每步解释**：

1. **切回 main**：你要把东西合到 main，必须站在 main 上。
2. **合并**：把 Codex 分支的改动"融入"到 main。如果有新东西就加，没变化就提示 `Already up to date.`
3. **push**：合并发生在本地，GitHub 还不知道。必须 push 才能让远程更新。

## 8. 合并冲突是什么

**什么情况下会冲突**：同一个文件的**同一行**被两个分支**同时修改**。

**不冲突的情况**：
- Codex 在末尾加了新内容，你在开头改了 → 不冲突（位置不同）
- Codex 新增了一个新文件，你没碰 → 不冲突

**冲突长这样**：

```
<<<<<<< HEAD
这是 main 分支的内容
=======
这是 codex 分支的内容
>>>>>>> origin/codex/xxx
```

- `<<<<<<< HEAD` ~ `=======`：你当前分支（main）的内容
- `=======` ~ `>>>>>>> xxx`：对方分支的内容
- 你需要手动删掉标记，**保留你想要的那一段**

## 9. 出问题如何撤销

```powershell
git merge --abort
```

回到合并前的状态，一切恢复原样。

## 10. 我的 AI 协作工作流

```
ChatGPT  → 规划方案、解释概念、纠正错误
    ↓
OpenCode → 本地写代码、改文件、运行项目
    ↓
Codex    → 云端创建分支、修改文件
    ↓
Git      → 记录版本、审核差异
    ↓
GitHub   → 保存和展示学习轨迹
```

**三种典型场景**：

| 场景 | 流程 |
|---|---|
| OpenCode 改本地文件 | `git status` → `add` → `commit` → `push` |
| Codex 改云端文件 | `git pull` |
| Codex 创建新分支 | 查看分支 → `git diff` 看差异 → `checkout main` → `merge` → `push` |
