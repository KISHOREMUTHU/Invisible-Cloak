# Importing Libraries

import numpy as np
import cv2


import time # To provide time for capturing the background
cap =cv2.VideoCapture(0)
time.sleep(3)
bg = 0
for i in range(30):
      ret,bg = cap.read()

while(cap.isOpened()):
      ret ,img = cap.read()

      if not ret:
            break

      hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
      # Hue Saturation value or Hue Saturation Brightness

      #HSV values
      lower_red = np.array([0,120,70])
      upper_red = np.array([10,255,255])
      mask1 = cv2.inRange(hsv,lower_red,upper_red) # Separating the  cloak part
      lower_red = np.array([170,120,70])
      upper_red = np.array([180,255,255])
      mask2 = cv2.inRange(hsv,lower_red,upper_red)
      mask1 = mask1 + mask2
      mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,np.ones((3,3), np.uint8),iterations=2) # Noise Removal
      mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3), np.uint8),iterations=2)# Improving the smoothness of the image
      mask2 = cv2.bitwise_not(mask1)
      res1 = cv2.bitwise_and(bg,bg,mask=mask1)
      res2 =cv2.bitwise_and(img,img,mask = mask2)
      final_output = cv2.addWeighted(res1,1,res2,1,0)
      cv2.imshow('Output',final_output)
      k=cv2.waitKey(10)
      if(k == 27):
            break

cap.release()
cv2.destroyAllWindows()



