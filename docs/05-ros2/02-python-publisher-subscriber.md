# 02｜ROS 2 Python 发布与订阅

本章给出 `rclpy` 的最小示例。运行前需要安装并正确 source 对应 ROS 2 发行版。

## 2.1 Publisher

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("tutorial_talker")
        self.publisher = self.create_publisher(String, "chatter", 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f"Hello embodied AI: {self.count}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
```

## 2.2 Subscriber

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("tutorial_listener")
        self.subscription = self.create_subscription(
            String, "chatter", self.callback, 10
        )

    def callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")


def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
```

## 2.3 运行思路

将两个脚本放入正确的 ROS 2 Python package，并在 `setup.py` 中注册 console scripts。构建并 source 工作空间后，分别启动 talker 和 listener。

## 2.4 观察点

- 两个节点是否都能被发现？
- 发布者和订阅者的话题名称、消息类型是否一致？
- QoS 设置是否兼容？
- 节点退出时资源是否正确释放？
