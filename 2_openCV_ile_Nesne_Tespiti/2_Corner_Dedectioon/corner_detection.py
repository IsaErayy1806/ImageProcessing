import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktarma
img=cv2.imread("sudoku.JPG",0)
#ondalıklı sayılara döndürme
img=np.float32(img)

print(img.shape)
plt.figure(), plt.imshow(img,cmap="gray"), plt.axis("off")

#Köşeyi tespit etmek için harris corner detection uyguluyoruz

dst=cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
#blocksize=komşuluk boyutu
#ksize=şimdiye kadar kullandığımız kutucuğun boyutu
#k=harris detectöründeki free parametrelerden bir tanesi
plt.figure(), plt.imshow(dst,cmap="gray"), plt.axis("off")

#Kenardaki şeylerin daha belirgin olamsı için genişleme fonksiyonu kullanıyoruz
dst=cv2.dilate(dst, kernel=None)
img[dst>0.2*dst.max()]=1
plt.figure(), plt.imshow(dst,cmap="gray"), plt.axis("off")

#Farklı bir kenar algılama yöntemi
#shi tomasi.detection
img=cv2.imread("sudoku.JPG",0)
img=np.float32(img)
corners=cv2.goodFeaturesToTrack(img, maxCorners=120, qualityLevel=0.01, minDistance=10)
corners=np.int64(corners)#float yapıyı integere çevirme

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y), 3, (125,125,125), cv2.FILLED )
    
plt.figure(), plt.imshow(img), plt.axis("off")

#Note:Toplamda 100 köşe tespiti yap demiştik ancak yetersi zkalıyorsa bu sayıyı arttırarak tüm köşe noktaları tespit edebiliriz.
