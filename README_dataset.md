# ISA Rescue dataset



Paper:

## Overview

The dataset is classified in different folders by scenario and sequence. 
Each sequence has a name corresponding to its content. Inside each sequence 
there are different directories for each "device" (i.e. rgb image, imu, ...).

The different available devices are:

* RGB realistic stereo camera.

* RGB tagged stereo camera.

* Inertial Measurement Unit (IMU).

* LiDAR OS1.

* Global Positioning System (GPS).

* Wheel tachometers.

In every case the timestamp is the ROS time recorded in the original rosbag file for that message.

## Images

The dataset contains two sets of stereo images. One corresponds to the RGB spectrum and the other is the label information.
The name convention followed is:

    timestamp_camera.jpg
and for the labeled one:
    timestamp_camera_tag.jpg

The images are stored in different directories named:

    img_right/

    img_right_tag/

    img_left/

    img_left_atg/

The capture ratio is 25 fps for both cameras. The image sizes are 1280x720 pixels for both cameras.  

## IMU

The data from the IMU is stored in a single "imu_data.txt" file inside `imu/` directory for each sequence. The file stores the messages as successive lines.
The structure for each line is:

    timestamp quaternion.x quaternion.y quaternion.z ang_vel_X ang_vel_Y ang_vel_Z lin_acc_X lin_acc_Y lin_acc_Z

- Roll, pitch and yaw are in rad and about fixed axes XYZ.

- Angular velocities (ang_vel_{X, Y, Z}) are in rad/sec.

- Linear accelerations (lin_acc_{X, Y, Z}) are in m/s².

The capture ratio is 50 .

## OS1 points

Each message is stored in one .csv file as a Nx4 matrix (being N the number of points per message) following the next convention:

    x y z intensity

- x, y and z are the position respect the Velodyne sensor in meters.

- The intensity correponds to one of the 15 classes.

-

They are stored in the folder `lidar/`. The name convention followed is:

    timestamp.csv

In order to open and parse the data from the binary file, the followings commands are examples of use:

* `numpy:`

```python
    import numpy as np
    
    points = np.fromfile(filename, dtype=np.float32).reshape(-1, 4)
```

* `MATLAB:`

```matlab
    fileID = fopen(filename, 'r');
    format = 'float32';
    data = fread(fileID, Inf, format);
    xyzi=reshape(data,4,length(data)/4)';
```

## GPS

The data from the GPS is stored in a single "GPS_data.txt" file inside `GPS/` directory for each sequence. The file stores the messages as successive lines.
The structure for each line is:

    timestamp latitude longitude altitude

## Position_ground_truth
The data from the exact positon of the "base_link" of the robot in the Gazebo globlal reference system. The file stores the messages as successive lines.
The structure for each line is:

    timestamp position_x position_y position_z orientation_x orientation_y orientation_z orientation_w
 

## Sequence extractor

The following [repository](https://github.com/davdmc/extract_sequence) offers tools to extract sub-sequences from each sequence. This can be used to separate data for an specific purpose (e.g. scenes with/without movement only, scenes with/without a semantic class as people or cars ...).

Detailed information about the usage of the tools are included in the repository. Two scripts can be used:

- `extract_single.py:` script to extract data from a single sequence. It recieves several options (see extract_single_options.py).

- `extract_file.py:` script to automate the process of extracting data from multiple sequences. It uses a .txt file as a single parameter with a specific format to describe the different sequences that can be shared and edited (see [Extraction format](https://github.com/davdmc/extract_sequence#extraction-format) or [extraction_format.txt](https://github.com/davdmc/extract_sequence/blob/master/extraction_format.txt)).

### Specific rules for extraction format

In the case of this dataset the extraction format for `extract_file` must follow these rules:

- `folder:` it corresponds to the specific sequence under the year/day/sequence path convention.

- `devices and formats:` the devices with their correspondent formats are listed below. The number of devices to extract is optional. The user may choose which devices to extract depending on the usage of the extracted sequence. If the device is assigned a wrong data format the data will be extracted wrong or an error will appear.

    |      Device     |   Data format  |
    |:---------------:|:--------------:|
    |    image_rgb    | multiple_files |
    |    image_the    | multiple_files |
    |       imu       |   single_file  |
    | velodyne_points | multiple_files |
    |     gps_user    |   single_file  |
    |     gps_rtk     |   single_file  |

- `intervals:` must be in the same time units as the correspondent in the file names or "data.txt" files.
