# 01｜向量与矩阵：机器人空间计算的基础

## 学习目标

- 理解向量、矩阵和坐标表示。
- 掌握点积、叉积和矩阵乘法的含义。
- 理解为什么机器人学需要统一的数学表示。

## 1.1 向量

三维位置可以写成列向量：

$$
\mathbf{p} =
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
$$

其中 $x,y,z$ 表示点在某个指定坐标系中的坐标。必须说明坐标系，否则数字本身没有完整意义。

向量加法：

$$
\mathbf{a}+\mathbf{b} =
\begin{bmatrix}
a_x+b_x\\a_y+b_y\\a_z+b_z
\end{bmatrix}
$$

## 1.2 点积

两个向量的点积为：

$$
\mathbf{a}\cdot\mathbf{b}
= a_xb_x+a_yb_y+a_zb_z
= \|\mathbf{a}\|\|\mathbf{b}\|\cos\theta
$$

点积可以用于计算夹角、投影和方向相似性。若两个非零向量正交，则点积为零。

## 1.3 叉积

三维向量的叉积：

$$
\mathbf{a}\times\mathbf{b} =
\begin{bmatrix}
a_yb_z-a_zb_y\\
a_zb_x-a_xb_z\\
a_xb_y-a_yb_x
\end{bmatrix}
$$

结果向量垂直于两个输入向量张成的平面，方向由右手定则确定。机器人学中常用于表达旋转轴和力矩。

## 1.4 矩阵

矩阵可以表示线性变换。二维旋转矩阵：

$$
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
$$

对点 $\mathbf{p}$ 进行旋转：

$$
\mathbf{p}'=R(\theta)\mathbf{p}
$$

## 1.5 旋转矩阵的性质

$$
R^TR=I,\qquad \det(R)=1
$$

第一条表示旋转矩阵的列向量互相正交且长度为 1；第二条表示它是保持方向的纯旋转，而不是镜像变换。

## 1.6 练习

1. 计算 $[1,2,0]^T$ 与 $[2,1,0]^T$ 的点积。
2. 计算两个向量的叉积，并用右手定则检查方向。
3. 将点 $[1,0]^T$ 逆时针旋转 $90^\circ$，写出结果。
