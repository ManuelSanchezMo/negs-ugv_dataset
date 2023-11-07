Software requirements:
Ubuntu 18.04
Ros Melodic (Desktop-full)

Hardware requirements:
Memory: 32GB RAM
Graphics: Nvidia GTX 1050 

INSTALLATION:

1. Extract models.zip into folder models in gazebo (usually in ~/.gazebo)
2. Create folder simulator into catkin_ws/src
3. Extract worlds.zip into simulator folder
4. Extract husky_ouster.zip into src folder
5. Build packages, e.g., catkin_make
6. Install packages: 

ros-melodic-hector-gazebo-plugins 
ros-melodic-robot-localization
ros-melodic-interactive-marker-twist-server
ros-melodic-twist-mux
ros-melodic-joy
ros-melodic-teleop-twist-joy
ros-melodic-geonav-transform

7. Add to .bashrc or .zshrc

export HUSKY_SENSOR_ARCH="true"
export HUSKY_URDF_EXTRAS=~/catkin_ws/src/husky/husky_description/urdf/sensor_description.urdf

USAGE:

1. Change directory

cd ~/catkin_ws

2. Source 

source devel/setup.bashrc

or

source devel/setup.zshrc

3. Launch environment simulation

roslaunch natural_environments create_<environment>.launch

where environment = forest, hill, lake or park. The loading time may vary between 2 and 10 minutes depending on the complexity of the environment
(simplest - park, lake, hill, forest - most complex)

4. Place husky on the environment
	
roslaunch natural_environments add_husky_<environment>_#.launch

where environment = forest, hill, lake or park and # = 1 or 2

5. Run navigation script

rosrun natural_environments fixer_husky.py

6. Record ROS messages except camera data using rosbag record

rosbag record -O <environment>_#.bag /gazebo/model_states /gazebo_client/back_left_speed /gazebo_client/back_right_speed /gazebo_client/front_left_speed /gazebo_client/front_right_speed /imu/data /imu/data/accel/parameter_descriptions /imu/data/accel/parameter_updates /imu/data/bias  /imu/data/rate/parameter_descriptions /imu/data/rate/parameter_updates  /imu/data/yaw/parameter_descriptions /imu/data/yaw/parameter_updates /navsat/fix  /navsat/fix/position/parameter_descriptions /navsat/fix/position/parameter_updates /navsat/fix/status/parameter_descriptions /navsat/fix/status/parameter_updates /navsat/fix/velocity/parameter_descriptions /navsat/fix/velocity/parameter_updates /navsat/vel /odometry/filtered /os0_cloud_node/imu /os0_cloud_node/imu/accel/parameter_descriptions /os0_cloud_node/imu/accel/parameter_updates  /os0_cloud_node/imu/bias /os0_cloud_node/imu/rate/parameter_descriptions /os0_cloud_node/imu/rate/parameter_updates /os0_cloud_node/imu/yaw/parameter_descriptions /os0_cloud_node/imu/yaw/parameter_updates  /os0_cloud_node/points /tf /tf_static /navigation/objetive_gps

NOTE: Gazebo real time factor greatly decreases due to the data recording process.

7. Run way-point generator

rosrun natural_environments obj_send_<environment>_#.py

where environment = forest, hill, lake or park and # = 1 or 2

8. When path following has finished close rosbag record 

9. Close everything and launch natural environment to record realistic image from stereo camera

roslaunch natural_environments create_<environment>.launch

where environment = forest, hill, lake or park.


10. Spawn camera for the experiment at position

roslaunch natural_environments spawn_camera_<environment>_#.launch

where environment = forest, hill, lake or park.

11. Run the following script to capture the realistic stereo camera images:

python ~/catkin_ws/src/natural_enviroment/scripts/get_real_cam.py -i <environment>_#.bag -o <environment>_#_real_camera.bag

where environment = forest, hill, lake or park.

12. Close Gazebo and launch the natural environment with plain colors

roslaunch natural_environments create_<environment>_tagged.launch

where environment = forest, hill, lake or park.

13. Spawn camera for the experiment at position

roslaunch natural_environments spawn_camera_<environment>_#.launch

where environment = forest, hill, lake or park.

14. Run the script to create the tagged stereo camera images:

python ~/catkin_ws/src/natural_enviroment/scripts/get_tag_cam.py -i <environment>_#_real_camera.bag -o <environment>_#_complete.bag

where environment = forest, hill, lake or park

15. For extracting all data as human readable run the script:
 
python ~/catkin_ws/src/natural_enviroment/scripts/extract_bag.py -i <environment>_#_complete.bag -f <environment>_#_folder


