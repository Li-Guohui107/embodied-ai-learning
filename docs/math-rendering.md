# 数学公式显示规范

本教程统一使用 GitHub 原生支持的 LaTeX 定界符。无论是在 GitHub 仓库页面查看 Markdown，还是通过 MkDocs Material 构建教程网站，都使用同一套源文件写法。

## 1. 行内公式

使用单个美元符号包围公式：

```markdown
机械臂连杆长度记为 $L_1$ 和 $L_2$，关节角记为 $\theta_1$ 和 $\theta_2$。
```

显示效果示例：

机械臂连杆长度记为 $L_1$ 和 $L_2$，关节角记为 $\theta_1$ 和 $\theta_2$。

## 2. 独立公式

使用两个美元符号包围公式，并让公式单独占据段落：

```markdown
$$
x = L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2)
$$
```

显示效果示例：

$$
x = L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2)
$$

## 3. 多行公式与矩阵

```markdown
$$
\begin{aligned}
x &= L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) \\
y &= L_1\sin\theta_1 + L_2\sin(\theta_1+\theta_2)
\end{aligned}
$$
```

矩阵示例：

$$
\mathbf{p} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

## 4. 为什么 GitHub 之前显示成原始代码？

GitHub 仓库页面不会读取本项目的 `mkdocs.yml` 或 `mathjax.js` 来渲染 README 和普通 Markdown 文件。GitHub 文档页面支持 `$...$` 行内公式与 `$$...$$` 独立公式，因此教程源文件统一改用这两种格式。

## 5. MkDocs 网站如何继续渲染？

MkDocs 配置保留 `pymdownx.arithmatex` 的 `generic: true`。Arithmatex 会识别 Markdown 中的美元符号公式，并转换为 MathJax 可处理的数学标记；MathJax 配置负责在教程网站中排版公式。

因此，**不要在新章节中混用多套定界符**，统一写：

- 行内公式：`$...$`
- 独立公式：`$$...$$`

## 6. 公式编写检查清单

- [ ] 行内公式使用一对 `$`。
- [ ] 独立公式使用一对 `$$`，且前后留空行。
- [ ] 多行公式使用 `\\` 换行。
- [ ] 矩阵每一行使用 `&` 分列、`\\` 换行。
- [ ] 公式中的变量首次出现时解释含义和单位。
- [ ] 不要把需要渲染的公式放进普通代码块；代码块只用于展示公式源码。
- [ ] 提交前在 GitHub 页面检查公式是否正常显示。
