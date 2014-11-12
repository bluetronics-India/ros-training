#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist


#Fonction appelée lors de la réception de données
def callback(data):
    print "Speed is currently " + str(data.linear.x)

    ## Pour utiliser le handler ici, il faudra mettre les lignes suivantes dans son open():
    # global handler
    # handler = self

    ## Cela le rendra accessible de partout de le code. Ce n'est pas une bonne pratique mais
    ## c'est le plus simplque que je vois pour faire fonctionner ça ici. Pour l'utiliser, il
    ## faudra faire:
    # if "handler" in globals():
    #   global handler
    #   do stuff with handler



## La node ROS. Lors de la réception d'un message sur le topic /mock_robot_node/mock_vel",
## la fonction callback ci-haut est appelée
class MockRobot:

    def __init__(self):

        rospy.init_node('tornado_server')
        rospy.Subscriber("/mock_robot_node/mock_vel", Twist, callback)

        rospy.loginfo("Starting tornado_server")

        rospy.spin() #Bloquant, c'est-à-dire que le code ne continue pas plus loin



if __name__ == "__main__":

     ## Implémenter l'initialisation de vos serveurs ici. Vous allez devoir utiliser des
     ## threads pour que le code ne bloque pas à votre serveur et continue pour exécuter
     ## la node ROS

    try:
        MockRobot()
    except rospy.ROSInterruptException:
        pass
