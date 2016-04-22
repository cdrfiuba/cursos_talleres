#!/usr/bin/env python

# Se suscriba a un flujo de video y lo muestra

import rospy, cv2
import numpy as np

from sensor_msgs.msg import CompressedImage

class image_converter:
  def __init__(self):
    self.image_sub = rospy.Subscriber("/camera", CompressedImage, self.callback)

  def callback(self, data):
    #### direct conversion to CV2 ####
    np_arr = np.fromstring(data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
    cv2.imshow("ImageWindow", image_np)
    cv2.waitKey(1)

def main():
  cv2.namedWindow("ImageWindow")
  ic = image_converter()
  rospy.init_node('image_receiver', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
