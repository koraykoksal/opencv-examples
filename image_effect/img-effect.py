import cv2
import numpy as np



'''
img değişkeninde yer alan resim üzerinde belirli bir kısma efect uygulama
'''

img = cv2.imread("resim_efect/turuncu_kamera.jpg")

img[:,:,2] = 150     # RGB 2. index (Red değeri) değerine değer atanır.
img[:,:,1] = 190    # RGB 1. index (Green değeri) değerine değer atanır.
img[:,:,0] = 240    # RGB 0. index (Blue değeri) değerine değer atanır.

"""
RGB değerine yeni değer ataması ve efect uygulamak için RGB 0,1,2 index değerlerine yeni RGB no ataması yapılır.
[:,:,0/1/2] son parametre RGB değer parametresidir.
"""


img[100:350,500:780,1] = 34  # 100:150 Y parametresi ve 300:400 X parametresine Green değeri için 34 değeri atandı.
img[100:350,500:780,2] = 130    #aynı bölgenin 0-1-2 index değerlerine farklı renk değeri ataması yapılabilir.

img[120:370,420:620,2] = 44  # 120:170 Y parametresi ve 320:420 X parametresine Red değeri için 44 değeri atandı.
img[70:200,170:500,0] = 60  # 170:200 Y parametresi ve 370:500 X parametresine Red değeri için 60 değeri atandı.

"""
RGB index değeri ile istenilen bölgeye efect uygulaması yapılır.
(100:150) Y parametresi (300:400) X parametresi (1) RGB 1 indexi Green değeri.
"""





cv2.imshow("Image Effect", img) # img değerini görüntülemeyi sağlar.

cv2.waitKey(0)
cv2.destroyAllWindows()
