import cv2
import numpy as np


"""
open cv ile yeni bir shape oluşturma içine çizgi, çember ve metin kutusu yazdırma işlemi
"""

# shape oluşturma
new_variant = np.zeros((300,300,3),dtype="uint8")

# çizgi oluşturma
cv2.line(new_variant,(0,50),(250,100),(100,50,148),3)

"""
1.parametre kaynak (işlemin hangi değişkene uygulanacağı)
2.parametre çizginin başlangıç noktası
3.parametre çizginin bitiş noktası
4.parametre renk
5.paratmetre çizgi kalınlığı
"""

# daire oluşturma
cv2.circle(new_variant,(150,100),50,(0,255,0),2)

"""
1.parametre kaynak (işlemin hangi değişkene uygulanacağı)
2.parametre dairenin başlangıç noktası
3.parametre dairenin yarı çapı
4.parametre renk
5.paratmetre çizgi kalınlığı
"""

# metin kutusu oluşturma
cv2.putText(new_variant,"KORAY KOKSAL",(30,230),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

"""
1.parametre kaynak (işlemin hangi değişkene uygulanacağı)
2.parametre ekranda yazacak text bilgisi
3.parametre text yazısının başlangı noktası
4.parametre yazı fontu
5.parametre yazı boyutu
6.parametre yazı rengi
7.parametre yazı kalınlığı
"""



cv2.imshow("my line",new_variant)


cv2.waitKey(0)
cv2.destroyAllWindows()








