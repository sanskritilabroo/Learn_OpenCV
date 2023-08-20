import cv2
import numpy as np

cap = cv2.VideoCapture('tennis.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

   diff = cv2.absdiff(frame1, frame2)
   # used to find the absolute difference b/w first and second color
   diff = cv2.cvtColor(diff, cv2.COLOR_BGR2HSV) #convert bgr image to hsv
   diff = cv2.inRange(diff, (25, 130, 130), (37, 255, 255)) #lower and higher values for colour of ball
   # converts this difference to a gray color
   blur = cv2.GaussianBlur(diff, (5, 5), 0)
   # 5,5 is the ksize and 0 is the sigma x value
   _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
   # 20 is threshold, 255 is max value, type is binary thresh
   dilated = cv2.dilate(thresh, None, iterations=3)
   # dilate to fill in all the holes which will help us find better contours
   # kernel size provided as none
   contours, hierarchy = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

   for contour in contours: #if there are any contours
      ball = sorted(contours, key=cv2.contourArea)[-1]
      # sorts in descending order and takes last value(smallest area contour of ball)
      (x, y, w, h) = cv2.boundingRect(contour)
      cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
      # (x, y), r = cv2.minEnclosingCircle(ball)
      # cv2.circle(frame, (int(x), int(y)), int(r), (0, 0, 255), 5)

   cv2.imshow("feed", frame1)
   frame1 = frame2
   ret, frame2 = cap.read()

   if cv2.waitKey(40) == 27:
      break

cv2.destroyAllWindows()
cap.release()
