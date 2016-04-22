#!/usr/bin/env python

# Python libs
import sys, time

# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy

# Publica imagenes de la camara o de un archivo de video
from sensor_msgs.msg import CompressedImage, Image

def main(args):
  rospy.init_node('camera_pub', anonymous=True)
  pub = rospy.Publisher("/camera", CompressedImage, queue_size=10)
  cap = cv2.VideoCapture(0)
  #cap = cv2.VideoCapture("/home/ernesto/Videos/video1.avi")
  #cap.set(3, 320)
  #cap.set(4, 240)
  rate = rospy.Rate(24)
  while not rospy.is_shutdown():
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow("test", frame)
    cv2.waitKey(1)
    img = frame
    #### Create CompressedIamge ####
    msg = CompressedImage()
    msg.header.stamp = rospy.Time.now()
    msg.format = "jpeg"
    msg.data = np.array(cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 60])[1]).tostring()
    pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
    main(sys.argv)
