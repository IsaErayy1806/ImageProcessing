import cv2
import numpy as np

img=cv2.imread("kart.png")
cv2.imshow("Orijinal",img)
print("Shape: ",img.shape)

width=400
height=500

#-köşe piksel belirleme paint ile.
pts1=np.float32([[205,1],[2,472],[539,145],[339,617]])
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)


#nihai dönüştürülmüş resim
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Nihai resim",imgOutput)

cv2.waitkey(0)
cv2.destroyAllWindows()