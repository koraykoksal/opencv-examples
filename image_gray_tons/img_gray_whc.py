import cv2
import numpy as np

"""
Resme gri tonlama yapılması ve genişlik,yükselik,kanal sayısını görme
"""


img = cv2.imread("resim_gri_tonlama/dog.jpg")


# farklı renk tonlamaları

image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # gri tonlama
image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)    # pembe ışıklı tonlama
image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)   # yeşil ışıklı tonlama
image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)    # mavi ışıklı tonlama
image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   # soft renkte tonlama
image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
image_gray = cv2.cvtColor(img,cv2.COLOR_BGR2XYZ)


"""
img değişkeni içindeki resme gri veya farklı tonlama uygulaması

"""



# shape özelliği ile resmin yükselik, genişlik ve BGR kanal sayısını görme

yukseklik,genislik,kanalsayisi = img.shape
yukseklik,genislik = image_gray.shape

"""
renkli resimlerde kanal sayısı görüntülenebilir
gri tonlamaya sahip resimlerde kanal sayısı görüntülenemez. çünkü bir adet bgr değeri kullanılmıştr.
bundan dolayı image_gray.shape işleminde sadece yukseklik ve genislik belirtilmiştir.
"""



print(yukseklik,genislik,kanalsayisi)


cv2.imshow("Gray Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()




