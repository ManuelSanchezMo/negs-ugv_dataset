#!/usr/bin/env python  
import roslib
import rospy
import numpy as np
import math
import tf
from sensor_msgs.msg import MagneticField,Imu
from std_msgs.msg import Header,Float64MultiArray
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PointStamped,Twist
from std_msgs.msg import Float32
from geometry_msgs.msg import PointStamped
from geonav_transform.geonav_conversions import LLtoUTM
class Fixer(object):
	def __init__(self,):
	  	rospy.init_node('Fixer', anonymous=True)
		rospy.Subscriber("/compass/data",Imu, self.callimu)
		rospy.Subscriber("/navsat/fix",NavSatFix,self.Fix)
		rospy.Subscriber("/navigation/objetive_gps",Float64MultiArray,self.Objetives)
		self.pubvel = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
		self.enviar=False
		self.obje=0
		self.norte=0
		self.relx=0
		self.rely=0 
                self.fin=False
		self.n_obj=0
		self.lat_obj=0
		self.last_point=0
		self.lon_obj=0
		self.obj=[0,0]
		self.objetives_=Float64MultiArray
		rospy.spin()

	def obj(self,msg):
		self.obje=msg.data

	def Fixdif(self,msg):
		self.lat_obj=msg.latitude
		self.lon_obj=msg.longitude
		obj=LLtoUTM(self.lon_obj,self.lat_obj)
		print('obj'+str(obj))
		self.obje=math.atan2(obj[0],obj[1])

	def callimu(self,msg):
		quat=[msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w]
		euler= tf.transformations.euler_from_quaternion(quat)
		self.norte=euler[2]       
		obj=math.atan2(self.rely,-self.relx)
		dir_obj=(-obj+self.norte)
		if abs(dir_obj)>math.pi:
			if (dir_obj)>0:
				yaw_error=-2*math.pi+dir_obj
			else:
				yaw_error=2*math.pi+dir_obj
                else:
                    yaw_error=dir_obj		
		mssg=Twist()
                if self.fin==False and self.enviar==True: 
		    mssg.linear.x=0.3
		    mssg.angular.z=-5.5*yaw_error
                else:
		    mssg.linear.x=0.0
		    mssg.angular.z=0.0
		self.pubvel.publish(mssg)
		
	def Objetives(self,msg):
		self.objetives_ = msg
		self.lat_obj=self.objetives_.data[self.n_obj]
		self.lon_obj=self.objetives_.data[self.n_obj+1]
                self.last_point=len(self.objetives_.data)
                self.enviar=True

	def Fix(self,msg):
		obj=LLtoUTM(self.lat_obj,self.lon_obj)
		utm=LLtoUTM(msg.latitude,msg.longitude)
		dist=math.sqrt((utm[0]-obj[0])**2+(utm[1]-obj[1])**2)
		if dist<1.0:
		        print('nobj'+str(self.n_obj))
			self.n_obj=self.n_obj+2
                        if self.n_obj>self.last_point:
                           pause_physics_client=rospy.ServiceProxy('/gazebo/pause_physics',Empty)
                           pause_physics_client(EmptyRequest())
                           self.fin=True
                        
                        else:
			   self.lat_obj=self.objetives_.data[self.n_obj]
			   self.lon_obj=self.objetives_.data[self.n_obj+1]

		self.relx=utm[0]-obj[0]
		self.rely=utm[1]-obj[1]
		
if __name__ == '__main__':
	Fixer()
			  
      
