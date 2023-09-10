import cv2
import matplotlib.pyplot as plt
import os


#template matching : şablon eşleme

img=cv2.imread("cat1.jpg",0)
print(type(img))
"""
template=cv2.imread("cat_face1.jpg",0)
print(template.shape)

h,w=template.shape
"""