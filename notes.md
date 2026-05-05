# Python 学习笔记

## 1. Windows 路径 + Python 字符串 = SyntaxError

### 我遇到的问题
在 Python 字符串里写 Windows 文件路径（比如 `"C:\Users\..."`），运行时报错。

### 报错信息
```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
```

### 错误原因
反斜杠 `\` 是 Python 字符串的**转义字符**开头。比如 `\n` 是换行，`\t` 是 Tab。路径里的 `\U` 被 Python 当成"Unicode 转义"（`\Uxxxxxxxx`），后面接的不是 8 位十六进制数字，于是报错。

### 正确写法（3 选 1）

```python
# 方法 1：用正斜杠（最推荐）
path = "C:/Users/16068/桌面"

# 方法 2：双反斜杠
path = "C:\\Users\\16068\\桌面"

# 方法 3：原始字符串
path = r"C:\Users\16068\桌面"
```

### 我自己的理解
Python 看到 `\` 就想"这是个特殊符号"，不会把它当普通斜杠。所以要么告诉 Python "这真的是普通反斜杠"（双写 `\\`），要么告诉它"这段话别转义"（`r"..."`），要么干脆换成正斜杠 `/`——Windows 也认。

### 下次如何避免
- 在 Python 代码里写 Windows 路径，**一律用正斜杠 `/`**，一劳永逸。
- 或者从 `input()` 接收路径——用户输入的路径 Python 不会转义，天然安全。
