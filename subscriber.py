import rclpy as rp 
from rclpy.node import Node 
from turtlesim.msg import Pose              # /turtle1/pose [turtlesim/msg/Pose]

class TurtlesimSubscriber(Node):
    def __init__(self):
        super().__init__('turtlesim_subscriber')    # 'turtlesim_subscriber'는 노드 이름
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.callback, 10)

    def callback(self, msg):                # msg : turtlesim/msg/Pose type
        print("x:", msg.x, ", y:", msg.y)

def main(args=None):
    rp.init(args=args)
    turtlesim_subscriber = TurtlesimSubscriber()    # Class TurtlesimSubscriber 객체 생성
    rp.spin(turtlesim_subscriber)                   # 생성한 객체 실행(객체에 발생한 이벤트 처리 등)

    turtlesim_subscriber.destroy_node()             # 객체 삭제
    rp.shutdown()                                   # rclpy 종료

if __name__ == '__main__':
    main()

# self.self.subscriber = self.create_subscription(
#                               msg_type,           # 메시지 타입 (예: Pose)
#                               topic,              # 토픽 이름 (예: '/turtle1/pose')
#                               callback,           # 콜백 함수
#                               qos_profile         # QoS 설정 (여기서는 10)
