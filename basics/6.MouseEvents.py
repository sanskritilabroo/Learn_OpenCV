import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #adding left click functionality
        print(x,', ' ,y) #this code prints coordinates of place clicked
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2)
        #strXY is the text,
        #  x,y is location
        # 1 is font size
        # 2 is font thickness
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN: #adding right click functionality
        blue = img[y, x, 0] #blue is the first channel
        green = img[y, x, 1] #green is the second channel
        red = img[y, x, 2] #red is the third channel
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img) #points to BGR values at a certain location when clicked

cv2.setMouseCallback('image', click_event) #calling the function whenever mouse is clicked

cv2.waitKey(0)
cv2.destroyAllWindows()