# 009 - 错误与 Debug 手册

> 整理所有遇到和可能遇到的错误。每个错误按「报错长什么样→人话翻译→为什么发生→怎么解决→怎么避免→和项目的关系」组织。

---

## Git 错误

### 1. `src refspec main does not match any`

**报错信息**：
```
error: src refspec main does not match any
```

**人话翻译**：Git 找不到叫 `main` 的分支，因为你还没做过任何 commit。

**为什么发生**：`git push` 之前没有 `git commit`。没有 commit，就没有分支历史，`main` 分支还不存在。

**怎么解决**：
```powershell
git add .
git commit -m "first commit"
git push -u origin main
```

**怎么避免**：记住顺序：add → commit → push。少一步都不行。

### 2. `Author identity unknown`

**报错信息**：
```
Author identity unknown
```

**人话翻译**：Git 不知道你是谁，没法在 commit 记录里署名。

**为什么发生**：没有配置 `git config --global user.name` 和 `user.email`。

**怎么解决**：
```powershell
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
```

**怎么避免**：装完 Git 就配好，只配一次，终身受用。

### 3. `nothing to commit, working tree clean`

**报错信息**：
```
nothing to commit, working tree clean
```

**人话翻译**：没有新改动需要存档，一切干净。**这不是报错，是正常状态。**

**为什么出现**：当前所有文件都已经被 Git 记录过了，没有修改、没有新文件。

### 4. `Everything up-to-date`

**报错信息**：
```
Everything up-to-date
```

**人话翻译**：没有新的本地 commit 需要 push。**不是报错，但要注意。**

**注意**：这不代表 GitHub 上一定有你想要的内容。它只看 commit 记录，不看工作区文件。如果你改了文件但没 `add` + `commit`，这条提示照样出现。

### 5. `Failed to connect to github.com port 443`

**报错信息**：
```
fatal: unable to access 'https://github.com/.../': Failed to connect to github.com port 443
```

**人话翻译**：网络连不上 GitHub。

**常见原因**：
- 没开代理/VPN
- 防火墙拦截
- GitHub 暂时不可达

**解决**：
- 开 Clash/V2Ray，确认全局模式
- 或配置 SSH 替代 HTTPS（见 002 号笔记）
- 换手机热点测试

### 6. `Your branch is ahead of origin/main by 1 commit`

**人话翻译**：你的本地比 GitHub 多了一个 commit，还没 push。

**不是报错**，是提醒。跑 `git push` 就好。

---

## Python 错误

### 7. `SyntaxError`

**报错信息**：
```
SyntaxError: invalid syntax
```

**人话翻译**：Python 看不懂你写的代码，语法有问题。

**常见原因**：
- 忘了写冒号 `:`
- `elif` 写成了 `else if`
- 括号没配对
- 字符串引号没配对

**怎么解决**：看错误信息指的那一行和上一行，检查语法。

### 8. `IndentationError`

**报错信息**：
```
IndentationError: expected an indented block
```

**人话翻译**：该缩进的地方没缩进。

**为什么发生**：
- `for`、`if`、`elif`、`else` 后面必须跟缩进的代码
- 你写了冒号但下一行没缩进

**怎么解决**：在冒号下一行加 4 个空格。

**怎么避免**：写完冒号按回车，编辑器自动缩进。不要删那个缩进。

### 9. `NameError`

**报错信息**：
```
NameError: name 'listdir' is not defined
```

**人话翻译**：Python 不认识你写的这个名字。

**为什么发生**：
- `import os` 之后写 `listdir()` 而不是 `os.listdir()`
- 变量名拼错（`name` vs `Name`）
- 用了没定义的变量

**怎么解决**：检查拼写，检查是否忘了 `import`，检查是否忘了前缀（`os.`）。

### 10. `FileNotFoundError`

**报错信息**：
```
FileNotFoundError: [WinError 2] 系统找不到指定的文件
```

**人话翻译**：你指定的路径对应的文件不存在。

**为什么发生**：
- 路径拼错了
- 文件已被移走或删除
- `file` 只有文件名，被当成完整路径传递了

**怎么解决**：`print(path)`、`print(old_path)` 检查路径。

### 11. `PermissionError`

**报错信息**：
```
PermissionError: [WinError 5] 拒绝访问
```

**人话翻译**：你没有权限操作这个文件。

**为什么发生**：
- 文件正在被 Excel/Word/编辑器打开
- 操作系统保护目录（C 盘系统文件夹）

**怎么解决**：关掉占用文件的程序；不要在系统目录测试。

### 12. `FileExistsError`

**报错信息**：
```
FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件
```

**人话翻译**：你要创建的文件夹或文件已经存在了。

**为什么发生**：
- 没有加 `exist_ok=True`
- `os.rename` 的目标路径已有同名文件

**怎么解决**：创建文件夹加 `exist_ok=True`；移动文件前检查目标是否已有同名文件。

### 13. Windows 路径转义 `SyntaxError`

**报错信息**：
```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
```

**为什么发生**：字符串里的 `\U` 被当成 Unicode 转义。

**解决**：用正斜杠 `/`、双反斜杠 `\\` 或原始字符串 `r"..."`。

---

## SSH 错误

### 14. `Permission denied (publickey)`

**报错信息**：
```
Permission denied (publickey)
```

**人话翻译**：GitHub 不认识你的公钥。

**排查步骤**：
1. 生成 key 了吗？→ `ssh-keygen -t ed25519`
2. 公钥复制到 GitHub 了吗？→ https://github.com/settings/keys
3. 用的是哪个 key？→ 检查 `~/.ssh/` 下的文件

### 15. `Connection timed out`

**报错信息**：
```
ssh: connect to host github.com port 22: Connection timed out
```

**人话翻译**：连不上 GitHub，超时了。

**解决**：开代理（TUN 模式）、换网络、检查防火墙。

### 16. `Host key verification failed`

**报错信息**：
```
Host key verification failed
```

**人话翻译**：第一次连接 GitHub，系统问你是否信任。

**解决**：输入 `yes` 确认即可。或删除 `~/.ssh/known_hosts` 中 github.com 那一行。

---

## Debug 通用方法论

1. **读报错最后一行**：上面都是"调用栈"，最后一行才是真正错误类型
2. **print 大法**：任何不确定的值，`print()` 出来看
3. **先缩小范围**：注释掉一半代码，定位到哪一行出错
4. **搜索报错信息**：把错误类型复制到搜索框
5. **回退到上一个能跑的版本**：有 Git 的好处就在这里

---

## 复习问题

1. `nothing to commit` 和 `Everything up-to-date` 分别是什么意思？哪个是报错？
2. `src refspec main does not match any` 怎么解决？
3. `NameError: name 'listdir' is not defined` 缺了什么？
4. `FileNotFoundError` 怎么排查？
5. `Permission denied (publickey)` 的三步排查是什么？
6. Windows 路径 `"C:\test"` 为什么可能报错？三种正确写法是什么？
