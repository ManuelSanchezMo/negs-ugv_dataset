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

    msg.data.append(49.8997050979)
    msg.data.append(8.9002609161)

    msg.data.append(49.8997050979)
    msg.data.append(8.9002609161)

    msg.data.append(49.8997668328)
    msg.data.append(8.90016321205)

    msg.data.append(49.8999267705)
    msg.data.append(8.89998310184)

    msg.data.append(49.8999267705)
    msg.data.append(8.89998310184)

    msg.data.append(49.8998463325)
    msg.data.append(8.8999042785)

    msg.data.append(49.8997136283)
    msg.data.append(8.89982003253)

    msg.data.append(49.8996051022)
    msg.data.append(8.89973291934)
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
