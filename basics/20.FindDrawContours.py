import numpy as np
import cv2

img = cv2.imread('baseball.png')


gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gr, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #find and draw contours

print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(gr, contours, -1, (0, 255, 0), 3)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
