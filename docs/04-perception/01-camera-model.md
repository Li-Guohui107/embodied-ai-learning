# 01｜相机模型与标定

## 1.1 针孔相机模型

相机将三维空间点投影到二维图像平面。设相机坐标系中的点为：

$$
\mathbf{P}_c=
\begin{bmatrix}X_c\\Y_c\\Z_c\end{bmatrix}
$$

忽略畸变时，像素坐标近似满足：

$$
u=f_x\frac{X_c}{Z_c}+c_x
$$

$$
v=f_y\frac{Y_c}{Z_c}+c_y
$$

其中 $f_x,f_y$ 是以像素为单位的焦距，$c_x,c_y$ 是主点坐标。

## 1.2 相机内参矩阵

$$
K=
\begin{bmatrix}
f_x&0&c_x\\
0&f_y&c_y\\
0&0&1
\end{bmatrix}
$$

在齐次像素坐标下：

$$
Z_c
\begin{bmatrix}u\\v\\1\end{bmatrix}
=
K
\begin{bmatrix}X_c\\Y_c\\Z_c\end{bmatrix}
$$

## 1.3 外参

外参描述相机坐标系相对于世界或机器人坐标系的姿态：

$$
{}^W T_C=
\begin{bmatrix}
{}^W R_C&{}^W\mathbf{t}_C\\
0&1
\end{bmatrix}
$$

相机内参描述相机成像几何，外参描述相机在外部参考系中的位置和姿态。两者不能混淆。

## 1.4 畸变

真实镜头可能存在径向和切向畸变。标定过程估计内参和畸变系数，并用于图像去畸变。

## 1.5 练习

查阅一台相机的标定文件，识别焦距、主点、畸变参数和外参，并说明这些参数分别用于哪一步计算。
