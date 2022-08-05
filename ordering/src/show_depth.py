#!/usr/bin/env python
import rospy
import struct
import argparse
import numpy as np
import matplotlib.pyplot    as plt
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg        import PointCloud2
from darknet_ros_msgs.msg   import BoundingBox, BoundingBoxes, fruit
from geometry_msgs.msg      import Vector3


#import geometry_msgs.msg
#from ur3_hardwrare.msg import Tracker

#from std_msgs.msg import Header
#from trajectory_msgs.msg import JointTrajectory
#from trajectory_msgs.msg import JointTrajectoryPoint

#traker = Tracker()

###
# ROS CLASS IMPLEMENTATION
# https://answers.ros.org/question/225008/python-class-for-subscribing-data-for-several-topics/
#

#############################################
# Global Variables                          #
#############################################
bbox    = BoundingBox()
pre_bbox= BoundingBox()
pc      = PointCloud2()
center  = Vector3()
point   = Vector3()
points  = []
depth   = 0.0

def bbox_callback(msg):
    num_box = len(msg.bounding_boxes)
    if num_box>0:
        b         = msg.bounding_boxes[0]
        bbox.xmin = b.xmin
        bbox.xmax = b.xmax
        bbox.ymin = b.ymin
        bbox.ymax = b.ymax
	#bbox.zmin = b.zmin
	#bbox.zmax = b.zmax

def point_callback(msg):
    #global fruit
    global points
    global bbox
    global pre_bbox
    pc.header = msg.header
    pc.height = msg.height
    pc.width  = msg.width
    pc.fields = msg.fields      # channels and their layout
    pc.is_bigendian = msg.is_bigendian
    pc.point_step   = msg.point_step
    pc.row_step     = msg.row_step
    pc.data         = msg.data  #  Actual point data, size is (row_step*height)
    resolution = (pc.height, pc.width)

    
    if bbox.xmin==pre_bbox.xmin and \
        bbox.xmin==pre_bbox.xmin and \
        bbox.xmin==pre_bbox.xmin and \
        bbox.xmin==pre_bbox.xmin:
        pass
    else:
        points = [  ]
        for p in pc2.read_points(msg, skip_nans=False, field_names=("x", "y", "z")):
            points.append(p[2])
        if len(points) == pc.width*pc.height:
            z_points = np.array(points, dtype=np.float32)
            z = z_points.reshape(resolution)

            if not (bbox.xmin==0 and bbox.xmax==0):
                # print('Box: {}, {}'.format(bbox.xmin, bbox.xmax))
		
		# jeongin added
                x_center=((bbox.xmax+bbox.xmin)/2 - 360)
                y_center=((bbox.ymax+bbox.ymin)/2 - 320)
                z_box = z[bbox.xmin:bbox.xmax, bbox.ymin:bbox.ymax]
                z_value = z_box[~np.isnan(z_box)]
                distance = min(z_value)
		z_distance = int (distance * 100)
                #print('Box_Center: x {}, y {}, z {}'.format(x_center,y_center,z_distance))

		pub = rospy.Publisher("/fruit_position", fruit, queue_size=10)
	        rate = rospy.Rate(30)
                
	        pos = fruit()

		pos.xpos = x_center
		pos.ypos = y_center
		pos.zpos = z_distance
		pos.zdistance = z_distance

		rospy.loginfo("fruit")
		rospy.loginfo("X: %d", pos.xpos)
		rospy.loginfo("Y: %d", pos.ypos)
		rospy.loginfo("Z: %d", pos.zpos)
		rospy.loginfo("D: %d", pos.zdistance)

		pub.publish(pos)

		#print('z {}'.format(z_box))
                #print('Distance: {}'.format(distance))

        pre_bbox.xmin = bbox.xmin
        pre_bbox.xmax = bbox.xmax
        pre_bbox.ymin = bbox.ymin
        pre_bbox.ymax = bbox.ymax



def main(args):
    rospy.init_node('Fruit_position', anonymous=True)

    point_sub   = rospy.Subscriber('camera/depth_registered/points', PointCloud2, point_callback)
    bbox_sub    = rospy.Subscriber('darknet_ros/bounding_boxes', BoundingBoxes, bbox_callback)    

    pub = rospy.Publisher('fruit_position', fruit, queue_size=10)

    rate = rospy.Rate(30)
    pos = fruit()

#    while not rospy.is_shutdown():
#	pos.xpos = x_center
#	pos.ypos = y_center
#	pos.zpos = z_distance
#	pos.zdistance = z_distance
#	
#	rospy.loginfo("fruit")
#	rospy.loginfo("X: %d", pos.xpos)
#	rospy.loginfo("Y: %d", pos.ypos)
#	rospy.loginfo("Z: %d", pos.zpos)
#	rospy.loginfo("D: %d", pos.zdistance)
#
#	pub.publish(pos)
#
#	rate.sleep()

#    freq = 1
#    rate = rospy.Rate(freq)

    while not rospy.is_shutdown():
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Output Depth of an Target Object')
    args = parser.parse_args()
    main(args)
