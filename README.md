# Cucumber_ordering


## Installation
### Dependencies
* [CUDA](https://developer.nvidia.com/cuda-toolkit-archive)

* Make packages
```
$ mkdir -p ~/catkin_ws/src
$ cd catkin_ws
$ catkin_make
```
* [IntelRealSense](https://github.com/IntelRealSense/realsense-ros)
* [Cucumber detection](https://github.com/hgnoej/cucumber_detection)
* Ordering
```
$ cd ~/catkin_ws/src
$ git clone -- https://github.com/hgnoej/cucumber_ordering.git
$ unzip darknet_ros.zip
$ mv darknet_ros ordering ~/catkin_ws/src/
$ cd ..
$ catkin_make

# terminal 1
* perception
$ roslaunch darknet_ros object_detection.launch

# terminal 2
* estimate position 
$ rosrun darknet_ros show_depth.py

# terminal 3
* ordering
$ cd ~/catkin_ws/src/ordering/src
$ rosrun ordering GAorder -g 10 -p 10 -k 10 -m 10
$ ^C

# terminal 4
$ cd ~/catkin_we/src/ordering/src
$ rosrun ordering publisher.py
```

* Cucumber weights file [DOWNLOAD](https://drive.google.com/file/d/1RSzCzxxeflkGGB4y9GMLQCJY_EiZE-id/view?usp=sharing)
```
Add in yolo_network_config/weights/cucumber.weights
```



