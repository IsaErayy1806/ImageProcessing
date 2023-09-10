import cv2 
import time 

video_name="MOT17-04-DPM.mp4"
cap=cv2.VideoCapture(video_name)

print("Genişlik : ",cap.get(3))#3 used for genişlik
print("Yükseklik : ",cap.get(4))#4 used for yükseklik

if cap.isOpened()==False:
    print("There is an error.Try again.")
    
while True:
    ret,frame=cap.read()
    if ret==True:
        time.sleep(0.01)# uyarı: kullanmazsak çok hızlı akar
        cv2.imshow("Video",frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("k"):
        break 
cap.release() #: Video yakalama nesnesini serbest bırakır, yani video dosyasının kullanımını sonlandırır.
cap.destroyAllWindows()


