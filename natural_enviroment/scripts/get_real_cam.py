#!/usr/bin/env python  
import roslib
import rosbag
import rospy
import math
import tf
import sys
import numpy as np
from std_msgs.msg import Float32,Header
from sensor_msgs.msg import CameraInfo, Image,CompressedImage
from gazebo_msgs.srv import SpawnModel, DeleteModel,SetModelState
from gazebo_msgs.msg import ModelState,ModelStates
from cv_bridge import CvBridge
import cv2
import getopt
import matplotlib.pyplot as plt
im_left_check=False
im_rigth_check=False
pose_check=False
img_msg_right=CompressedImage()
img_msg_left=CompressedImage()
def left_img_cb(msg):
     global img_msg_left
     img_msg_left=msg
     im_left_check=True
def right_img_cb(msg): 
     global img_msg_right
     img_msg_right=msg
def pose_cb(msg):
     global pose_check
     pose_check=True
if __name__ == '__main__':
  global img_msg_left
  global img_msg_right
  global im_rigth_check
  global pose_check

  bridge = CvBridge()
  inputfile = ''
  outputfile = ''
  try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
  rospy.init_node('im_listener')
  rospy.Subscriber("/husky/camera/left/image_raw/compressed",CompressedImage,left_img_cb)
  rospy.Subscriber("/husky/camera/right/image_raw/compressed",CompressedImage,right_img_cb)
  t_prev=rospy.Time()
  m_count=0
  f=0
  with rosbag.Bag(outputfile, 'w') as outbag:
    for topic, msg, t in rosbag.Bag(inputfile).read_messages():
       #if topic != "/stereo/camera/right/image_raw_tagged":
           #outbag.write(topic, msg, t)
       outbag.write(topic, msg, t)
       if topic == "/gazebo/model_states" :
            m_count=m_count+1
            if m_count==40:
               f=f+1
 
               m_count=0

               t_prev=t

               msg_move=ModelState()
               msg_move.model_name='stereo_camera'
               #Se usa el cambio baselink->cameralink para posicionarla correctamente
               msg_move.pose=msg.pose[len(msg.name)-1]
               msg_move.pose.position.x=msg.pose[len(msg.name)-1].position.x+0.0812
               msg_move.pose.position.z=msg.pose[len(msg.name)-1].position.z+0.245+0.52
    	       rospy.wait_for_service('/gazebo/set_model_state')
               try:
                   set_state = rospy.ServiceProxy(
                      '/gazebo/set_model_state', SetModelState)
                   resp = set_state(msg_move)
  

               except rospy.ServiceException as e:
                   print ("Service call failed: %s" % e)
               rospy.sleep(0.01)
               print(resp)
               im_left_check=False
               im_rigth_check=False
               pose_check=False
               '''
               img_left = rospy.wait_for_message('/husky/camera/left/image_raw', Image, timeout=500)
               img_right = rospy.wait_for_message('/husky/camera/left/image_raw', Image, timeout=500)
               '''
               #im_save=img_msg
               #im_left_cv=bridge.imgmsg_to_cv2(img_msg)
          
               #name_real='imr'+str(f)+'.png'
               #im_left=bridge.imgmsg_to_cv2(img_left)
               #cv2.imwrite(name_real, im_left)
               #print(f)


               outbag.write('stereo/camera/left/real/compressed', img_msg_left, t)
               outbag.write('stereo/camera/right/real/compressed', img_msg_right, t)



              
