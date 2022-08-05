#!/usr/bin/python

import rospy
import argparse
from darknet_ros_msgs.msg import testing, testing_ar


f = open("order.txt",'r')
order = f.readlines()
f.close()

order = list(map(int, order))

global order0, order1, order2, order3, order4, order5, order6, order7
order0 = order[0]


def position_callback(msg):
	pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
	rate = rospy.Rate(30)
	pos = testing_ar()	

	if (order[0] == 0):
		pos.xpos1 = msg.xpos1
		pos.ypos1 = msg.ypos1
		pos.zpos1 = msg.zpos1
		pos.zdistance1 = msg.zdistance1	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)

	elif (order[0] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos2
		pos.ypos1 = msg.ypos2
		pos.zpos1 = msg.zpos2
		pos.zdistance1 = msg.zdistance2	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos3
		pos.ypos1 = msg.ypos3
		pos.zpos1 = msg.zpos3
		pos.zdistance1 = msg.zdistance3	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos4
		pos.ypos1 = msg.ypos4
		pos.zpos1 = msg.zpos4
		pos.zdistance1 = msg.zdistance4	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos5
		pos.ypos1 = msg.ypos5
		pos.zpos1 = msg.zpos5
		pos.zdistance1 = msg.zdistance5	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos6
		pos.ypos1 = msg.ypos6
		pos.zpos1 = msg.zpos6
		pos.zdistance1 = msg.zdistance6	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos7
		pos.ypos1 = msg.ypos7
		pos.zpos1 = msg.zpos7
		pos.zdistance1 = msg.zdistance7	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos8
		pos.ypos1 = msg.ypos8
		pos.zpos1 = msg.zpos8
		pos.zdistance1 = msg.zdistance8	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


	elif (order[0] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos1 = msg.xpos9
		pos.ypos1 = msg.ypos9
		pos.zpos1 = msg.zpos9
		pos.zdistance1 = msg.zdistance9	

		rospy.loginfo("fruit1")
		rospy.loginfo("X: %d", pos.xpos1)
		rospy.loginfo("Y: %d", pos.ypos1)
		rospy.loginfo("Z: %d", pos.zpos1)
		rospy.loginfo("D: %d", pos.zdistance1)

#		pub.publish(pos)


#######################################################

	if (order[1] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos1
		pos.ypos2 = msg.ypos1
		pos.zpos2 = msg.zpos1
		pos.zdistance2 = msg.zdistance1	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos2
		pos.ypos2 = msg.ypos2
		pos.zpos2 = msg.zpos2
		pos.zdistance2 = msg.zdistance2	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos3
		pos.ypos2 = msg.ypos3
		pos.zpos2 = msg.zpos3
		pos.zdistance2 = msg.zdistance3	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos4
		pos.ypos2 = msg.ypos4
		pos.zpos2 = msg.zpos4
		pos.zdistance2 = msg.zdistance4	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos5
		pos.ypos2 = msg.ypos5
		pos.zpos2 = msg.zpos5
		pos.zdistance2 = msg.zdistance5	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos6
		pos.ypos2 = msg.ypos6
		pos.zpos2 = msg.zpos6
		pos.zdistance2 = msg.zdistance6	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos7
		pos.ypos2 = msg.ypos7
		pos.zpos2 = msg.zpos7
		pos.zdistance2 = msg.zdistance7	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos8
		pos.ypos2 = msg.ypos8
		pos.zpos2 = msg.zpos8
		pos.zdistance2 = msg.zdistance8	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

	elif (order[1] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos2 = msg.xpos9
		pos.ypos2 = msg.ypos9
		pos.zpos2 = msg.zpos9
		pos.zdistance2 = msg.zdistance9	

		rospy.loginfo("fruit2")
		rospy.loginfo("X: %d", pos.xpos2)
		rospy.loginfo("Y: %d", pos.ypos2)
		rospy.loginfo("Z: %d", pos.zpos2)
		rospy.loginfo("D: %d", pos.zdistance2)

#		pub.publish(pos)

####################################################################3

	if (len(order) > 2 and order[2] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos1
		pos.ypos3 = msg.ypos1
		pos.zpos3 = msg.zpos1
		pos.zdistance3 = msg.zdistance1	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos2
		pos.ypos3 = msg.ypos2
		pos.zpos3 = msg.zpos2
		pos.zdistance3 = msg.zdistance2	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos3
		pos.ypos3 = msg.ypos3
		pos.zpos3 = msg.zpos3
		pos.zdistance3 = msg.zdistance3	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos4
		pos.ypos3 = msg.ypos4
		pos.zpos3 = msg.zpos4
		pos.zdistance3 = msg.zdistance4	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos5
		pos.ypos3 = msg.ypos5
		pos.zpos3 = msg.zpos5
		pos.zdistance3 = msg.zdistance5	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos6
		pos.ypos3 = msg.ypos6
		pos.zpos3 = msg.zpos6
		pos.zdistance3 = msg.zdistance6	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos7
		pos.ypos3 = msg.ypos7
		pos.zpos3 = msg.zpos7
		pos.zdistance3 = msg.zdistance7	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos8
		pos.ypos3 = msg.ypos8
		pos.zpos3 = msg.zpos8
		pos.zdistance3 = msg.zdistance8	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

	elif (len(order) > 2 and order[2] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos3 = msg.xpos9
		pos.ypos3 = msg.ypos9
		pos.zpos3 = msg.zpos9
		pos.zdistance3 = msg.zdistance9	

		rospy.loginfo("fruit3")
		rospy.loginfo("X: %d", pos.xpos3)
		rospy.loginfo("Y: %d", pos.ypos3)
		rospy.loginfo("Z: %d", pos.zpos3)
		rospy.loginfo("D: %d", pos.zdistance3)

#		pub.publish(pos)

#########################################################

	if (len(order) > 3 and order[3] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos1
		pos.ypos4 = msg.ypos1
		pos.zpos4 = msg.zpos1
		pos.zdistance4 = msg.zdistance1	
		
		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos2
		pos.ypos4 = msg.ypos2
		pos.zpos4 = msg.zpos2
		pos.zdistance4 = msg.zdistance2	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos3
		pos.ypos4 = msg.ypos3
		pos.zpos4 = msg.zpos3
		pos.zdistance4 = msg.zdistance3	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos4
		pos.ypos4 = msg.ypos4
		pos.zpos4 = msg.zpos4
		pos.zdistance4 = msg.zdistance4	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos5
		pos.ypos4 = msg.ypos5
		pos.zpos4 = msg.zpos5
		pos.zdistance4 = msg.zdistance5	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos6
		pos.ypos4 = msg.ypos6
		pos.zpos4 = msg.zpos6
		pos.zdistance4 = msg.zdistance6	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos7
		pos.ypos4 = msg.ypos7
		pos.zpos4 = msg.zpos7
		pos.zdistance4 = msg.zdistance7	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos8
		pos.ypos4 = msg.ypos8
		pos.zpos4 = msg.zpos8
		pos.zdistance4 = msg.zdistance8	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

	elif (len(order) > 3 and order[3] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos4 = msg.xpos9
		pos.ypos4 = msg.ypos9
		pos.zpos4 = msg.zpos9
		pos.zdistance4 = msg.zdistance9	

		rospy.loginfo("fruit4")
		rospy.loginfo("X: %d", pos.xpos4)
		rospy.loginfo("Y: %d", pos.ypos4)
		rospy.loginfo("Z: %d", pos.zpos4)
		rospy.loginfo("D: %d", pos.zdistance4)

#		pub.publish(pos)

#####################################################

	if (len(order) > 4 and order[4] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos1
		pos.ypos5 = msg.ypos1
		pos.zpos5 = msg.zpos1
		pos.zdistance5 = msg.zdistance1	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos2
		pos.ypos5 = msg.ypos2
		pos.zpos5 = msg.zpos2
		pos.zdistance5 = msg.zdistance2	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos3
		pos.ypos5 = msg.ypos3
		pos.zpos5 = msg.zpos3
		pos.zdistance5 = msg.zdistance3	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos4
		pos.ypos5 = msg.ypos4
		pos.zpos5 = msg.zpos4
		pos.zdistance5 = msg.zdistance4	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos5
		pos.ypos5 = msg.ypos5
		pos.zpos5 = msg.zpos5
		pos.zdistance5 = msg.zdistance5	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos6
		pos.ypos5 = msg.ypos6
		pos.zpos5 = msg.zpos6
		pos.zdistance5 = msg.zdistance6	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos7
		pos.ypos5 = msg.ypos7
		pos.zpos5 = msg.zpos7
		pos.zdistance5 = msg.zdistance7	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos8
		pos.ypos5 = msg.ypos8
		pos.zpos5 = msg.zpos8
		pos.zdistance5 = msg.zdistance8	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

	elif (len(order) > 4 and order[4] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos5 = msg.xpos9
		pos.ypos5 = msg.ypos9
		pos.zpos5 = msg.zpos9
		pos.zdistance5 = msg.zdistance9	

		rospy.loginfo("fruit5")
		rospy.loginfo("X: %d", pos.xpos5)
		rospy.loginfo("Y: %d", pos.ypos5)
		rospy.loginfo("Z: %d", pos.zpos5)
		rospy.loginfo("D: %d", pos.zdistance5)

#		pub.publish(pos)

#######################################################

	if (len(order) > 5 and order[5] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos1
		pos.ypos6 = msg.ypos1
		pos.zpos6 = msg.zpos1
		pos.zdistance6 = msg.zdistance1	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

#		pub.publish(pos)

	elif (len(order) > 5 and order[5] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos2
		pos.ypos6 = msg.ypos2
		pos.zpos6 = msg.zpos2
		pos.zdistance6 = msg.zdistance2	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

#		pub.publish(pos)

	elif (len(order) > 5 and order[5] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos3
		pos.ypos6 = msg.ypos3
		pos.zpos6 = msg.zpos3
		pos.zdistance6 = msg.zdistance3	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

#		pub.publish(pos)

	elif (len(order) > 5 and order[5] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos4
		pos.ypos6 = msg.ypos4
		pos.zpos6 = msg.zpos4
		pos.zdistance6 = msg.zdistance4	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

#		pub.publish(pos)

	elif (len(order) > 5 and order[5] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos5
		pos.ypos6 = msg.ypos5
		pos.zpos6 = msg.zpos5
		pos.zdistance6 = msg.zdistance5	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

		#pub.publish(pos)

	elif (len(order) > 5 and order[5] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos6
		pos.ypos6 = msg.ypos6
		pos.zpos6 = msg.zpos6
		pos.zdistance6 = msg.zdistance6	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

		#pub.publish(pos)

	elif (len(order) > 5 and order[5] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos7
		pos.ypos6 = msg.ypos7
		pos.zpos6 = msg.zpos7
		pos.zdistance6 = msg.zdistance7	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

		#pub.publish(pos)

	elif (len(order) > 5 and order[5] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos8
		pos.ypos6 = msg.ypos8
		pos.zpos6 = msg.zpos8
		pos.zdistance6 = msg.zdistance8	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

		#pub.publish(pos)

	elif (len(order) > 5 and order[5] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos6 = msg.xpos9
		pos.ypos6 = msg.ypos9
		pos.zpos6 = msg.zpos9
		pos.zdistance6 = msg.zdistance9	

		rospy.loginfo("fruit6")
		rospy.loginfo("X: %d", pos.xpos6)
		rospy.loginfo("Y: %d", pos.ypos6)
		rospy.loginfo("Z: %d", pos.zpos6)
		rospy.loginfo("D: %d", pos.zdistance6)

		#pub.publish(pos)

#######################################################

	if (len(order) > 6 and order[6] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos1
		pos.ypos7 = msg.ypos1
		pos.zpos7 = msg.zpos1
		pos.zdistance7 = msg.zdistance1	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos2
		pos.ypos7 = msg.ypos2
		pos.zpos7 = msg.zpos2
		pos.zdistance7 = msg.zdistance2	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos3
		pos.ypos7 = msg.ypos3
		pos.zpos7 = msg.zpos3
		pos.zdistance7 = msg.zdistance3	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos4
		pos.ypos7 = msg.ypos4
		pos.zpos7 = msg.zpos4
		pos.zdistance7 = msg.zdistance4	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos5
		pos.ypos7 = msg.ypos5
		pos.zpos7 = msg.zpos5
		pos.zdistance7 = msg.zdistance5	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos6
		pos.ypos7 = msg.ypos6
		pos.zpos7 = msg.zpos6
		pos.zdistance7 = msg.zdistance6	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos7
		pos.ypos7 = msg.ypos7
		pos.zpos7 = msg.zpos7
		pos.zdistance7 = msg.zdistance7	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos8
		pos.ypos7 = msg.ypos8
		pos.zpos7 = msg.zpos8
		pos.zdistance7 = msg.zdistance8	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

	elif (len(order) > 6 and order[6] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos7 = msg.xpos9
		pos.ypos7 = msg.ypos9
		pos.zpos7 = msg.zpos9
		pos.zdistance7 = msg.zdistance9	

		rospy.loginfo("fruit7")
		rospy.loginfo("X: %d", pos.xpos7)
		rospy.loginfo("Y: %d", pos.ypos7)
		rospy.loginfo("Z: %d", pos.zpos7)
		rospy.loginfo("D: %d", pos.zdistance7)

		#pub.publish(pos)

##########################################################

	if (len(order) > 7 and order[7] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos1
		pos.ypos8 = msg.ypos1
		pos.zpos8 = msg.zpos1
		pos.zdistance8 = msg.zdistance1	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos2
		pos.ypos8 = msg.ypos2
		pos.zpos8 = msg.zpos2
		pos.zdistance8 = msg.zdistance2	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos3
		pos.ypos8 = msg.ypos3
		pos.zpos8 = msg.zpos3
		pos.zdistance8 = msg.zdistance3	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos4
		pos.ypos8 = msg.ypos4
		pos.zpos8 = msg.zpos4
		pos.zdistance8 = msg.zdistance4	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos5
		pos.ypos8 = msg.ypos5
		pos.zpos8 = msg.zpos5
		pos.zdistance8 = msg.zdistance5	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos6
		pos.ypos8 = msg.ypos6
		pos.zpos8 = msg.zpos6
		pos.zdistance8 = msg.zdistance6	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos7
		pos.ypos8 = msg.ypos7
		pos.zpos8 = msg.zpos7
		pos.zdistance8 = msg.zdistance7	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos8
		pos.ypos8 = msg.ypos8
		pos.zpos8 = msg.zpos8
		pos.zdistance8 = msg.zdistance8	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

	elif (len(order) > 7 and order[7] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos8 = msg.xpos9
		pos.ypos8 = msg.ypos9
		pos.zpos8 = msg.zpos9
		pos.zdistance8 = msg.zdistance9	

		rospy.loginfo("fruit8")
		rospy.loginfo("X: %d", pos.xpos8)
		rospy.loginfo("Y: %d", pos.ypos8)
		rospy.loginfo("Z: %d", pos.zpos8)
		rospy.loginfo("D: %d", pos.zdistance8)

		#pub.publish(pos)

#######################################################

	if (len(order) > 8 and order[8] == 0):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos1
		pos.ypos9 = msg.ypos1
		pos.zpos9 = msg.zpos1
		pos.zdistance9 = msg.zdistance1	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 1):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos2
		pos.ypos9 = msg.ypos2
		pos.zpos9 = msg.zpos2
		pos.zdistance9 = msg.zdistance2	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 2):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos3
		pos.ypos9 = msg.ypos3
		pos.zpos9 = msg.zpos3
		pos.zdistance9 = msg.zdistance3	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 3):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos4
		pos.ypos9 = msg.ypos4
		pos.zpos9 = msg.zpos4
		pos.zdistance9 = msg.zdistance4	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 4):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos5
		pos.ypos9 = msg.ypos5
		pos.zpos9 = msg.zpos5
		pos.zdistance9 = msg.zdistance5	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 5):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos6
		pos.ypos9 = msg.ypos6
		pos.zpos9 = msg.zpos6
		pos.zdistance9 = msg.zdistance6	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 6):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos7
		pos.ypos9 = msg.ypos7
		pos.zpos9 = msg.zpos7
		pos.zdistance9 = msg.zdistance7	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 7):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos8
		pos.ypos9 = msg.ypos8
		pos.zpos9 = msg.zpos8
		pos.zdistance9 = msg.zdistance8	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

		#pub.publish(pos)

	elif (len(order) > 8 and order[8] == 8):
#		pub = rospy.Publisher("/pos_pub", testing_ar, queue_size=10)
#		rate = rospy.Rate(30)
#		pos = testing_ar()	

		pos.xpos9 = msg.xpos9
		pos.ypos9 = msg.ypos9
		pos.zpos9 = msg.zpos9
		pos.zdistance9 = msg.zdistance9	

		rospy.loginfo("fruit9")
		rospy.loginfo("X: %d", pos.xpos9)
		rospy.loginfo("Y: %d", pos.ypos9)
		rospy.loginfo("Z: %d", pos.zpos9)
		rospy.loginfo("D: %d", pos.zdistance9)	

	pub.publish(pos)

#########################################################
	
def main(args):
	rospy.init_node("publisher", anonymous=True)
	pos_sub = rospy.Subscriber("/fruit_position", testing, position_callback)

	while not rospy.is_shutdown():
		pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Output Depth of an Target Object')
	args = parser.parse_args()
	main(args)


	

	
