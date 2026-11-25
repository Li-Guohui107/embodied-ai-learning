# 开始学习

## 1. 前置知识

不要求一开始全部掌握，但建议逐步补齐：

| 知识 | 建议掌握内容 | 在本课程中的用途 |
|---|---|---|
| Python | 函数、列表、模块、类、虚拟环境 | 编写实验与工具 |
| 线性代数 | 向量、矩阵、矩阵乘法 | 坐标变换与运动学 |
| 三角函数 | 正弦、余弦、反三角函数 | 机械臂运动学 |
| 微积分 | 导数、偏导数、链式法则 | 雅可比与优化 |
| 概率基础 | 均值、方差、概率分布 | 传感器噪声与学习 |
| Linux | 终端、文件、进程 | ROS 2 开发 |

## 2. 推荐环境

- Python 3.10 或更新版本
- Git
- VS Code
- 一个 Python 虚拟环境

创建环境：

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## 3. 第一次运行

```bash
python examples/planar_2dof_arm/kinematics.py
python -m unittest discover -s examples/planar_2dof_arm -p "test_*.py"
python examples/agent_loop/simple_agent.py
```

## 4. 视觉实验（可选）

需要摄像头以及 OpenCV：

```bash
pip install -r requirements-vision.txt
python examples/vision_color_tracking/color_tracker.py --camera 0
```

## 5. 学习记录模板

```text
本章主题：
学习目标：
关键概念：
公式与变量定义：
运行环境：
实验步骤：
实验结果：
误差 / 失败分析：
仍未解决的问题：
```
