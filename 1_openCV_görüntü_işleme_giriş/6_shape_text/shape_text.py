import cv2 
import numpy as np

#resim oluştur
img=np.zeros((512,512,3),np.uint8)
#3 refers BGR boyut
print("The shape of the image: ",img.shape)
cv2.imshow("Siyah Resim",img)

#çizgi oluşturma
img2=cv2.line(img, (100,100),(300,300),(0,255,255),3)
#3 refers to the fontsize of the line
cv2.imshow("Line Resim",img2)

img3=cv2.line(img2, (300,100),(100,300),(0,255,255),3)
#3 refers to the fontsize of the line
cv2.imshow("Line Resim",img3)

#Dikdörtgen
#(resim ismi,başlangı.,bitiş,renk)
img4=cv2.rectangle(img3,(100,100),(300,300),(255,0,0),3,cv2.FILLED)
cv2.imshow("Dikdortgen",img4)

#çember
img5=cv2.circle(img4,(200,200),142,(0,0,255),cv2.FILLED())
cv2.imshow("Circle-Rectangle-X",img5)

# metin
# (resim, başlangıç noktası, font, kalınlığı, renk)
cv2.putText(img5, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
#cv2.FONT_HERSHEY_COMPLEX ile yazı tipi belirlenir
cv2.imshow("Metin", img5)