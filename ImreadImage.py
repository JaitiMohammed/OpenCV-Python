import cv2
import numpy as np 
img =cv2.imread('fleurs.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('fleurs.png',img)
    cv2.destroyAllWindows()
