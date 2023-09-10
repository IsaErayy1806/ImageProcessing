# %% spyter tanıtımı
print("Hello World")

# %% değişkenler 

tamsayı_degisken=10
ondalıkli_sayi=12.3
print(tamsayı_degisken)
print(ondalıkli_sayi)

#4 işlem özellikleri

pi_sayısı=3.14
katsayı=2
toplam=pi_sayısı+1
fark=pi_sayısı-1
carpma=pi_sayısı*katsayı
bolme=pi_sayısı/katsayı

print("Toplam :",toplam)
print("Toplam: {} ve fark: {}".format(toplam,fark))
print("Carpma : %.1f , Bölme %.4f"%(carpma,bolme))

carpma_int=int(carpma)
print(carpma_int)

tamsayı_float=float(tamsayı_degisken)
print(tamsayı_float)

string="Merhaba dünya"
print(string)

str1="veri"+"\\"+"img"+".png"
print(str1)


# %% pyhton listeler

# Birleşik veri türüdür ve çok yönlüdür
# [1,"a",1.0]
# farklı veri tiplerini içerisinde barındırabilir

liste = [1,2,3,4,5,6]
print(type(liste))

hafta=["süt","muz","elma","karpuz"]
print(hafta[0])#gives the first index at the list
print(hafta[3])#gives the last index
print(hafta[len(hafta)-1])
print(hafta[-2])
#0 1 2 3
#-4 -3 -2 -1 diye gidiyor
print(hafta[1:3]) 
liste.append(7)#listeye eleman ekleme
print(liste)

liste.remove(3)#Listeden elemna çıkarma
print(liste)

liste.reverse()#Listeyi ters çevirme
print(liste)

sayı_listesi=[1,9,7,12,5,8,13]
sayı_listesi.sort() #Sayıları büyükten küçüğe doğru sıralama
print(sayı_listesi)


# %% Tuple type in python

#Değiştirilemez ve sıralı bir veri tipidir.
#Listede [] kulllanırken tuple için () kullanıyoruz


veritipi=(1,2,3,4,5,6)
print(type(veritipi))

print(veritipi[0])
print(veritipi[5])

print(veritipi[2:])

#With count() function we calculate the number of elements in the array list

print(veritipi.count(3))
tuple_xyz=(1,2,3)
x,y,z=tuple_xyz
print(x,y,z)

# %%  Deque type in python

#Lİstenin boyutu belirlenebilir

from collections import deque
dq=deque(maxlen=3)

dq.append(1) # 1 ekle sonuna [1]
print(dq)

dq.append(2)
print(dq)

dq.append(3)
print(dq)

dq.append(4)
print(dq)

#After the fourth elements it has a circular type around itself
dq2=deque(maxlen=3)
dq2.append(1)
dq2.append(2)
dq2.appendleft(3)
print(dq2)

dq2.clear() #It clears the inside of the list.
print(dq2)

dq2.append(1)
dq3=dq2.copy()# Copies an elements of a list to an another list
print(dq3)

oddnumbers=(1,3,5,7,9)
odddeque=deque(oddnumbers)
print("Odd numbers :",odddeque)

moreoddnumbers=(11,13,15,17)
odddeque.extend(moreoddnumbers)#Exten the dimension of the list
print("Odd numbers with extending : ",odddeque)


# %%DICTIONARY İN PYTHON

#Bir çeişt karma tablo türüdür
#Anahtar ve değer çiftlerindeno luşur
dictionary={"İstanbul":34,
            "İzmir":35,
            "Konya":42
            }
print(dictionary)
print(dictionary["İstanbul"])

#Anahtarlar
print(dictionary.keys())

#değerler
print(dictionary.values())

# %% IF-ELSE IN PYTHON

#Büyük-küçük sayı karşılaştırması

sayi1=12.0
sayi2=20.0

if sayi1<sayi2:
    print("sayi2 büyüktür sayi1 den")
else:
    print("Sayi1 sayi 2 den büyüktür")
    

liste=[1,2,3,4,5]
değer=32

if değer in liste:
    print("{} değeri listenin içersindedir.".format(değer))
else:
    print("{} değeri listenin içerisinde değildir.".format(değer))
    
