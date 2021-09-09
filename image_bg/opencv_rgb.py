"""
R(red)G(green)B(blue) renk kodları 0-255 arasında değer alır. 
Bellekte daha az yer kaplamasından ve net ulaşılabilir renk değerinin yakalanmasından dolayı 0-255 arasında değer alır.

"""


import cv2
import numpy as np
# kütüphaneler dahil edildi


oku = cv2.imread("resim_bgr/bird.jpg")
# "resim_okuma" dizini altındaki nesne2.jpeg dosyası okundu.



cv2.imshow("Image RGB Calisması",oku)
# "cv2.imshow" metodu ile pencere title isimlendirmesi yapılır ve oku değişkenindeki resim gösterildi.

print(oku)
# oku değişkeni içindeki resim üzerinde bulunan pixellerin değerlerini (matris bilgilerini) gösteren kod yazıldı.


cv2.waitKey(0)
# pencere açıldıktan sonra pencerenin kalmasını sağlayan kod bloğu yazıldı.

cv2.destroyAllWindows()
# açılan pencerenin fonksiyon butonlarının çalışmasını sağlayan kod bloğu yazıldı.
