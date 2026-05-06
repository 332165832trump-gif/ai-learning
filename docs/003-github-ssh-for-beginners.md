# 003 - GitHub SSH 入门

## 1. 我为什么学 SSH

之前我遇到过这些问题：

- `git push` 失败：`Failed to connect to github.com port 443`
- `git pull` 失败：`Connection was reset`
- HTTPS 连接不稳定，每次 push 可能因为网络波动中断
- 本地改完代码，GitHub 云端就是收不到

这不是 Git 出了问题，是**连接 GitHub 的方式**出了问题。

## 2. SSH 是什么

**一句话**：SSH = 让我的电脑和 GitHub 安全互相信任的一套钥匙系统。

- SSH = Secure Shell（安全外壳协议）
- 它让两台电脑之间**加密通信**
- 在 GitHub 场景里，配好之后不用每次输密码
- 它不是 Git，也不是 GitHub，只是**连接方式**

## 3. Git、GitHub、SSH 的关系

| 工具 | 管什么 | 用在哪 |
|------|--------|--------|
| Git | 版本管理 | 本地 |
| GitHub | 代码托管 | 云端 |
| SSH | 连接认证 | 本地→云端之间的通道 |

**一句话记住**：Git 管版本，GitHub 管云端，SSH 管连接。

## 4. 公钥和私钥

**用门禁卡类比**：

| 名称 | 文件名 | 放在哪 | 能公开吗 | 作用 |
|------|--------|--------|----------|------|
| 私钥 | `id_ed25519` | 你电脑里 | **绝对不能** | 证明"我是我" |
| 公钥 | `id_ed25519.pub` | GitHub 上 | 可以 | 验证"你真是你" |

- `.pub` 结尾 → 公钥 → 复制到 GitHub
- 没有 `.pub` → 私钥 → **绝对不能泄露，不要复制，不要发微信**

> 类比：公钥 = 小区门禁登记表（物业那里谁都能查），私钥 = 你手里的门禁卡（自己保管）。

## 5. HTTPS 和 SSH 的区别

| | HTTPS | SSH |
|---|---|---|
| 地址格式 | `https://github.com/用户/仓库.git` | `git@github.com:用户/仓库.git` |
| 端口 | 443（易被墙） | 22 |
| 认证方式 | Token / 密码 | 密钥对 |
| 每次需要输入密码吗 | 是（或缓存） | 否 |
| 稳定性 | 依赖网络 | 更稳定 |

## 6. 生成 SSH Key

```powershell
ssh-keygen -t ed25519 -C "github-ssh-key"
```

- `-t ed25519`：钥匙类型（目前最推荐的）
- `-C "..."`：备注，方便你以后识别这把钥匙
- 生成的钥匙在 `C:\Users\你的用户名\.ssh\` 下

## 7. 复制公钥到 GitHub

```powershell
notepad $env:USERPROFILE\.ssh\id_ed25519.pub
```

复制全部内容，然后：
1. 打开 https://github.com/settings/keys
2. 点 **New SSH Key**
3. Title 随便填（如 `my-windows-pc`）
4. Key 里粘贴公钥
5. 点 **Add SSH Key**

## 8. 测试 SSH 是否连通

```powershell
ssh -T git@github.com
```

成功时显示：

```
Hi 你的用户名! You've successfully authenticated, but GitHub does not provide shell access.
```

**这句话的意思**：认证成功！"does not provide shell access" 不是错误——GitHub 不让你像登录服务器一样操作它，只能用来 push/pull，正常。

## 9. 把仓库从 HTTPS 改成 SSH

```powershell
# 查看当前用什么
git remote -v

# 改成 SSH
git remote set-url origin git@github.com:你的用户名/仓库名.git

# 验证
git remote -v
```

示例（我的仓库）：
```powershell
git remote set-url origin git@github.com:332165832trump-gif/ai-learning.git
```

## 10. SSH 常见错误

### 10.1 `Permission denied (publickey)`

- **原因**：GitHub 没识别到你的公钥
- **排查**：生成了 key 吗？公钥复制到 GitHub 了吗？用的是对的 key 吗？

### 10.2 `Could not resolve hostname github.com`

- **原因**：DNS 问题，电脑找不到 github.com 的 IP
- **解决**：检查网络，换 DNS 为 `114.114.114.114`

### 10.3 `Connection timed out`

- **原因**：网络不通、代理没开、防火墙拦截
- **解决**：开代理，换网络，检查防火墙

### 10.4 `Host key verification failed`

- **原因**：第一次连接 GitHub，系统问你是否信任
- **解决**：输入 `yes` 确认即可

## 11. 记忆口诀

> **公钥给 GitHub，私钥留电脑。**
> **Git 管版本，SSH 管连接。**
> **add / commit 是本地，push / pull 才连云端。**
