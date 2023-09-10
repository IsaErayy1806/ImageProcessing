import cv2


cap= cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#Genişlik almak için kullanılır
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#yükeseklik almak için kullanılır

print(width,height)


writer=cv2.VideoWriter("video_kaydi3.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))

while True:
    ret, frame=cap.read()
    cv2.imshow("Video Kaydi",frame)
    
    #saving
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("k"): break 
    
cap.release() #Video yakalama nesnesini serbest bırakır.
writer.release() # Video kaydetme nesnesini serbest bırakır ve dosyayı kapatır.
cv2.destroyAllWindows()  #Açık olan tüm pencereleri kapatır.
