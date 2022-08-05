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

* darknet_ros
```
$ cd ~/catkin_ws/src
$ git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
$ cd ..
$ catkin_make -DCMAKE_BUILD_TYPE=Release
```

* cucumber_detection
```
$ git clone https://github.com/hgnoej/cucumber_detection.git
$ cd cucumber_detection/darknet_ros

in config directory
$ cp -r ros.yaml ~/catkin_ws/src/darknet_ros/darknets_ros/config
$ cp -r cucumber.yaml ~/catkin_ws/src/darknet_ros/darknets_ros/config

in launch directory
$ cp -r bringup_d435.launch ~/catkin_ws/src/darknet_ros/darknet_ros/launch
$ cp -r darknet_ros.launch ~/catkin_ws/src/darknet_ros/darknet_ros/launch
$ cp -r object_detection.launch ~/catkin_ws/src/darknet_ros/darknet_ros/launch

in yolo_network_config/cfg/
$ cp -r cucumber.cfg ~/catkin_ws/src/darknet_ros/darknet_ros/cfg
```


