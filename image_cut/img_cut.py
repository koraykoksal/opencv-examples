import cv2
import numpy as np


"""
Resim üzeriden belirli bir alanı kesit alma işlemi
"""

img = cv2.imread("turuncu_kamera.jpg")




#img[234:600, 123:500, 2] = 123  # x,y kordinatında 234:600 ile 123:500 arasında RGB 2 değerine 123 değeri uygulanır.

cut = img[120:340, 160:440] 
#cut[:,:,0] = 45 # blue değerine 45 değeri atanır.

cut2 = img[240:550, 180:440]
cut2[:,:,1] = 187   # green değerine 187 değeri atannır.


"""
img değerinde belirtilen parametre değerleri farklı bir değişkenin içine atılarak o bölgenin çıktısı alınır.
cut değişkenin 0 nolu Blue RGB değerine yeni bir değer ataması yapılır.
cut2 değişkenin 1 nolu Green RGB değerine yeni bir değer ataması yapılır.
"""

img[0:220, 0:280] = cut

"""
img değeşkeninde belirtilen 0:220, 0:280 pararetrelerinin içine cut değişkeni atarnır.
Burada yazılan parametre değeri ile cut değişkeninde belirtilen parametre değerleri aynı olmalıdır.
Cut değişkeninde belirtilen 120:340 arasındaki 220 değeri ve 160:440 arasında ki 280 değeri img parametresinde tanımlanır. 
Aksi halde cut değişkenin boyutu büyük veya küçük gelecektirme ve resim üzerine yazma yapamayacaktır.
"""

img[230:450, 123:349] = (5,156,230) # img parametre değerlerine RGB renk değerleri atanmıştır.



cv2.imshow("Image Cut",img)
#cv2.imshow("Kesilen resim", cut)
#cv2.imshow("Kesin resim 2", cut2)

"""
Oluşturulan yeni değişkenler cv2.imshow metodu ile tekrar gösterilir.
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
