from typing import no_type_check
import cv2
import numpy as np



"""
Resmin 2 kat büyütülmesi ve küçütülmesi işlemi.
bütütme ve küçültme işlemi sonrası shape özellikleri görüntüleme
"""


img = cv2.imread("dog.jpg")
img2 = cv2.imread("bird.jpg")


# img değişkeni içindeki köpek resminin 2 kat büyümesini sağlayan fonksiyon
x2_up = cv2.pyrUp(img)

# orijinal resim ile 2 kat büyük resmin shape özelliklerini gösterir
print("img original dog photo height/with: ",img.shape)
print("img x2 up dog photo height/with: ",x2_up.shape)

"""
yükseklik ve genişlik değerlerinde küsüratlı rakamlar yukarı yuvarlanır ve tam sayı olarak gösterilir.
"""

# 2 kat büyütülmüş köpek resmini kare içine alan fonksiyon
cv2.rectangle(x2_up,(1030,950),(100,350),(0,0,183),3)

# orjinal resim ile 2 kat büyütülmüş resmi gösterir.
cv2.imshow("img original dog photo",img)
cv2.imshow("img x2 up dog photo",x2_up)




# img2 değişkeni içindeki kuş resminin 2 kat küçülmesini sağlar
x2_down = cv2.pyrDown(img2)

print("img2 original bird photo height/with: ",img2.shape)
print("img2 x2 down bird photo height/with: ",x2_down.shape)

"""
yükseklik ve genişlik değerlerinde küsüratlı rakamlar yukarı yuvarlanır ve tam sayı olarak gösterilir.
"""

cv2.imshow("img2 original bird photo",img2)
cv2.imshow("img2 x2 down bird photo",x2_down)



cv2.waitKey(0)
cv2.destroyAllWindows()


