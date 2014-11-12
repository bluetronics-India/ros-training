#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist


#Fonction appelée lors de la réception de données
def callback(data):
    print "Speed is currently " + str(data.linear.x)


#La node ROS
class MockRobot:

    def __init__(self):

        rospy.init_node('tornado_server')
        rospy.Subscriber("/mock_robot_node/mock_vel", Twist, callback)

        rospy.loginfo("Starting tornado_server")

        rospy.spin() #Bloquant, c'est-à-dire que le code ne continue pas plus loin



if __name__ == "__main__":

     # Implémenter l'initialisation ici. Vous allez devoir utiliser des threads pour que le code
     # ne bloque pas à votre serveur

    try:
        MockRobot()
    except rospy.ROSInterruptException:
        pass
