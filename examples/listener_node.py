import rospy
from rosrx import observabletopic
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('listener_node')

    topic = observabletopic('/chatter', String)
    topic.subscribe(lambda msg: rospy.loginfo(msg.data))

    rospy.spin()
