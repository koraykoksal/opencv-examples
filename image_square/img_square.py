import cv2
import numpy as np


img = cv2.imread("resim_kare/mavi_boncuk.png")


cv2.rectangle(img,(260,180),(380,55),(0,0,183),3)

"""
cv2.rectangle metodu içinde img değişkeni için '()' oval parantez kullanılarak x,y kordinat değeri verildi.
1.parametre x,y kordinatı (sol alt köşe)
2.parametre x,y koddinatı (sağ üst köşe)
3.parametre rgb renk değeri (border rengi)
4.parametre border kalınlık değeri 
"""

cv2.imshow("Image Square",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
