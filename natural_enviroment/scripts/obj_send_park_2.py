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

    msg.data.append(49.9003753127)
    msg.data.append(8.89990414421)

    msg.data.append(49.9002215744)
    msg.data.append(8.89981442453)

    msg.data.append(49.9001570052)
    msg.data.append(8.89975981705)

    msg.data.append(49.9001570052)
    msg.data.append(8.89975981705)

    msg.data.append(49.9000894361)
    msg.data.append(8.89987280729)

    msg.data.append(49.9000197913)
    msg.data.append( 8.90003912138)

 

    msg.data.append(49.9000061145)
    msg.data.append(8.90007898626)

    msg.data.append(49.899948754)
    msg.data.append(8.90019538206)

    msg.data.append(49.8998651447)
    msg.data.append(8.90022626211)

    msg.data.append(49.8997961155)
    msg.data.append(8.90020325011)

    msg.data.append(49.899679516)
    msg.data.append(8.90001835798)

    msg.data.append(49.8997008847)
    msg.data.append(8.89987985049)

    msg.data.append(49.8998309318)
    msg.data.append(8.89982764988)

    msg.data.append(49.8998933443)
    msg.data.append(8.89995454)

    msg.data.append(49.899969462)
    msg.data.append(8.90005987382)

    msg.data.append(49.9001063895)
    msg.data.append(8.90021451447)

    msg.data.append(49.9002462448)
    msg.data.append(8.90020568804)

    msg.data.append(49.9003736772)
    msg.data.append(8.90011904742)
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
