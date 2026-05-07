# 002 - GitHub SSH 完整手册：让电脑和 GitHub 安全互相信任

> 面向零基础初学者。解释 SSH 是什么、为什么需要它、怎么配、配错了怎么办。

---

## SSH 是什么

### 一句话
SSH = Secure Shell（安全外壳协议）。它让两台电脑之间**加密通信**，在 GitHub 场景里，让我的电脑和 GitHub **安全互相信任，不用每次输密码**。

### 名字拆解
- **S**ecure = 安全
- **S**hell = 外壳（计算机术语，"操作系统的外壳"）

### 本质
SSH 是一套**钥匙系统**。你手里有一把私钥（证明你是谁），GitHub 有你的公钥（验证你真是你）。两把钥匙对上了，才能通信。

### SSH 不是什么
- 不是 Git（Git 管版本）
- 不是 GitHub（GitHub 管云端）
- SSH 只管**连接方式**

---

## 为什么我需要 SSH

### 我之前遇到的问题
```
Failed to connect to github.com port 443
Connection was reset
Recv failure
git push 一直失败
```

**根本原因**：HTTPS 走 443 端口，在中国大陆容易被墙/代理不稳定。

### HTTPS vs SSH

| | HTTPS | SSH |
|---|---|---|
| 地址格式 | `https://github.com/用户/仓库.git` | `git@github.com:用户/仓库.git` |
| 端口 | 443（容易被墙） | 22 |
| 认证 | Token / 密码 | 密钥对 |
| 需要每次输密码吗 | 是 | 否 |
| 稳定性 | 依赖网络质量 | 更稳定 |

---

## 公钥和私钥

### 用门禁卡类比

| 名称 | 文件名 | 放在哪 | 能公开吗 | 作用 |
|------|--------|--------|----------|------|
| 私钥 | `id_ed25519` | 你电脑里 | **绝对不能** | 证明"我就是我" |
| 公钥 | `id_ed25519.pub` | GitHub 上 | 可以公开 | 让别人验证"你真是你" |

### `.pub` 是什么意思
**pub** = public（公开的）。`.pub` 结尾的文件是公钥，可以复制粘贴给 GitHub。没有 `.pub` 的文件是私钥，绝对不能泄露。

### 为什么私钥不能泄露
任何人拿到你的私钥，就能冒充你 push 代码到你的仓库。所以：
- 不要复制私钥发微信
- 不要把 `.ssh` 文件夹上传到 GitHub
- 不要在任何地方展示私钥内容

---

## 全套操作命令

### `ssh-keygen -t ed25519 -C "注释"` — 生成钥匙对

**是什么**：生成一对 SSH 密钥（公钥+私钥）。

**名字含义**：
- **ssh-keygen** = SSH Key Generator（SSH 密钥生成器）
- **-t ed25519**：指定钥匙类型为 ed25519（目前最推荐）
- **-C "..."**：备注（comment），方便你以后识别这把钥匙

**基本写法**：
```powershell
ssh-keygen -t ed25519 -C "github-ssh-key"
```

**执行后会问什么**：
```
Enter file in which to save the key (C:\Users\16068/.ssh/id_ed25519):
```
→ 直接按回车（用默认路径）

```
Enter passphrase (empty for no passphrase):
```
→ 直接按回车（不设密码）

**正常输出**：
```
Your identification has been saved in C:\Users\16068\.ssh\id_ed25519
Your public key has been saved in C:\Users\16068\.ssh\id_ed25519.pub
```

**常见错误**：
- `No such file or directory` → `.ssh` 文件夹不存在。先手动创建 `mkdir %USERPROFILE%\.ssh`
- 已存在同名 key → 提示是否覆盖，小心选择

---

### `notepad $env:USERPROFILE\.ssh\id_ed25519.pub` — 查看公钥

**是什么**：用记事本打开公钥文件，方便复制内容。

**基本写法**：
```powershell
notepad $env:USERPROFILE\.ssh\id_ed25519.pub
```

- `$env:USERPROFILE`：PowerShell 变量，指向 `C:\Users\你的用户名`
- 也可以用 `cat ~/.ssh/id_ed25519.pub` 在终端直接显示

