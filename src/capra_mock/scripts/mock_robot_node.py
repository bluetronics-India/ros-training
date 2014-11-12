#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist


class MockRobot:

    def __init__(self):

        rospy.init_node('mock_robot_node')

        pub_robot_vel = rospy.Publisher("~mock_vel", Twist, queue_size=10)

        rate = 5
        r = rospy.Rate(rate)

        rospy.loginfo("Starting mock_robot_node. Message rate(hz): " + str(r))

        speed = 0.0

        while not rospy.is_shutdown():
            vel = Twist()
            vel.linear.x = speed
            pub_robot_vel.publish(vel)

            speed += 0.1
            if speed > 10:
                speed = 0

            r.sleep()
        rospy.spin()

if __name__ == "__main__":
    try:
        MockRobot()
    except rospy.ROSInterruptException:
        pass
