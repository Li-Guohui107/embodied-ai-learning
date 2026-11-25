# 平面二自由度机械臂

运行：

```bash
python examples/planar_2dof_arm/kinematics.py
python -m unittest discover -s examples/planar_2dof_arm -p "test_*.py"
```

角度单位为弧度，长度单位由调用者统一（示例默认米）。逆运动学提供两个肘部构型分支。该示例不处理关节限位和碰撞约束。
