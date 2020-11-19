#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32 
from common_msgs.msg import Timevector

def callback(msg):
    num = msg.vector.x + msg.vector.y + msg.vector.z
    print "subscribe:",  num
rospy.init_node('sch_subscriber')
sub = rospy.Subscriber('common_msgs', Timevector, callback)
rospy.spin()
