#!/usr/bin/env python3
# Import necessary libraries for ROS2 and geometry messages
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Define a class for the node that draws a circle
class DrawCircleNode(Node):

    # Initialize the node with a name and set up a publisher for velocity commands
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # Log a message to indicate the node has started
        self.get_logger().info("Starting Circle Node......")
        # Create a timer to call the vel_cmd function at regular intervals
        self.create_timer(0.5, self.vel_cmd)

    # Define a function to generate and publish velocity commands
    def vel_cmd(self):
       # Create a Twist message to hold the velocity command
       msg = Twist()
       # Set the linear velocity 
       msg.linear.x = 2.0
       # Set the angular velocity
       msg.angular.z = 1.0
       # Publish the velocity command
       self.cmd_vel_pub.publish(msg)


# Define the main function to initialize and run the node
def main(args=None):
    # Initialize the ROS2 environment
    rclpy.init(args=args)
    # Create an instance of the DrawCircleNode class
    node = DrawCircleNode()
    # Run the node's main loop
    rclpy.spin(node)
    # Shut down the ROS2 environment
    rclpy.shutdown()

# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Call the main function
    main()