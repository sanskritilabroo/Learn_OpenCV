import numpy as np
import cv2 as cv

def nothing(x):
    print(x) #simple print function

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

#create 3 trackbars that print the values they display
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'  #adding a switch
cv.createTrackbar(switch, 'image', 0, 1, nothing) #switch goes from 0 to 1 and only prints 0 or 1

while(1): #loop for switch
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

#these trackbars return the trackbarpos and change color according to position
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0: #if condition for switch
       img[:] = 0
    else:
       img[:] = [b, g, r]


cv.destroyAllWindows()