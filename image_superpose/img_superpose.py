import cv2
import numpy as np

"""
Resimleri üst üste yazdırıp yeni bir resim ortaya çıkarma
Üst üste yazdırılacak resimlerin boyutları aynı olmalıdır !
"""


img = cv2.imread("old_woman.jpg")
img2 = cv2.imread("young_woman.jpg")

#print(img.size)

# iki resmi üst üst yazdırma işlemi
superpose = cv2.add(img,img2)

# resimleri %lik değer ile üst üste yazdırıp belirginletirme işlemi
superpose = cv2.addWeighted(img,0.2,img2,0.6,0)

'''
'cv2.addWeighted' metodu ile 1. parametre ilk resim, 2. parametre ilk resme uygulanacak belirginleştirme tonlaması, 3.parametre ikinci resim, 4.parametre 2.resme uygulanacak
beliginleştirme tonlaması, 5.parametre resmin tamamına uygulanacak gamma işlemi
'''

cv2.imshow("Yeni Resim", superpose)


cv2.waitKey(0)
cv2.destroyAllWindows()
