#!/usr/bin/env python
import rospy
from common_msgs.srv import DivTwoNum, DivTwoNumResponse

def service_callback(request):
    response = DivTwoNumResponse(div=request.a - request.b)
    print "request data:", request.a, request.b, ", response: (reduce)", response.div, "Battery :", request.b
    if request.b > 80:
        print "very good"
    elif (request.b >50) and (request.b <= 80):
        print "good"
    elif (request.b > 30) and (request.b <= 50):
        print "not bad"
    elif (request.b > 10) and (request.b <= 30):
        print " bad"
    elif (request.b > 0) and (request.b <= 10):
        print "very bad"
    elif request.b == 0:
        print "over"
    return response

rospy.init_node('sch_server')
service = rospy.Service('div_two_number', DivTwoNum, service_callback)
rospy.spin()
