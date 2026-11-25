"""Minimal ROS 2 subscriber. Run inside a sourced ROS 2 Python package."""

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
