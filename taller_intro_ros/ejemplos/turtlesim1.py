#!/usr/bin/env python

# Tortuga que se mueve al azar

import rospy, math, random, time
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('square_turtle', anonymous=True)
    while not rospy.is_shutdown():
        rospy.loginfo("Moviendo la tortuga...")
        mensaje = Twist()
        mensaje.linear.x = random.random()*2 + 0.1
        pub.publish(mensaje)
        rospy.sleep(2)
        mensaje = Twist()
        mensaje.angular.z = random.random()*3
        pub.publish(mensaje)
        rospy.sleep(2)

if __name__ == '__main__':
   talker()
