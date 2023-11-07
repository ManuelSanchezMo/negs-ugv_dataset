#!/bin/bash

xhost +local:root
IMG=wilselby/ouster_example:latest

# If NVIDIA is present, use Nvidia-docker
if test -c /dev/nvidia0
then
    docker run --rm -it \
      --runtime=nvidia \
      --privileged \
      --device /dev/dri:/dev/dri \
      --env="DISPLAY" \
      --env="QT_X11_NO_MITSHM=1" \
      -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
      $IMG \
      bash
else
    docker run --rm -it \
      -e DISPLAY \
      --device=/dev/dri:/dev/dri \
      -v "/tmp/.X11-unix:/tmp/.X11-unix" \
      $IMG \
      bash
fi

# Google Cartographer commands

# Get sample data
# cd /root/bags
# curl -O https://data.ouster.io/downloads/office_demo_9_25_19.bag 

# Source the workspace
# source /root/catkin_ws/devel/setup.bash

# Navigate to the cartographer_ros launch file directory
# cd /root/catkin_ws/src/ouster_example/cartogrpaher_ros/launch

## Validate rosbag
#rosrun cartographer_ros cartographer_rosbag_validate -bag_filename /root/bags/office_demo_9_25_19.bag

## Run 2D online
# roslaunch demo_cart_2d.launch bag_filename:=/root/bags/office_demo_9_25_19.bag

## Run 2D offline (to generate .pbstream file)
# roslaunch offline_cart_2d.launch bag_filenames:=/root/bags/office_demo_9_25_19.bag

## Run 2D assets_writer
# roslaunch assets_writer_cart_2d.launch bag_filenames:=/root/bags/office_demo_9_25_19.bag  pose_graph_filename:=/root/bags/office_demo_9_25_19.bag.pbstream 

## View output pngs
# xdg-open office_demo_9_25_19.bag_xray_xy_all.png
# xdg-open office_demo_9_25_19.bag_probability_grid.png

## Run 3d online
# roslaunch demo_cart_3d.launch bag_filename:=/root/bags/office_demo_9_25_19.bag

## Run 3d offline
# roslaunch offline_cart_3d.launch bag_filenames:=/root/bags/office_demo_9_25_19.bag 

## Run 3d assets_writer
# roslaunch assets_writer_cart_3d.launch bag_filenames:=/root/bags/office_demo_9_25_19.bag  pose_graph_filename:=/root/bags/office_demo_9_25_19.bag.pbstream 

# xdg-open office_demo_9_25_19.bag_xray_xy_all.png
# xdg-open office_demo_9_25_19.bag_probability_grid.png

