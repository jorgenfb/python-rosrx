import rospy
import pkg_resources

from rosrx import TopicObserver
from std_msgs.msg import String


if __name__ == '__main__':
    rospy.init_node('talker_node')

    if pkg_resources.get_distribution('rx').version.startswith('1.'):
        # Usage for rx 1.x
        from rx import Observable
        source = Observable.interval(1000)
        source.map(lambda value: 'hello world {}'.format(value)).subscribe(
            observer=TopicObserver('/chatter', String, queue_size=1))
    else:
        # Usage for rx 3.x
        from rx import interval
        from rx.operators import map
        source = interval(1.0)
        source.pipe(map(lambda value: 'hello world {}'.format(value))).subscribe(
            observer=TopicObserver('/chatter', String, queue_size=1))

    rospy.spin()
