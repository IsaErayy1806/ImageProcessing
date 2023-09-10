import cv2
import matplotlib.pyplot as plt
import os
"""
template=cv2.imread("cat_face1.jpg",0)
print(template.shape)

h,w=template.shape
"""

#template matching : şablon eşleme
os.chdir("C:\\Users\\aslan\\OneDrive\\Masaüstü\\python\\2_openCV_ile_Nesne_Tespiti\\5_templatematching")
img=cv2.imread("cat1.jpg",0)
print(img.shape)

template=cv2.imread("cat_face1.jpg",0)
print(template.shape)


#methods that contains strings representing various methods or techniques for template matching using the OpenCV library in Python
#'cv2.TM_COEF': This might be a custom method or a typo, as it does not correspond to any standard OpenCV template matching method that I'm aware of. It could be a placeholder for a custom method.
#'cv2.TM_CCOEFF_NORMED': This method performs template matching using normalized cross-correlation. It's one of the standard methods available in OpenCV.
"""
'cv2.TM_CCORR': This method performs template matching using cross-correlation without normalization. It's another standard method in OpenCV.

'cv2.TM_CCORR_NORMED': This method performs template matching using normalized cross-correlation. It's similar to 'cv2.TM_CCOEFF_NORMED' but uses a different correlation formula.

'cv2.TM_SQDIFF': This method performs template matching using the sum of squared differences. It's a standard method in OpenCV.

'CV2.TM_SQDIFF_NORMED': There is a typo here; it should be 'cv2.TM_SQDIFF_NORMED' (note the lowercase "cv2"). This method performs template matching using normalized sum of squared differences.
"""
h, w=template.shape
methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR',
         'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'CV2.TM_SQDIFF_NORMED']
for meth in methods:
    method=eval(meth)

    res=cv2.matchTemplate(img, template, method)
    print(res.shape)
    min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    bottom_right=(top_left[0]+w, top_left[1]+h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap="gray")
    plt.title("Eşleşen sonuçç"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap="gray")
    plt.title("Tespit edilen sonuç"), plt.axis("off")
    plt.suptitle(meth)

    plt.show()    
    