**复制后去哪**：
1. 打开 https://github.com/settings/keys
2. 点 **New SSH Key**
3. Title 随便填（如 `my-windows-pc`）
4. Key 里粘贴公钥（整个一行，包括 `ssh-ed25519` 开头）
5. 点 **Add SSH Key**

---

### `ssh -T git@github.com` — 测试 SSH 连接

**是什么**：测试你的电脑能不能通过 SSH 连接到 GitHub。

**名字含义**：
- **ssh**：使用 SSH 协议
- **-T**：禁止分配终端（GitHub 不支持你登录进去操作，只是测试连接）
- **git@github.com**：用 git 用户身份连接 github.com

**基本写法**：
```powershell
ssh -T git@github.com
```

**成功输出**：
```
Hi 332165832trump-gif! You've successfully authenticated, but GitHub does not provide shell access.
```

**人话翻译**：认证成功！"does not provide shell access" 不是错误——GitHub 不让你像登录服务器一样进去敲命令，只允许 push/pull。**这是正常的。**

**常见错误**：

| 错误 | 原因 | 解决 |
|------|------|------|
| `Permission denied (publickey)` | GitHub 没识别到你的公钥 | 检查是否生成 key、公钥是否粘贴到 GitHub |
| `Could not resolve hostname github.com` | DNS 问题 | 换 DNS 或检查网络 |
| `Connection timed out` | 网络不通 | 开代理/换网络/开 TUN 模式 |
| `Host key verification failed` | 第一次连接，系统问你是否信任 | 输入 `yes` 确认 |

---

### `git remote set-url origin git@github.com:用户/仓库.git` — 切到 SSH

**是什么**：把仓库的远程地址从 HTTPS 格式改成 SSH 格式。

**什么时候用**：配好 SSH Key 之后，把现有仓库从 HTTPS 切到 SSH。

**基本写法**（我的仓库为例）：
```powershell
git remote set-url origin git@github.com:332165832trump-gif/ai-learning.git
```

**验证**：
```powershell
git remote -v
```

**改前**：
```
origin  https://github.com/332165832trump-gif/ai-learning.git
```

**改后**：
```
origin  git@github.com:332165832trump-gif/ai-learning.git
```

**地址格式区别**：
- HTTPS：`https://github.com/用户名/仓库名.git`
- SSH：`git@github.com:用户名/仓库名.git`（**冒号**不是斜杠）

---

## Git、GitHub、SSH 的关系图

```
        你电脑                 互联网               GitHub
    ┌──────────┐                               ┌──────────┐
    │  Git     │ ←── SSH 加密通道 ──────────→  │  GitHub  │
    │ (管版本)  │                               │ (管云端)  │
    │          │     HTTPS/SSH                 │          │
    │  add     │     push ───────────────→     │  接收    │
    │  commit  │     pull ←───────────────     │  存储    │
    └──────────┘                               └──────────┘
```

- **Git**：管理你本地的代码版本（add、commit）
- **GitHub**：存储代码的云端服务器
- **SSH**：Git 和 GitHub 之间的**安全通信管道**

---

## SSH 和 push/pull 的关系

| 操作 | 需要连 GitHub 吗 | 会用到 SSH 吗 |
|------|------------------|---------------|
| `git add` | 不需要 | 不需要 |
| `git commit` | 不需要 | 不需要 |
| `git status` | 不需要 | 不需要 |
| `git push` | **需要** | **会** |
| `git pull` | **需要** | **会** |
| `git clone` | **需要** | **会** |

**核心认知**：只有`push`/`pull`/`clone`这类"和远程通信"的操作才走 SSH。本地操作（add/commit/status）完全不需要。

---

## 记忆口诀

> **公钥给 GitHub，私钥留电脑。**
> **Git 管版本，SSH 管连接。**
> **add/commit 本地，push/pull 连云端。**
> **`ssh -T` 是体检，`git remote set-url` 是换通道。**

---

## 复习问题

1. SSH 的全称是什么？每个字母代表什么？
2. 公钥和私钥的区别是什么？哪个能公开？
3. `.pub` 是什么意思？
4. HTTPS 和 SSH 的地址格式有什么不同？
5. `ssh -T git@github.com` 成功后显示什么？为什么有"does not provide shell access"？
6. `git remote set-url` 什么时候用？
7. `git add` 和 `git commit` 需要 SSH 吗？为什么？
8. `Permission denied (publickey)` 怎么排查？