dictionary={"Türkiye":"Ankara", "İngiltere":"Londra","Ispanya":"Madrid"}
keys=dictionary.keys()
deger="Türkiye"

if deger in keys:
    print("Evet")
else:
    print("Hayır")

# %%For and While döngüleri in python

#for 

for i in range(1,11): 
    print(i)

liste=[1,2,3,4,5,6,10]
toplam=0
for i in liste:
    toplam=toplam+i
print(toplam)

topl=0
i=0
while i<len(liste):
    topl=topl+liste[i]
    i=i+1
print(topl)

# %%Fonksiyonlar
pi=3.14
def dairenin_alanı(yarıcap):
    alan=pi*(yarıcap**2)
    return alan
print(dairenin_alanı(5))

def daire_cevresi(yarıcap):
    daire_cevre=2*pi*yarıcap
    return daire_cevre
print(daire_cevresi(5))


#boş fonksiyonlar

def bos():
    pass

# %%Yield yapısı
    
#İterasyon
#Generator:Değerleri bellekte saklamazlar,yeri gelince anında üretirler.
#Yield

generator=(x for x in range(1,4))
for i in generator:
    print(i)

#Fonksiyon eğer return olarak generator döndürecekse bunu return  yerine "yield" anahtar sözcüğü ile yapar.
def creategenerator():
    liste=range(1,4)
    for i in liste:
        yield i
generator=creategenerator()
print(generator)

for i in generator:
    print(i)


# %% Numpy kütüphanesi
    
#Matixler için hesaplama kolylaığı sağlar

import numpy as np

dizi=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

#shape() fonksiyonu arrayin boyutunu verir
print(dizi.shape)

dizi2=dizi.reshape(3,5)
print("Şekil: ",dizi2.shape)
print("Boyut: ",dizi2.ndim)
print("Veri tipi : ",dizi2.dtype.name)
print("Boy: ",dizi2.size)
print(dizi2)

#2 boutlu array
dizi2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2d)

#Sıfırlardan oluşan bir array
sıfır_dizi=np.zeros((3,4))#Çift parantez olmak zorunda data type anlaşılmıyor.
print(sıfır_diz)

#Birlerden oluşan bir array
bir_dizi=np.ones((3,3))
print(bir_dizi)

liste=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
clist=[]
for i in liste:
    clist.append(i)
print(clist)

#bos array
bos_dizi=np.empty((3,4))
print(bos_dizi)

#arange(x,y,basamak)

dizi_aralık=np.arange(10,50,5)
print(dizi_aralık)

#linspace(x,y,basamak)
dizi_bosluk=np.linspace(10,20,5)
print(dizi_bosluk)

#matematiksel işlemler 

a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

#dizi elemanı toplama
print(np.sum(a))

#max değer
print(np.max(b))

#nmin değer
print(min(a))

#ortalama değer
print(np.mean(a))

#rastgele sayı üretme random generator

rastgele_dizi=np.random.random((3,3))
print(rastgele_dizi)

#index bakma
dizi=np.array([1,2,3,4,5,6,7])
print(dizi[::-1])

array2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2d[1,2])#İt will give 8 

#1.ci sütyun ve tüm satırlar
print(array2d[:,1])

#1.ci satır ve index olarak sütun 1 den 3 e kadar olanla alınsın yani 7,8,9
print(array2d[1,1:4])

#1.ci satır tüm sütunlar
print(array2d[-1,:])

#vektör haline getirm
vektor=array2d.ravel()
print(vektor)

# %%PANDAS KÜTÜPHANESİ

#PANDAS VERİ İŞLEME VE ANALİZİ İÇİN PYTYON RMEMLLİ YAZILMIŞ BİR KÜTÜPHANEDİR
#Hızlı ve güçlü bir veri analizi yapabiliriz.
import pandas as pd

#sözlük oluştur
dictionary={"İsim":["Ali","veli","kenan","Murat","ayse","hilal"],
            "Yas": [15,16,17,35,38,66],
            "Maas": [100,150,240,350,110,220]}

veri=pd.DataFrame(dictionary)
#pandas.DataFrame() fonksiyonu dictionary kısmını veri yapısına dönüştürmek için kullanılır
print(veri.head())
print(veri.columns)

#Veri bilgisi
print(veri.info())

#İstatistiksel bilgiler
print(veri.describe())

