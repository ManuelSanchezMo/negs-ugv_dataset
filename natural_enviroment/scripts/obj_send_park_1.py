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
    points.size =9
    points.stride = points.size * 2
    msg.layout.dim.append(points)
    coords.label = "numero_coordenadas"
    coords.size = 2
    coords.stride = 2
    msg.layout.dim.append(coords)
    msg.layout.data_offset = 0

    msg.data.append(49.9003439105)
    msg.data.append(8.89998265669)

    msg.data.append(49.9002436091)
    msg.data.append(8.89998465971)

    msg.data.append(49.9002436091)
    msg.data.append(8.89998465971)

    msg.data.append(49.9000103866)
    msg.data.append(8.90003336643)

    msg.data.append(49.899856529)
    msg.data.append(8.90004639993)

    msg.data.append(49.899856529)
    msg.data.append(8.90004639993)

    msg.data.append(49.8997232844)
    msg.data.append(8.9000480494)
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
