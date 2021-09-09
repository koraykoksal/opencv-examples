import cv2
import numpy as np


'''
Resim üzerinden çerçeve, aynalama, tekrarlama veya uzatma işleminin yapılması.
'''


img = cv2.imread("resim_dikdortgen/turuncu_kamera.jpg")


# kullanılan method cv2.(copyMakeBorder)
cerceve = cv2.copyMakeBorder(img,30,30,25,25,cv2.BORDER_CONSTANT,value=(45,67,190))
uzatma = cv2.copyMakeBorder(img,330,0,0,0,cv2.BORDER_REFLECT)
tekrar = cv2.copyMakeBorder(img,330,0,225,0,cv2.BORDER_REPLICATE)
aynalama = cv2.copyMakeBorder(img,430,30,425,125,cv2.BORDER_REFLECT)


cv2.imshow("Image dikdortgen",cerceve)

cv2.waitKey(0)
cv2.destroyAllWindows()


