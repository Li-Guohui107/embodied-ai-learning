# 项目 01｜二自由度平面机械臂

## 目标

实现平面二连杆机械臂的正运动学和解析逆运动学，并通过单元测试验证两者的一致性。

## 数学模型

$$
x=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

## 运行

```bash
python examples/planar_2dof_arm/kinematics.py
python -m unittest discover -s examples/planar_2dof_arm -p "test_*.py"
```

## 实验任务

1. 修改连杆长度。
2. 改变两个关节角，观察末端位置。
3. 尝试肘上和肘下两个逆解分支。
4. 输入不可达目标，观察错误处理。
5. 为关节添加限位检查。

## 验收标准

- 能够解释 FK 与 IK 的输入输出。
- 对可达目标，FK 与 IK 结果能够在数值容差内互相验证。
- 对不可达目标，程序明确报错。
- 实验记录包含连杆长度、角度单位和目标坐标。

## 安全边界

当前示例仅进行数学计算，不连接真实机械臂。
