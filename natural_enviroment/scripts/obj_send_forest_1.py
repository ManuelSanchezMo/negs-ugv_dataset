#!/usr/bin/env python  
import roslib

import rospy
import math
import tf
from std_msgs.msg import Float32
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension

if __name__ == '__main__':
    rospy.init_node('obj_send')

    
    pub = rospy.Publisher('/navigation/objetive_gps', Float64MultiArray, queue_size=10)
    msg=Float64MultiArray()
    points=MultiArrayDimension()
    coords=MultiArrayDimension()
    points.label = "numero_puntos"
    points.size =3
    points.stride = points.size * 2
    msg.layout.dim.append(points)
    coords.label = "numero_coordenadas"
    coords.size = 2
    coords.stride = 2
    msg.layout.dim.append(coords)
    msg.layout.data_offset = 0

    msg.data.append(49.9003714848)
    msg.data.append( 8.89994488402)


    msg.data.append(49.9003010126)
    msg.data.append( 8.89993377297)

    msg.data.append(49.9001315134)
    msg.data.append(8.89995588079)

    msg.data.append(49.9001315134)
    msg.data.append(8.89995588079)

    msg.data.append(49.8999967186)
    msg.data.append(8.89995965979)

    msg.data.append(49.8999967186)
    msg.data.append(8.89995965979)

    msg.data.append(49.8999180043)
    msg.data.append(8.89998487274)

    msg.data.append(49.899827401)
    msg.data.append(8.90009283695)

    msg.data.append(49.8997426026)
    msg.data.append(8.90021135075)
    rate = rospy.Rate(10.0)
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
    pub.publish(msg)
    rate.sleep()
