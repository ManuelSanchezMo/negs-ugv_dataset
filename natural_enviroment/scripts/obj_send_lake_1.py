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

    msg.data.append(49.899674532)
    msg.data.append(8.90021489657)

    msg.data.append(49.8997771728)
    msg.data.append(8.90015486364)

    msg.data.append(49.8998714531)
    msg.data.append(8.90006200193)

    msg.data.append(49.8999659543)
    msg.data.append(8.89997311259)

    msg.data.append(49.9000949478)
    msg.data.append(8.89989594223)

    msg.data.append(49.9002511139)
    msg.data.append(8.89983039325)

    msg.data.append(49.9003580251)
    msg.data.append(8.8997341309)


    msg.data.append(49.9004006963)
    msg.data.append(8.89980215277)


    msg.data.append(49.900337319)
    msg.data.append(8.89987525049)


    msg.data.append(49.9002687235)
    msg.data.append(8.90005973355)

    msg.data.append(49.9001859327)
    msg.data.append(8.90008306199)

    msg.data.append(49.9000739357)
    msg.data.append(8.90016060267)

    msg.data.append(49.9000182648)
    msg.data.append(8.90022615456)

    msg.data.append(49.8999049306)
    msg.data.append(8.90016081326)

    msg.data.append(49.899714537)
    msg.data.append(8.90018873468)
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
