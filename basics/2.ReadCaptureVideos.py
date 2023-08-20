import cv2
cap=cv2.VideoCapture(0) #captures video through the webcam
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('../output.avi', fourcc, 20.0, (640, 480))
print(cap.isOpened())

while (cap.isOpened()): #can also write while True:
    ret, frame=cap.read()

    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts color video to gray but it is still saved as color
        cv2.imshow("frame",gray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()