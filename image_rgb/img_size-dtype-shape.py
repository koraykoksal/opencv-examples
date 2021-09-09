import cv2
import numpy as np



img = cv2.imread("happy.jpg")

cv2.imshow("Image", img)

print(img[(230,80)])

# img değişkeni içindeki resim üzerinden (230,80) değerlerine karşılık gelen pixel sonucu bulunur.
# ilk parametre yukarıdan aşağıya gelen değer, ikinci parametre soldak sağa gelen değer.
# iki değerin kesişme noktası pixel bilgisini verir.


print("Resmin size bilgisi : "+ str(img.size))  # str tipindeki değer ile oku.size değeri str convert işlemi ile yazdırıldı. Bu işlem str convert yapılmadan da yapılabilir.
print("resmin veri tibi : " + str(img.dtype))
print("Resim özellikleri : "+ str(img.shape))



cv2.waitKey(0)
cv2.destroyAllWindows()
