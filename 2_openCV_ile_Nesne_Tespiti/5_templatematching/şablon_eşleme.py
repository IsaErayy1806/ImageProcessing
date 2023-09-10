"""
Şablon eşleştirme, bir şablon görüntünün konumunu daha büyük bir görüntüde aramak ve bulmak için bie yöntemdir.
Şablon görüntüsünü giriş görüntüsün üzerine kaydırır ve şablon görüntüsünün altındaki giriş görüntüsünün şablonu ve yamayı karşılaştırır
Çablon kaynak resmin neresindeyse o kısım kararıyor veya aydınlanıyor
"""

import cv2
import matplotlib.pyplot as plt
import os
#template matching : şablon eşleme

img=cv2.imread("C:\\Users\\aslan\\OneDrive\\Masaüstü\\python\\2_openCV_ile_Nesne_Tespiti\\5_templatematching\\cat.jpg",0)
print(img.shape)

template=cv2.imread("C:\\Users\\aslan\\OneDrive\\Masaüstü\\python\\2_openCV_ile_Nesne_Tespiti\\5_templatematching\\cat_face.jpg",0)
print(template.shape)

h,w=template.shape
