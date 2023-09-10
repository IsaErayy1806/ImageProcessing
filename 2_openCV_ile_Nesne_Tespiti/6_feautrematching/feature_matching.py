#Özellik eşleştirme
import cv2
import matplotlib.pyplot as plt
import os 

os.chdir('C:\\Users\\aslan\\OneDrive\\Masaüstü\\python\\2_openCV_ile_Nesne_Tespiti\\6_feautrematching')
#ana görüntüyü içe aktar
chos=cv2.imread("chocolates.jpg",0)
print(chos.shape)
plt.figure(), plt.imshow(chos,cmap="gray"), plt.axis("off")

#aranacak alan görüntü
cho=cv2.imread("nestle.jpg",0)
print(cho.shape)
plt.figure(), plt.imshow(cho,cmap="gray"), plt.axis("off")

#orb tanımlayıcı
#köşe-kenar gibi nesneye ait özellikler
orb=cv2.ORB_create()

#anahtar nokta tespitleri
kp1, des1=orb.detectAndCompute(cho,None)
kp2, des2=orb.detectAndCompute(chos,None)

#bf matcher
bf=cv2.BFMatcher(cv2.NORM_HAMMING)

#NOKTALARI EŞLEŞTİR
matches=bf.match(des1,des2)

#mesafeye göre sırala
matches=sorted(matches, key=lambda x: x.distance)

#eşleşen resimleri gçrselleştirelim
plt.figure()
img_match=cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, 2 )
plt.imshow(img_match), plt.axis("off")



