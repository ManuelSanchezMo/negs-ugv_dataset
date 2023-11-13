cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
project(husky_tachometers)
find_package(roscpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(hector_gazebo_plugins REQUIRED)
find_package(message_generation)
include_directories(${roscpp_INCLUDE_DIRS})
include_directories(${std_msgs_INCLUDE_DIRS})
include_directories(${sensor_msgs_INCLUDE_DIRS})
include_directories(${hector_gazebo_plugins_INCLUDE_DIRS})

include_directories(include ${catkin_INCLUDE_DIRS})
# Find Gazebo
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")
 add_message_files(
   FILES
	Encoder.msg
 )

generate_messages(
   DEPENDENCIES
   geometry_msgs
	sensor_msgs
	nav_msgs
	std_msgs
)

# Build our plugin
add_library(encoder_plugin  src/encoderPlugin.cpp)
target_link_libraries(encoder_plugin ${GAZEBO_LIBRARIES} ${roscpp_LIBRARIES})





