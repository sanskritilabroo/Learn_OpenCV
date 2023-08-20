import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000) #programmer sets resolution as 3000
cap.set(4, 3000)

#if too high, camera automatically resolves to 720 x 1280, and if too low then 480 x 640
print(cap.get(3)) #3 refers to width property
print(cap.get(4)) #4 refers to height property
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()