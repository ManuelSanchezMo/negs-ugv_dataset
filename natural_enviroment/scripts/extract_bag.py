#!/usr/bin/env python  
import roslib
import rosbag
import rospy
import math
import getopt
import sys
import tf
import os
import numpy as np
from std_msgs.msg import Float32,Header
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import CameraInfo, Image
import csv
from cv_bridge import CvBridge
import cv2
from gazebo_msgs.msg import ModelState,ModelStates
from sensor_msgs.msg import PointCloud2

if __name__ == '__main__':
  inputfile = ''
  try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:",["ifile="])
  except getopt.GetoptError:
      print 'test.py -i <inputfile> '
      sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> '
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
  bridge = CvBridge()
  rospy.init_node('bag_extractor')	
  text_file_imu = open("imu_data.txt", "w")
  text_file_gps = open("gps_data.txt", "w")
  text_file_position_ground_truth = open("position_gt_data.txt", "w")
  text_file_cmd_vel = open("cmd_vel.txt", "w")
  os.mkdir('img_left')
  os.mkdir('img_left_tag')
  os.mkdir('img_right')
  os.mkdir('img_right_tag')
  os.mkdir('lidar')
  os.mkdir('tachometers')
  os.mkdir('imu')
  back_left_tachometre = open("tachometers/back_left_tachometre.txt", "w")
  front_left_tachometre = open("tachometers/front_left_tachometre.txt", "w")
  back_right_tachometre = open("tachometers/back_right_tachometre.txt", "w")
  front_right_tachometre = open("tachometers/front_right_tachometre.txt", "w")
  for topic, msg, t in rosbag.Bag(inputfile).read_messages():

       time=t.secs*pow(10,9)+t.nsecs
       print((topic))
       if topic == "stereo/camera/left/real/compressed" :
          im=bridge.compressed_imgmsg_to_cv2(msg)
          name='img_left/'+str(time)+'_left.png'
          cv2.imwrite(name, im)

       if topic == "stereo/camera/right/real/compressed" :
          im=bridge.compressed_imgmsg_to_cv2(msg)
          name='img_right/'+str(time)+'_right.png'
          cv2.imwrite(name, im)

       if topic == "stereo/camera/left/tag/img_raw" :
          im=bridge.imgmsg_to_cv2(msg)
          name='img_left_tag/'+str(time)+'left_tag.png'
          cv2.imwrite(name, im)

       if topic == "stereo/camera/right/tag/img_raw" :
          im=bridge.imgmsg_to_cv2(msg)
          name='img_right_tag/'+str(time)+'right_tag.png'
          cv2.imwrite(name, im)
       if topic == "/imu/data" :

          msg_string=str(time)+' ' +' '+str(msg.orientation.x)+''+str(msg.orientation.y)+' '+str(msg.orientation.z)+''+str(msg.orientation.w)  +' '+str(msg.angular_velocity.x)+' '+str(msg.angular_velocity.y)+' '+str(msg.angular_velocity.z)+' '+str(msg.linear_acceleration.x)+' '+str(msg.linear_acceleration.y)+' '+str(msg.linear_acceleration.z)+'\n'
          n = text_file_imu.write(msg_string)

       if topic == "/gazebo_client/back_left_speed" :
          msg_string=str(time) +' '+str(msg.data)+'\n'
          n = back_left_tachometre.write(msg_string)
       if topic == "/gazebo_client/back_right_speed" :
          msg_string=str(time) +' '+str(msg.data)+'\n'
          n = back_right_tachometre.write(msg_string)
       if topic == "/gazebo_client/front_left_speed" :
          msg_string=str(time) +' '+str(msg.data)+'\n'
          n = front_left_tachometre.write(msg_string)
       if topic == "/gazebo_client/front_right_speed" :
          msg_string=str(time) +' '+str(msg.data)+'\n'
          n = front_right_tachometre.write(msg_string)
       if topic == "/navsat/fix" :
          msg_string=str(time)+' ' +' '+str(msg.latitude)+' '+str(msg.longitude)+' '+str(msg.altitude)+'\n'
          n = text_file_gps.write(msg_string)
       if topic == "/os1_cloud_node/points" :
          cloud_name='lidar/'+str(time)+'.csv'
          cloud_points = []
          for p in pc2.read_points(msg, field_names = ("x", "y", "z","intensity"), skip_nans=True):
              cloud_points.append(p)

          with open(cloud_name, "wb") as f:
              writer = csv.writer(f)
              writer.writerows(cloud_points)
       if topic == "/cmd_vel" :
          msg_string=str(time)+' ' +' '+str(msg.latitude)+' '+str(msg.longitude)+' '+str(msg.altitude)+'\n'
       if topic == "/gazebo/model_states" :
          robot_index=msg.name.index('husky')
          pose=msg.pose[robot_index]
          msg_string=str(time)+' '+' '+str(pose.position.x)+' '+str(pose.position.y)+' '+str(pose.position.z) +' '+str(pose.orientation.x)+' '+str(pose.orientation.y)+' '+str(pose.orientation.z)+' '+str(pose.orientation.w)  +'\n'
          n = text_file_position_ground_truth.write(msg_string)
  text_file_imu.close()
  text_file_gps.close()
  text_file_position_ground_truth.close()
