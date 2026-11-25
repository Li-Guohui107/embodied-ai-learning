# 04｜雅可比矩阵（Jacobian）

## 4.1 为什么需要雅可比矩阵？

正运动学描述关节位置如何决定末端位置。雅可比矩阵进一步描述关节速度的小变化如何映射为末端速度。

对于关节变量 $\mathbf{q}$ 和末端位置 $\mathbf{x}=f(\mathbf{q})$，对时间求导：

$$
\dot{\mathbf{x}}=J(\mathbf{q})\dot{\mathbf{q}}
$$

其中：

$$
J(\mathbf{q})=\frac{\partial f}{\partial\mathbf{q}}
$$

称为雅可比矩阵。

## 4.2 二自由度平面机械臂

正运动学：

$$
x=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

对关节角求偏导：

$$
J=
\begin{bmatrix}
-L_1\sin\theta_1-L_2\sin(\theta_1+\theta_2)&-L_2\sin(\theta_1+\theta_2)\\
L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)&L_2\cos(\theta_1+\theta_2)
\end{bmatrix}
$$

因此：

$$
\begin{bmatrix}\dot{x}\\\dot{y}\end{bmatrix}
=
J
\begin{bmatrix}\dot{\theta}_1\\\dot{\theta}_2\end{bmatrix}
$$

## 4.3 奇异位形

当雅可比矩阵秩下降时，机器人可能失去某些方向上的瞬时运动能力，这称为奇异性。

对于平面二连杆机械臂：

$$
\det(J)=L_1L_2\sin\theta_2
$$

当 $\theta_2=0$ 或 $\theta_2=\pi$ 时，行列式为零，两个连杆共线，系统处于奇异位形。

## 4.4 应用

- 末端速度控制
- 速度逆解
- 奇异性分析
- 力与关节力矩映射
- 基于梯度的运动优化

## 4.5 练习

推导雅可比矩阵，并在 $\theta_2=0$ 时分析机械臂能够和不能够产生哪些末端瞬时运动。
