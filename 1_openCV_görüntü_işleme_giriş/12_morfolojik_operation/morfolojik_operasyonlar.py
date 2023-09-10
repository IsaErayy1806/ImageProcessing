import cv2 
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("datai_team.jpg",0)
plt.figure(), plt.imshow(img,cmap="gray"), plt.axis("OFF"), plt.title("Orijinal image")


#erozyon 
kernel=np.ones((5,5), dtype=np.uint8)
result=cv2.erode(img, kernel, iterations=1)
#As we increase the number of iterations the image will be off
plt.figure(), plt.imshow(result,cmap="gray"), plt.axis("off"), plt.title("Erozyon image")

#Genişleme-dilation
result2=cv2.dilate(img, kernel,iterations=1)
plt.figure(), plt.imshow(result2,cmap="gray"), plt.axis("off"), plt.title("Dilation-Genişleme image")

#açılma
#gürültüyü azaltmak için kullanılır

#Önce bir gürültü oluşturuyoruz
whiteNoise=np.random.randint(0, 2, size=img.shape[:2])
whiteNoise=whiteNoise*255#Normalize edilmiş 0 ve 2 arasındaki random sayıları 255 ile çarparak istediğimiz boutu elde ediyoruz

plt.figure(), plt.imshow(whiteNoise,cmap="gray"), plt.axis("off"), plt.title("White NOise")

#şimdi gürültüyü orijinal resmin üüzerine ekleyeceğiz
noise_img=whiteNoise+img
plt.figure(), plt.imshow(noise_img,cmap="gray"), plt.axis("off"), plt.title(" Noise İmage")

#Noise yapısını açılma yöntemiyle ortadan kaldırmak
opening=cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening,cmap="gray"), plt.axis("off"), plt.title(" Acılma İmage")


#black noise
blackNoise=np.random.randint(0, 2, size=img.shape[:2])
blackNoise=blackNoise*-255#Normalize edilmiş 0 ve 2 arasındaki random sayıları 255 ile çarparak istediğimiz boutu elde ediyoruz
plt.figure(), plt.imshow(blackNoise,cmap="gray"), plt.axis("off"), plt.title("Black NOise")

black_noise_img=blackNoise+img
#filtreye sokacağız
black_noise_img[black_noise_img<=-245]=0
plt.figure(), plt.imshow(black_noise_img,cmap="gray"), plt.axis("off"), plt.title("Black NOise image")

#♥kapatma
closing=cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing,cmap="gray"), plt.axis("off"), plt.title("Closing image")


#♦morfolojik gradient methodu
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient,cmap="gray"), plt.axis("off"), plt.title("gradient image")
#Gradyan yöntemi şekillerde kenar tespiti konusunda çok iyidir.
#yazı kenarları tespit edilebiliyor

