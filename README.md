<div align="center">

# 🤖 具身智能系统学习教程
### Embodied AI · From Fundamentals to Intelligent Robotics

**从数学基础到机器人系统，从环境感知到智能决策，从仿真训练到真实世界交互。**

一套循序渐进、实践导向的中文具身智能课程。

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Docs](https://img.shields.io/badge/Docs-MkDocs%20Material-informational)
![Version](https://img.shields.io/badge/课程版本-v1.0.1-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## 课程简介

具身智能（Embodied AI）研究智能体如何通过身体、传感器和执行器与环境持续交互，并在感知、状态估计、规划、决策、控制和反馈中完成任务。它融合人工智能、机器人学、计算机视觉、控制理论、机器学习和物理仿真等领域。

本教程不把具身智能简化为某一种模型或某一个软件平台，而是从完整机器人系统出发，建立一条可实践的学习路径：

**数学与编程 → 机器人学 → 环境感知 → ROS 2 → 仿真 → 机器人学习 → VLA → 综合项目**

课程强调三个层次：

1. **理解原理：** 理解坐标系、公式、算法假设和适用边界。
2. **运行实验：** 通过 Python 示例验证推导，观察输入、输出和误差。
3. **构建系统：** 把感知、规划、控制和学习模块连接起来，形成可评估的机器人任务流程。

当前版本提供系统化入门至进阶课程、数学推导、基础代码示例和实验练习。大型仿真平台、真实机器人和大规模 VLA 训练需要根据设备与算力另行配置。

## 学完之后，你应该能够

- 解释具身智能系统的组成，并画出从观测到动作再到反馈的闭环。
- 使用向量、矩阵、旋转矩阵和齐次变换描述机器人空间关系。
- 推导并实现简单机械臂的正运动学、逆运动学和雅可比矩阵。
- 理解相机内参、深度图、点云和机器人坐标变换。
- 说明 ROS 2 的节点、话题、服务、动作和 TF 的作用。
- 比较 MuJoCo、Gazebo、Isaac Sim 与 Isaac Lab 的使用场景。
- 区分强化学习、模仿学习、行为克隆和 VLA 的问题设定。
- 设计具有输入、输出、评估指标和安全边界的机器人项目。

## 课程知识地图

```text
                         具身智能 Embodied AI
                                  │
          ┌───────────────────────┼────────────────────────┐
          │                       │                        │
       理论基础                 机器人系统                学习算法
          │                       │                        │
   智能体与环境             数学 / 坐标变换             机器学习
   感知与行动闭环           运动学 / 动力学             强化学习
   系统架构                 感知 / 控制                 模仿学习
          │                       │                      VLA / 世界模型
          └───────────────────────┼────────────────────────┘
                                  │
                            仿真与实验
                                  │
                       ROS 2 / MuJoCo / Gazebo
                          Isaac Sim / Isaac Lab
                                  │
                                  ▼
                             综合项目
                    感知 → 定位 → 规划 → 控制
                         → 执行 → 反馈评估
```

## 完整课程目录

### 模块 01｜具身智能基础
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [什么是具身智能](docs/01-foundations/01-embodied-ai.md) | 定义、特点、应用与研究问题 |
| 02 | [智能体交互闭环](docs/01-foundations/02-agent-loop.md) | Observation、State、Action、Feedback |
| 03 | [系统架构与任务分层](docs/01-foundations/03-system-architecture.md) | 高层任务、中层规划、低层控制 |

### 模块 02｜数学与空间变换
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [向量与矩阵](docs/02-mathematics/01-vectors-matrices.md) | 向量、矩阵乘法、点积、叉积 |
| 02 | [坐标系与参考系](docs/02-mathematics/02-coordinate-frames.md) | 世界、基座、关节、工具、相机坐标系 |
| 03 | [齐次变换矩阵](docs/02-mathematics/03-homogeneous-transforms.md) | 旋转、平移、变换链 |
| 04 | [三维姿态表示](docs/02-mathematics/04-rotation-representations.md) | 欧拉角、旋转矩阵、四元数 |

### 模块 03｜机器人学与控制
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [机器人结构与关节](docs/03-robotics/01-robot-model.md) | 自由度、连杆、关节、末端执行器 |
| 02 | [正运动学](docs/03-robotics/02-forward-kinematics.md) | 从关节变量求末端位姿 |
| 03 | [逆运动学](docs/03-robotics/03-inverse-kinematics.md) | 从目标位姿求关节变量 |
| 04 | [雅可比矩阵](docs/03-robotics/04-jacobian.md) | 关节速度与末端速度映射 |
| 05 | [轨迹规划](docs/03-robotics/05-trajectory-planning.md) | 关节空间、笛卡尔空间、时间参数化 |
| 06 | [控制基础](docs/03-robotics/06-control-basics.md) | 开环、闭环、PID 与安全约束 |

### 模块 04｜机器人感知
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [相机模型与标定](docs/04-perception/01-camera-model.md) | 针孔模型、内参、外参 |
| 02 | [RGB-D 与深度感知](docs/04-perception/02-rgbd-depth.md) | 深度图、反投影、误差来源 |
| 03 | [点云处理](docs/04-perception/03-point-cloud.md) | 采样、滤波、聚类、配准 |
| 04 | [目标检测与视觉任务](docs/04-perception/04-object-detection.md) | 检测、分割、跟踪与评估 |

### 模块 05｜ROS 2 机器人软件系统
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [ROS 2 核心概念](docs/05-ros2/01-ros2-concepts.md) | Node、Topic、Service、Action、TF |
| 02 | [Python 发布与订阅](docs/05-ros2/02-python-publisher-subscriber.md) | rclpy 节点通信 |

### 模块 06｜仿真与 Sim-to-Real
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [仿真平台选型](docs/06-simulation/01-simulation-platforms.md) | MuJoCo、Gazebo、Isaac Sim、Isaac Lab |
| 02 | [Sim-to-Real](docs/06-simulation/02-sim-to-real.md) | 域随机化、系统辨识、迁移验证 |

### 模块 07｜机器人学习与前沿模型
| 章节 | 内容 | 学习重点 |
|---|---|---|
| 01 | [机器学习基础](docs/07-learning/01-ml-foundations.md) | 数据、损失函数、泛化与评估 |
| 02 | [强化学习](docs/07-learning/02-reinforcement-learning.md) | MDP、策略、奖励、PPO 等 |
| 03 | [模仿学习](docs/07-learning/03-imitation-learning.md) | BC、DAgger、示范数据 |
| 04 | [VLA 模型](docs/07-learning/04-vla.md) | 视觉、语言、动作与机器人数据 |
| 05 | [世界模型](docs/07-learning/05-world-models.md) | 状态预测、潜空间动力学与规划 |

### 模块 08｜综合实践项目
| 项目 | 内容 | 难度 |
|---|---|---|
| 01 | [二自由度机械臂 FK / IK](docs/08-projects/01-planar-2dof-arm.md) | 入门 |
| 02 | [视觉颜色目标检测](docs/08-projects/02-vision-color-detection.md) | 入门 |
| 03 | [ROS 2 通信实验](docs/08-projects/03-ros2-communication.md) | 入门—中级 |
| 04 | 机械臂视觉抓取系统设计 | 中级 |
| 05 | 移动机器人导航系统设计 | 中级 |
| 06 | VLA 机器人操作任务分析 | 进阶 |

## 数学公式显示规范

本教程使用 LaTeX 编写数学公式。GitHub README 与 `docs/` 教程页面统一使用 `$...$` 行内公式和 `$$...$$` 独立公式。

平面二自由度机械臂的末端位置：

$$
\begin{aligned}
x &= L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) \\
y &= L_1\sin\theta_1 + L_2\sin(\theta_1+\theta_2)
\end{aligned}
$$

齐次变换矩阵：

$$
T =
\begin{bmatrix}
\cos\theta & -\sin\theta & t_x \\
\sin\theta & \cos\theta & t_y \\
0 & 0 & 1
\end{bmatrix}
$$

不要把裸 LaTeX 命令直接写成普通文本，也不要把需要渲染的公式放进普通代码块。

## 实践代码

### 二自由度机械臂
```bash
python examples/planar_2dof_arm/kinematics.py
python -m unittest discover -s examples/planar_2dof_arm -p "test_*.py"
```
实现正运动学、解析逆运动学、肘上 / 肘下分支和不可达目标检查。

### 智能体闭环
```bash
python examples/agent_loop/simple_agent.py
```
观察智能体如何执行“观测 → 决策 → 动作 → 新观测”的最小循环。

### OpenCV 颜色目标检测
```bash
pip install -r requirements-vision.txt
python examples/vision_color_tracking/color_tracker.py --camera 0
```
使用摄像头检测指定 HSV 颜色区域并计算像素中心。此示例不输出真实三维坐标，也不会控制机器人。

## 推荐学习顺序

1. 具身智能基础，建立系统闭环概念。
2. 向量、矩阵、坐标系和齐次变换。
3. 机器人运动学，并运行二自由度机械臂示例。
4. 相机模型、深度图和点云。
5. ROS 2 通信与坐标变换。
6. 选择一个仿真平台深入练习。
7. 学习强化学习、模仿学习和 VLA。
8. 完成综合项目，记录实验设置、评估指标和失败案例。

## 开发环境建议

- Python 3.10 或更高版本
- Git、VS Code
- 线性代数、三角函数和微积分基础
- 学习 ROS 2 时建议使用官方支持的 Linux 环境
- 深度学习和高保真仿真根据模型与平台要求选择 GPU

不要一开始安装所有仿真平台。不同平台对操作系统、显卡驱动和软件版本有不同要求，应先查阅官方兼容性说明。

## 安全说明

本教程用于学习与研究。数学示例和仿真代码不等于经过安全验证的真实机器人控制程序。真实硬件实验前必须进行风险评估，设置速度、力矩和工作空间限制，验证急停和人工接管，并在安全隔离区域由具备经验的人员监督。

## 官方资源

- [ROS 2 Documentation](https://docs.ros.org/)
- [MuJoCo Documentation](https://mujoco.readthedocs.io/)
- [Gazebo Documentation](https://gazebosim.org/docs)
- [NVIDIA Isaac Sim Documentation](https://docs.isaacsim.omniverse.nvidia.com/)
- [Isaac Lab](https://isaac-sim.github.io/IsaacLab/)
- [PyTorch](https://pytorch.org/)
- [OpenCV](https://docs.opencv.org/)
- [Python Documentation](https://docs.python.org/3/)

更多资源见 [官方文档索引](docs/resources/official-resources.md) 和 [论文阅读指南](docs/resources/paper-reading.md)。

---

<div align="center">

**Learn · Perceive · Reason · Plan · Act · Improve**

让智能不止于理解，更能够感知、行动与探索真实世界。

</div>
