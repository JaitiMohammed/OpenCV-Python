import numpy as np
import cv2 as cv
cap = cv.VideoCapture('TesteRead.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

