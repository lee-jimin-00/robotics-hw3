#!/usr/bin/env python
import rospy
from common_msgs.msg import Timevector
from geometry_msgs.msg import Vector3


rospy.init_node('sch_publisher')
pub = rospy.Publisher('common_msgs', Timevector, queue_size=1)
msg = Timevector()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.vector= Vector3(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z
    rate.sleep()


