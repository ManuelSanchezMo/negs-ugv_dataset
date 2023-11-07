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


    msg.data.append(49.9002052314)
    msg.data.append(8.89982764647)

    msg.data.append(49.9001072849)
    msg.data.append(8.8998093971)

    msg.data.append(49.8999730275)
    msg.data.append( 8.89982059379)

    msg.data.append(49.8997742649)
    msg.data.append(8.89986186362)

    msg.data.append(49.899718201)
    msg.data.append(8.89989296404)

    msg.data.append(49.8996791001)
    msg.data.append(8.90003010789)

    msg.data.append(49.8997418387)
    msg.data.append(8.90016432491)

    msg.data.append(49.8997418387)
    msg.data.append(8.90016432491)

    msg.data.append(49.899816444)
    msg.data.append( 8.90018983489)

    msg.data.append(49.8999742285)
    msg.data.append(8.90018406505)

    msg.data.append(49.899974104)
    msg.data.append(8.90018358044)

    msg.data.append(49.9000841125)
    msg.data.append(8.90018545776)

    msg.data.append(49.9002423706)
    msg.data.append(8.90018657159)

    msg.data.append(49.9003312078)
    msg.data.append( 8.90017497398)


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
