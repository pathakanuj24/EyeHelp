import cv2

import numpy as np

keyboard = np.zeros((1000,1500,3), np.uint8)

# making keys for keyboard 

cv2.rectangle(keyboard,(0,0),(200,200),(255,0,0),3)

rectangle = {1,2,3}













cv2.imshow("Keyboard", keyboard)
cv2.waitKey(0)
cv2.destroyAllWindows()