#tas sutunu
print(veri["Yas"])

#sütun eklemek
veri["Sehir"]=["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
print(veri)

#yas sütunu
print(veri.loc[ :,"Yas"])

#lk üç yas sütunu
print(veri.loc[:2,"Yas"])#15,16,17 alır sadece

#Not:Listelerden ve numpy yapısından farkklı olarak loc[] yapısında yazılan son indexe kadar alır.

#Yas ve sehir arası alsın
print(veri.loc[:2,"Yas":"Sehir"])

#İsim ve yas sadece
print(veri.loc[:3,"İsim":"Yas"])

#Satırları tersten yazdır
print(veri.loc[::-1,:])

#yas sütunu wih iloc() means index location
print(veri.iloc[:,1])

#İl üç satır ve yaş ve isim
print(veri.iloc[:3,[0,1]])


#Filtreleme
dictionary={"İsim":["Ali","veli","kenan","Murat","ayse","hilal"],
            "Yas": [15,16,17,35,38,66],
            "Sehir": ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"] }
veri2=pd.DataFrame(dictionary)


#İlk olarak yaşa göre bir filtre oluşturalım yas>22
filtre1=veri.Yas>22
filtrelenmis_veri=veri2[filtre1]
print(filtrelenmis_veri)

#ortalama yas
ortalama_yas=veri.Yas.mean()
veri["Yas Grubu"]=["kucuk" if ortalama_yas> i else "buyuk" for i in veri.Yas]
print(veri)

#Birleştirme methodu
sozluk1={"isim":["ali","veli","kenan"],
         "yas":[15,16,17],
         "sehir":["Izmir","Ankara","Konya"]}
veri1=pd.DataFrame(sozluk1)

sozluk2={"isim":["murat","ayse","hilal"],
         "yas":[33,45,66],
         "sehir":["Ankara","Ankara","Antalya"]}
veri2=pd.DataFrame(sozluk2)

veri_dikey=pd.concat([veri1,veri2],axis=0)#axis=0 ile dikeyde birleştiririz
veri_yatay=pd.concat([veri1,veri2],axis=1)#axis=1 ile yatayda birleştirme gerçekleştirilir

# %%Matplotlib kütüphanesi

#Verilerimizi ve görüntülerimizi görselleştiricez

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y=np.array([4,3,2,1])

#Önemli part 
plt.figure()
plt.plot(x,y,color="red",alpha=0.7,  label= "line")
plt.scatter(x,y,color="blue",alpha=0.4, label= "scatter")
plt.title("Maplotlib")#Başlık atma
plt.xlabel("x")#X ekseni ayarlama
plt.ylabel("y")#Y ekseni auarlama
plt.grid(True)#Çizgi çekme
plt.xticks([0,1,2,3,4,5])#X eksenin aralığını belirleme gibi bir şey
plt.legend()
plt.show()

#diğer part
#görüntüleri yan yana çizdirme -subplot yöntemi

fig,axes=plt.subplots(2,1,figsize=(9,7))#2 tane satır 1 tane sütun ve 9 a 7 lik figürlerden oluştuğunu belirtmekte
fig.subplots_adjust(hspace=0.5)#İki resim arasında boşluk koyma

x=[1,2,3,4,5,6,7,8,9,10]
y=[10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub_1")
axes[0].set_xlabel("sub-1 x")
axes[0].set_ylabel("sub-1 y")

axes[1].scatter(y,x)
axes[1].set_title("sub_2")
axes[1].set_xlabel("sub-2 x")
axes[1].set_ylabel("sub-2 y")

#Random resim oluşturma

plt.figure()
img=np.random.random((50,50))
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()


#%% OS KÜTÜPHANESİ

#rESİMLERİ İÇERİYE YÜKLERKEN VEYA KAYDETMEK AMACIYLA KULLANDIĞIMIZ KÜTÜPHANE
import os
print(os.name)

currentDir=os.getcwd()
print(currentDir)

#new folder
folder_name="New folder"
os.mkdir(folder_name)#mkdir() make directory demek

new_folder_name="new_folder_2"
os.rename(folder_name,new_folder_name)


os.chdir(currentDir+"\\"+new_folder_name)#chdir() change directory
print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())

files=os.listdir()
for f in files:
    if f.endswith(".py"):
        print(f)
