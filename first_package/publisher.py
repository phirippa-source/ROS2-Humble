import rclpy as rp 
from rclpy.node import Node
from geometry_msgs.msg import Twist 		# /turtle1/cmd_vel [geometry_msgs/msg/Twist]

class TurtlesimPublisher(Node):
	def __init__(self):
		super().__init__('turtlesim_publisher')
		self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		self.timer = self.create_timer(0.5, self.callback_timer)

	def callback_timer(self):
		msg = Twist()
		msg.linear.x = 2.0
		msg.angular.z = 1.57
		self.publisher.publish(msg)

def main(args=None):
	rp.init(args=args)
	turtlesim_publisher = TurtlesimPublisher()
	rp.spin(turtlesim_publisher)

	turtlesim_publisher.destroy_node()
	rp.shutdown()

if __name__ == '__main__':
	main()
