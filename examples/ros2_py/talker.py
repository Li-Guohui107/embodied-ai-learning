"""Minimal ROS 2 publisher. Run inside a sourced ROS 2 Python package."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("tutorial_talker")
        self.publisher = self.create_publisher(String, "chatter", 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.publish_message)

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
