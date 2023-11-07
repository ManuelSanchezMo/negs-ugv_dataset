import rosbag
import rospy
n_messages=0
init_time=0
first_time=False
static=True

with rosbag.Bag('park_sampled.bag', 'w') as outbag:
    for topic, msg, t in rosbag.Bag('park_2_merged.bag').read_messages():

         if first_time==False:
            init_time=t.to_sec()
            first_time=True


         outbag.write(topic, msg, t)
         if t.to_sec()-init_time>15.0:
               break


    print("Ended")
