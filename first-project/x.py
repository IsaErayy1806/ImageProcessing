import cv2
import os

os.chdir('first-project')

# içe aktarma
img = cv2.imread("messi5.jpg", 0)

# görselleştir
cv2.imshow("ilk Resim", img)

k = cv2.waitKey(0) &0xFF

if k == 27: # esc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()
    