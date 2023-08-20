import numpy as np
#img=np.zeros([512,512,3],np.uint8) #if we want shapes on a plain black image screen
import cv2
img=cv2.imread("lena.jpg", 1) #to read the image in color

img =cv2.line(img,(0,0),(255,255),(147,96,44), 10)
img =cv2.arrowedLine(img,(0,255),(400,420),(255,0,0), 10)
img =cv2.rectangle(img,(384,0),(510,128),(0,0,255),10)
img=cv2.circle(img,(447,63),63,(0,255,0),-1)

font=cv2.FONT_HERSHEY_SIMPLEX #font style

#adding text to the image
#OpenCV is the word to display, 10,500 is the coordinates or location of text, 0,255,255 is text color
#10 is font thickness
img=cv2.putText(img,"OpenCV",(10,500),font,4,(0,255,255),10,cv2.LINE_4)

cv2.imshow("image",img) #displays image with shapes on it
cv2.waitKey(0)
cv2.destroyAllWindows()