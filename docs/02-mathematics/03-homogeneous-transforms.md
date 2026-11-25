# 03｜齐次变换矩阵

## 学习目标

理解齐次坐标如何将旋转和平移统一到一个矩阵中，并能解释变换矩阵的组成。

## 3.1 二维刚体变换

二维点：

$$
\mathbf{p}=
\begin{bmatrix}x\\y\end{bmatrix}
$$

旋转和平移：

$$
\mathbf{p}'=R(\theta)\mathbf{p}+\mathbf{t}
$$

其中：

$$
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix},
\qquad
\mathbf{t}=
\begin{bmatrix}t_x\\t_y\end{bmatrix}
$$

## 3.2 引入齐次坐标

将二维点扩展为三维齐次向量：

$$
\tilde{\mathbf{p}}=
\begin{bmatrix}x\\y\\1\end{bmatrix}
$$

定义齐次变换矩阵：

$$
T=
\begin{bmatrix}
\cos\theta&-\sin\theta&t_x\\
\sin\theta&\cos\theta&t_y\\
0&0&1
\end{bmatrix}
$$

于是：

$$
\tilde{\mathbf{p}}'=T\tilde{\mathbf{p}}
$$

旋转和平移被统一成一次矩阵乘法。

## 3.3 三维齐次变换

$$
T=
\begin{bmatrix}
R&\mathbf{t}\\
\mathbf{0}^T&1
\end{bmatrix}
=
\begin{bmatrix}
r_{11}&r_{12}&r_{13}&t_x\\
r_{21}&r_{22}&r_{23}&t_y\\
r_{31}&r_{32}&r_{33}&t_z\\
0&0&0&1
\end{bmatrix}
$$

其中 $R\in SO(3)$ 是旋转矩阵，$\mathbf{t}\in\mathbb{R}^3$ 是平移向量。

## 3.4 变换组合

若先从坐标系 C 变换到 B，再从 B 变换到 A：

$$
{}^A T_C={}^A T_B\,{}^B T_C
$$

矩阵乘法通常不可交换：

$$
T_1T_2\ne T_2T_1
$$

所以变换顺序非常重要。

## 3.5 求逆

对于刚体变换：

$$
T^{-1}=
\begin{bmatrix}
R^T&-R^T\mathbf{t}\\
0&1
\end{bmatrix}
$$

因为旋转矩阵满足 $R^{-1}=R^T$。

## 3.6 数值示例

点 $(1,0)$ 逆时针旋转 $90^\circ$，再平移 $(2,3)$：

$$
T=
\begin{bmatrix}
0&-1&2\\
1&0&3\\
0&0&1
\end{bmatrix}
$$

$$
\begin{bmatrix}x'\\y'\\1\end{bmatrix}
=
\begin{bmatrix}
0&-1&2\\
1&0&3\\
0&0&1
\end{bmatrix}
\begin{bmatrix}1\\0\\1\end{bmatrix}
=
\begin{bmatrix}2\\4\\1\end{bmatrix}
$$

## 3.7 练习

1. 将旋转角改为 $180^\circ$，重新计算。
2. 比较“先旋转再平移”和“先平移再旋转”的结果。
3. 推导上述齐次变换的逆矩阵。
