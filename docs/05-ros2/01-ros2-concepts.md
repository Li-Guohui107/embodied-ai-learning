# 01｜ROS 2 核心概念

## 1.1 ROS 2 是什么？

ROS 2 是机器人软件开发的中间件与工具生态，不是传统意义上的操作系统。它提供通信机制、工具、消息定义和软件包组织方式。

## 1.2 核心概念

| 概念 | 作用 | 例子 |
|---|---|---|
| Node | 独立功能模块 | 相机节点、控制节点 |
| Topic | 发布 / 订阅数据流 | `/camera/image` |
| Service | 请求—响应调用 | 查询配置 |
| Action | 可反馈、可取消的长任务 | 导航到目标点 |
| Message | 通信数据结构 | 图像、位姿、速度 |
| Parameter | 节点配置 | 相机帧率 |
| TF | 坐标系变换管理 | `base_link` 到 `camera_link` |

## 1.3 典型数据流

```text
Camera Node ── image topic ──> Perception Node
                                      │
                                      ▼
Planner Node ── target command ──> Controller Node
                                      │
                                      ▼
                                  Robot Driver
```

## 1.4 推荐学习顺序

1. 按照官方安装说明选择 ROS 2 发行版。
2. 学习 workspace、package 和 node。
3. 使用 `ros2 node list` 查看节点。
4. 使用 `ros2 topic list` 和 `ros2 topic echo` 检查话题。
5. 编写 publisher 和 subscriber。
6. 学习 service、action、launch、parameter 和 TF。

不同 ROS 2 发行版的支持平台和安装步骤不同，不要混用不同版本的命令。
