import cv2
import numpy as np

"""
resimdeki pixeller üst üste bindiği zaman ağırlıklarının toplanma işlemi
"""

#okuma işlemi
img = cv2.imread("resim_agirlikli_toplama/bird.jpg")
img2 = cv2.imread("resim_agirlikli_toplama/kahve.jpg")
img3 = cv2.imread("resim_agirlikli_toplama/turuncu_kamera.jpg")
img4 = cv2.imread("resim_agirlikli_toplama/turuncu_kamera.jpg")
gt = cv2.imread("resim_agirlikli_toplama/bird.jpg",0)

# img ve img2 y-x değerlerinin bgr değerlerinin çıktısı alınır.

print("img bgr index değeri: ",img[250,100])    # bu değerlere karşılık gelen bgr index değeri listelenir.
print("img2 bgr index değeri: ",img2[200,150])  # bu değerlere karşılık gelen bgr index değeri listelenir.
print("img 3 değeri: ",img3[123,56])
print("img 4 değeri: ",img4[230,6])

# y-x kodinatından gelen bgr index değerinin toplanması
print("img+img2 coordinate total result : ",img[250,100] + img2[200,150] + img3[123,56] + img4[230,6])

'''
img, img2, img3, img4 de belirtilen y-x değerlerine karşılık gelen bgr index değerleri toplanır.
bgr değeri 0-255 arasındadır.
img Blue-Green-Red değeri diğer img2, img3, img4 Blue-Green-Red değeri ile toplanır.
toplama sonucu oluşan değer>255 ise (değer-255)-1 yapılır ve çıkan sonuç yazılır.
-1 yapılmasının sebebi değer 0 dan başladığı için.

değer<255 olana kadar çıkarma işlemi oluşur. yeni değer 255in altında ise yeni bgr değeri olarak atanmış olur.

Önemli : gt değişkeni içindeki resime gri tonlama yapılmıştır. gt değişkeni içindeki yazım şekli ile hesaplama yapılmak istenir ise doğru sonuç çıkmayacaktır.
Bunun nedeni gri tonlama içinde bgr yani blue,green ve red değeri olmadığı için bgr index değerini vermeyecektir.
'''




#cv2.imshow("image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
