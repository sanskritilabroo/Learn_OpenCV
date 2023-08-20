import cv2
import mediapipe as mp
from math import hypot
import numpy as np
#import serial

#arduino = serial.Serial(port='COM5', baudrate=19200, timeout=.1)

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2)

Draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    Process = hands.process(frameRGB)

    landmarkList = []

    if Process.multi_hand_landmarks:
        for i in Process.multi_hand_landmarks:
            for _id, landmarks in enumerate(i.landmark):
                height, width, color_channels = frame.shape
                x, y = int(landmarks.x * width), int(landmarks.y * height)
                landmarkList.append([_id, x, y])

    if landmarkList != []:
        x_1, y_1 = landmarkList[4][1], landmarkList[4][2]
        x_2, y_2 = landmarkList[8][1], landmarkList[8][2]
        cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED)
        cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)
        cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)
        L = hypot(x_2 - x_1, y_2 - y_1)

        # 1-D linear interpolant to a function with given discrete data points
        # (Hand range 15 - 220, Distance range 0 - 255), evaluated at length.
        level = np.interp(L, [15, 220], [0, 255])

        cv2.putText(frame, str(int(level)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        #arduino.write(bytes(level))

    cv2.imshow('Image', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        #arduino.close()
        break
