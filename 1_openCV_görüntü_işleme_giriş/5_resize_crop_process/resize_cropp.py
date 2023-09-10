import cv2

#
img=cv2.imread("lenna.png")
print("Resim boyutu : ",img.shape)
cv2.imshow("Resim",img)

#
imgResized=cv2.resize(img, (800,800))
print("Size yapısı değismis resim boyutu :", imgResized.shape)
cv2.imshow("Resized Image",imgResized)

#Note:Resim isimlerinde ingilizce karakterlere dikkat et

# 
imgCropped = img[:200,:300] # width height -> height width 
cv2.imshow("Kirpik Resim",imgCropped)
