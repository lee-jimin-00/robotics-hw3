#!/usr/bin/env python
import rospy
from common_msgs.srv import DivTwoNum, DivTwoNumRequest

rospy.init_node('sch_client')
rospy.wait_for_service('div_two_number')
requester = rospy.ServiceProxy('div_two_number', DivTwoNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(3)
count = 100
while count > 0:
    if count % 1 == 0:
        req = DivTwoNumRequest(a=count, b=count-1)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.div
    rate.sleep()
    count -= 1
