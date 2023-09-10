import cv2
import matplotlib.pyplot as plt
import numpy as np

#Resmi içe aktarma
img=cv2.imread("red_blue.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure(), plt.imshow(img)
#red için (255,0,0)
#blue için(0,0,255)

print(img.shape)

img_hist=cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
print(img_hist.shape)

plt.figure(), plt.plot(img_hist)

color=("b","g","r")
for i,c in enumerate(color):
    #Tuplein içindeki indexi i ye , değeri ise c ye eşitliyor
    hist=cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist,color=c)
    #piksellerde yeşilden 0 piksel değerinde 136000 piksel var
    #kırmızı ve maviden ise 0 lardan 700000 255 değerinde ise 700000 piskel var !!!
    
img2=cv2.imread("goldenGate.jpg")
img2_vis=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img2_vis)
print(img2.shape)
#♦Total piksel sayısı 23970816
mask=np.zeros(img2.shape[:2], dtype=np.uint8)
plt.figure(), plt.imshow(mask,cmap="gray")

mask[1500:2000, 1000:2000]=255#Beyaz oluyor 255 yazınca , 0 yazarsak ise siyah oluyor
plt.figure(), plt.imshow(mask,cmap="gray")

#Resmi maskeleştirme işlemi
masked_img_vis=cv2.bitwise_and(img2_vis,img2_vis, mask=mask)
plt.figure(), plt.imshow(masked_img_vis,cmap="gray")

masked_img=cv2.bitwise_and(img2,img2, mask=mask)
masked_img_hist=cv2.calcHist([img2], channels=[1], mask=mask, histSize=[256], ranges=[0,256])
#channels[0] kırmızıya eşlik ediyor RGb den dolayı
plt.figure(), plt.plot(masked_img_hist)

color2=("b","g","r")
for i,c in enumerate(color2):
    histed=cv2.calcHist([img2_vis], channels=[i], mask=mask, histSize=[256], ranges=[0,256])
    plt.plot(histed,color=c)
    
#histogram eşitleme
#karşıtlık arttırma

img3=cv2.imread("hist_equ.jpg",0)
plt.figure(), plt.imshow(img3,cmap="gray")
img3_hist=cv2.calcHist([img3], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure(), plt.plot(img3_hist)

eq_hist=cv2.equalizeHist(img3)
plt.figure(), plt.imshow(eq_hist,cmap="gray")

eq_img3_hist=cv2.calcHist([eq_hist], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure(), plt.plot(eq_img3_hist)