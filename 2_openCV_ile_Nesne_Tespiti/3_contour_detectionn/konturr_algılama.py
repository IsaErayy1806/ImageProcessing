
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("contour.jpg",0)
plt.figure(), plt.imshow(img,cmap="gray"), plt.axis("off")

print(img.shape)
#282 451

#First: Görüntüyü yükle ve kenar algılama yap
edges=cv2.Canny(img, threshold1=50, threshold2=240)
plt.figure(), plt.imshow(edges,cmap="gray"), plt.axis("off")


#Second:Kenarlar üzerinde kontur algılama yapma
contours, _=cv2.findContours(edges, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
#mode: Kontur algılama modu. Örneğin cv2.RETR_EXTERNAL yalnızca en dıştaki konturları alırken, cv2.RETR_TREE tüm kontur yapısını alır.
#method: Kontur yaklaşım yöntemi. Örneğin cv2.CHAIN_APPROX_SIMPLE, konturları sıkıştırılmış bir şekilde saklar.

#Third:Konturları bulduktan sonra görüntü üzerine çizme
contour_img=np.zeros_like(img)
cv2.drawContours(contour_img,contours,-1,(255,255,255),2)


contour_img: Konturların çizileceği hedef görüntü. Genellikle bu görüntü, üzerine çizim yapılacak görüntünün boyutlarına uygun bir siyah zemin (sıfır değerler) olarak oluşturulur.
contours: Çizilecek konturların listesi.
-1: Çizilecek konturların indeksi. -1, tüm konturların çizilmesini belirtir.
(255, 255, 255): Konturun çizgi rengi. Bu örnekte beyaz renk kullanılıyor.
1: Çizginin kalınlığı.

plt.figure(), plt.imshow(contour_img,cmap="gray"), plt.axis("off")
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("contour.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# farklı sürüm için 
# image, contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape,dtype=np.uint8)
internal_contour = np.zeros(img.shape, dtype=np.uint8)

for i in range(len(contours)):
    
    # external
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour,contours, i, 255, -1)
    else: # internal
        cv2.drawContours(internal_contour,contours, i, 255, -1)

plt.figure(), plt.imshow(external_contour, cmap = "gray"),plt.axis("off")
plt.figure(), plt.imshow(internal_contour, cmap = "gray"),plt.axis("off")
