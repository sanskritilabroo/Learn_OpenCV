import cv2

img=cv2.imread("lena.jpg")
# lr1=cv2.pyrDown(img)#gaussian
# hr1=cv2.pyrUp(lr1)
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow("upper level gaussian pyramid",layer)
lp=[layer]

for i in range(5,0,-1):
    gaussian_extend=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_extend)
    cv2.imshow(str(i),laplacian)

cv2.imshow("original image",img)
# cv2.imshow("pyrdown 1",lr1)
# cv2.imshow("pyrup 1",hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()