#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def lidar_callback(data):
    rospy.loginfo("Received LiDAR data: %s", data.ranges)

def lidar_listener():
    rospy.init_node('lidar_listener', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, lidar_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_listener()
    except rospy.ROSInterruptException:
        pass
