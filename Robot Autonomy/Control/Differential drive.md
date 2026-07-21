# Differential drive



```python
import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class diff_drive(Node):

    def __init__(self):
        super().__init__('obstacle_avoider')
        # Create the publisher, define the type of message,
        # the topic and the frame rate
        self.__publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Create the subscriber, define the type of message,
        # the topic and the frame rate
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg: LaserScan):
        # Create a variable and Define the position of the scanner,
        # which will subcribe the distance.
        front_ranges = msg.ranges[165:195]
        valid_ranges = [r for r in front_ranges if math.isfinite(r) and r > 0.0]

        # Create a variable, and give him the type of Twist()
        min_distance = min(valid_ranges) if valid_ranges else float('inf')
        self.get_logger().info(f'Front min distance: {min_distance:.3f} m')

        # Create a variable, and give him the type of Twist()
        command_msg = Twist()
        # Define the speed of the robot to 0.2 m/s in x axis
        command_msg.linear.x = 0.2
        command_msg.angular.z = 0.0

        if min_distance < 0.5:
            # Define the speed of the robot, if the obstacle is in front
            command_msg.linear.x = 0.0
            command_msg.angular.z = 2.0
        
        # Publish the speed
        self.__publisher.publish(command_msg)


def main(args=None):
    rclpy.init(args=args)
    # Create an instance
    avoider = diff_drive()
    # run the instance
    rclpy.spin(avoider)
    
    # End the programm with Cntr+C
    avoider.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

