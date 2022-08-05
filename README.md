# cucumber_detection


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

* cucumber weights file [DOWNLOAD](https://drive.google.com/file/d/1RSzCzxxeflkGGB4y9GMLQCJY_EiZE-id/view?usp=sharing)
```
Add in yolo_network_config/weights/cucumber.weights
```


```
$ cd ~/catkin_ws/src
$ git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
$ cd ..
$ catkin_make

* perception
terminal 1
$ roslaunch darknet_ros object_detection.launch

terminal 2
* estimate position 
$ rosrun darknet_ros show_depth.py

terminal 3
* ordering
$ cd ~/catkin_ws/src/ordering/src
$ rosrun ordering GAorder -g 10 -p 10 -k 10 -m 10
$ ^C

terminal 4
$ cd ~/catkin_we/src/ordering/src
$ rosrun ordering publisher.py
```



