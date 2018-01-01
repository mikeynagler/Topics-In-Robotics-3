#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pi

def turnAround(data):
	speed = 10
	angular_speed = math.radians(speed)

	msg = Twist()
	msg.angular.z = -abs(angular_speed)

	t0 = rospy.Time.now().to_sec()
	current_angle = 0
	
	angle = float(data.data)
	relative_angle = math.radians(angle)
	deviation = 0.01*math.radians(angle)
	while(current_angle < relative_angle):
		pub.publish(msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angular_speed*(t1-t0)+deviation
	msg.angular.z = 0
	pub.publish(msg)

if __name__ == '__main__':
	rospy.init_node('turnningNode', anonymous=True)	
	rospy.Subscriber('turnAroundTopic', Float32, turnAround)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	rospy.spin()

