# 02｜正运动学（Forward Kinematics）

## 学习目标

- 理解正运动学解决的问题。
- 推导平面二自由度机械臂末端位置。
- 理解从单个关节变换到整条运动链的过程。
- 运行配套 Python 示例。

## 2.1 定义

正运动学（FK）根据机器人关节变量和已知几何参数，计算末端执行器相对于指定参考系的位置和姿态。输入通常是关节角或关节位移，输出是末端位姿。

## 2.2 平面二自由度机械臂

考虑由两段刚性连杆组成的平面机械臂：

- 第一段连杆长度：$$L_1$$
- 第二段连杆长度：$L_2$
- 第一关节角：$\theta_1$
- 第二关节相对角：$\theta_2$

约定两个角均以逆时针为正，第二关节角相对于第一段连杆方向定义。

## 2.3 末端位置推导

第一段连杆末端位置：

$$
x_1=L_1\cos\theta_1
$$

$$
y_1=L_1\sin\theta_1
$$

第二段连杆相对于世界坐标系的绝对方向为：

$$
\theta_1+\theta_2
$$

第二段连杆贡献的位置：

$$
x_2=L_2\cos(\theta_1+\theta_2)
$$

$$
y_2=L_2\sin(\theta_1+\theta_2)
$$

将两段连杆的位置相加，得到末端位置：

$$
\boxed{
x=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
}
$$

$$
\boxed{
y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
}
$$

末端平面朝向为：

$$
\phi=\theta_1+\theta_2
$$

## 2.4 齐次变换推导

第一关节到第一连杆末端的变换：

$$
{}^0T_1=
\begin{bmatrix}
\cos\theta_1&-\sin\theta_1&L_1\cos\theta_1\\
\sin\theta_1&\cos\theta_1&L_1\sin\theta_1\\
0&0&1
\end{bmatrix}
$$

第二段连杆变换：

$$
{}^1T_2=
\begin{bmatrix}
\cos\theta_2&-\sin\theta_2&L_2\cos\theta_2\\
\sin\theta_2&\cos\theta_2&L_2\sin\theta_2\\
0&0&1
\end{bmatrix}
$$

总变换：

$$
{}^0T_2={}^0T_1{}^1T_2
$$

展开后，平移部分正是前面得到的末端位置公式。

## 2.5 数值示例

设：

$$
L_1=1.0\text{ m},\quad L_2=0.8\text{ m}
$$

$$
\theta_1=30^\circ,\quad \theta_2=60^\circ
$$

则：

$$
x=1.0\cos30^\circ+0.8\cos90^\circ
\approx0.8660\text{ m}
$$

$$
y=1.0\sin30^\circ+0.8\sin90^\circ
=1.3000\text{ m}
$$

## 2.6 Python 实验

```bash
python examples/planar_2dof_arm/kinematics.py
```

程序会计算末端位置，并将结果输入逆运动学，再通过正运动学检查恢复的位置是否一致。

## 2.7 常见错误

- 将角度制直接传给 `sin()` / `cos()`，而 Python 数学函数默认使用弧度。
- 将第二关节角误认为相对于世界坐标系的绝对角。
- 连杆长度单位不统一。
- 坐标系原点或正方向定义不一致。

## 2.8 练习

1. 将 $\theta_1$ 改为 $0^\circ$，观察末端位置。
2. 将 $\theta_2$ 改为 $0^\circ$，解释为什么两段连杆共线。
3. 修改连杆长度，比较工作空间。
4. 推导一个三自由度平面机械臂的末端位置表达式。
