import cv2

#1 loads a color image
#0 loads a grayscale image
#-1 loads an image as is(alpha channel)
img = cv2.imread('lena.jpg', -1) #reads the contents of the image pixel by pixel

cv2.imshow('sara', img) #shows/displays image

k = cv2.waitKey(0) & 0xFF

if k == 27: #if esc key is pressed, the image disappears
  cv2.destroyAllWindows()

elif k == ord('s'): #if 's' key is pressed, image disappears but a copy is also created
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()