import numpy as np
import cv2 


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('interest.avi',fourcc, 20.0, (640,480))
out2 = cv2.VideoWriter('background.avi',fourcc, 20.0, (640,480))


upper_left = (50, 50)
bottom_right = (300, 300)

def region_of_background(image):
	mask = np.zeros_like(image)
	rect= cv2.rectangle(mask, upper_left, bottom_right, (255,255,255), cv2.FILLED)
	masked_image=cv2.bitwise_and(image,mask)
	out2.write(masked_image)
	return masked_image
    
def region_of_interest(image):
        r = cv2.rectangle(image, upper_left, bottom_right, (255,255,255), cv2.FILLED)
        out1.write(image)
        return image

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    imgcopy1 = np.copy(frame)
    imgcopy2 = np.copy(frame)
    img1 = region_of_interest(imgcopy1)
    img2 = region_of_background(imgcopy2)
    # Display the resulting frame
    cv2.imshow('interest',img1)
    cv2.imshow('background',img2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()

