# 项目 03｜ROS 2 通信实验

## 目标

创建两个 ROS 2 Python 节点：一个周期性发布字符串，另一个订阅并打印消息。

## 示例代码

代码位于 `examples/ros2_py/talker.py` 和 `examples/ros2_py/listener.py`。

## 实验步骤

1. 安装并 source 与操作系统匹配的 ROS 2 发行版。
2. 创建 Python package，并加入 `rclpy` 和 `std_msgs` 依赖。
3. 将示例节点放入 package。
4. 在 `setup.py` 中注册两个 console scripts。
5. 构建并 source 工作空间。
6. 分别启动 talker 和 listener。
7. 使用 `ros2 topic list` 和 `ros2 topic echo /chatter` 检查消息。

## 观察与思考

- 发布者和订阅者的话题名称是否一致？
- 消息类型是否一致？
- QoS 不兼容时会发生什么？
- 如果发布频率增加，订阅端如何处理消息积压？

本示例展示通信机制，不包含真实硬件驱动。
