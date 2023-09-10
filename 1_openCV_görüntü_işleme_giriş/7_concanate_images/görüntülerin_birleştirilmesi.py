import cv2 
import numpy as np
#resmi içe aktar

img=cv2.imread("lenna.png")
cv2.imshow("Orijinal",img)

#Birleştirme kısmı

#Horizontal şekilde

hor=np.hstack((img,img))
cv2.imshow("Horizontal",hor)

#Vertical
ver=np.vstack((img,img))
cv2.imshow("Vertical",ver)

#hstack örneği
matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

result_matrix = np.hstack((matrix1, matrix2))
print(result_matrix)

result2_matrix=np.vstack((matrix1,matrix2))
print(result2_matrix)