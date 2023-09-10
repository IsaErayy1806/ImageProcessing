#Görüntü eşikleme

import cv2 
import matplotlib.pyplot as plt

img=cv2.imread("img1.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Resmin rengini düzeltme işlemi yapılıyor
#Gray-gri scalada işlem görülüyor.


plt.figure()
plt.imshow(img,cmap="gray")
#colormağ(cmap) ile gri tonlamayı sağlıyoruz
plt.axis("off")
plt.show()


#eşikleme

_, thresh_img=cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")
plt.show()

#Adaptive threshold

thresh_img2=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2,cmap="gray")
plt.axis("off")
plt.show()

while True:
    if cv2.waitKey(1) & 0xFF == ord("k"):break

cv2.destroyAllWindows()


#cv2.ADAPTIVE_THRESH_MEAN_C: Uyarlamalı eşikleme türünü belirten parametre. Bu, ortalama yöntemini kullanır.
#11: Blok boyutu. Blok boyutu, her pikselin etrafındaki alanın boyutunu belirtir. Burada 11, 11x11 piksellik bir bloğun kullanılacağını gösterir.
#8: C değeri. Bu, ortalama yöntemiyle hesaplanan eşik değerine eklenen sabit bir değerdir.
