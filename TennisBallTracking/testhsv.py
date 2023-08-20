import numpy as np
import cv2

def nothing(x):
    print(x)

cap = cv2.VideoCapture('tennis.mp4')

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    L_H = cv2.getTrackbarPos("LH","Tracking")
    L_S = cv2.getTrackbarPos("LS","Tracking")
    L_V = cv2.getTrackbarPos("LV","Tracking")

    U_H = cv2.getTrackbarPos("UH", "Tracking")
    U_S = cv2.getTrackbarPos("US", "Tracking")
    U_V = cv2.getTrackbarPos("UV", "Tracking")

    L_B = np.array([L_H, L_S, L_V])
    U_B = np.array([U_H, U_S, U_V])

    mask = cv2.inRange(hsv,L_B,U_B)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Tracking", res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
