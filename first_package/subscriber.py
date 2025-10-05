import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose			# /turtle1/pose [turtlesim/msg/Pose]

class TurtlesimSubscriber(Node):
	def __init__(self):
		super().__init__('turtlesim_subscriber')
		self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.callback, 10)

	def callback(self, msg):
		print('x:', msg.x, ', y:', msg.y)

def main(args=None):
	rp.init(args=args)
	turtlesim_subscriber = TurtlesimSubscriber()
	rp.spin(turtlesim_subscriber)

	turtlesim_subscriber.destroy_node()
	rp.shutdown()

if __name__ == '__main__':
	main()
