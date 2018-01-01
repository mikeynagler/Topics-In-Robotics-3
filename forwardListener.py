#!/usr/bin/env python
import rospy

from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

goForwardFlag = 0

def callback(data):
	global goForwardFlag
	center=data.ranges[len(data.ranges)/2]
	rospy.loginfo(center)
	msg = Twist()
	if( center>0.5 and goForwardFlag):
		goForwardFlag=0
		msg.linear.x = 0.45
		pub.publish(msg)
	elif(goForwardFlag):
		msg.linear.x = 0.0

	

def goForward(data):
	global goForwardFlag
	goForwardFlag=1
	rospy.Subscriber("/scan", LaserScan, callback)
	


if __name__ == '__main__':
	rospy.init_node('forwardNode', anonymous=True)	
	rospy.Subscriber('moveForwardTopic', Bool, goForward)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	rospy.spin()
