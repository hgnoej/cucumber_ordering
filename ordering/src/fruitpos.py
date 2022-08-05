#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
#import time
#import random
from darknet_ros_msgs.msg import BoundingBoxes, BoundingBox, fruit
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import PoseArray, Pose
#import tf
#from enum import Enum


def fruit_pos_callback(data):
    rospy.loginfo("-----")
    rospy.loginfo("X: %d", data.xpos)


def main():
    rospy.init_node('subscribe_pos', anonymous=False)
    rospy.Subscriber("fruit_position", fruit, fruit_pos_callback)

    rospy.spin()

  
if __name__ == '__main__':
   try:
	main()
   except rospy.ROSInterruptException:
	pass
