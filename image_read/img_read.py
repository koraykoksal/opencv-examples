'''

cv2 open cv kütüphanesidir.
numpy python da az bellek alanı kaplayan liste liste kütüphanesidir.

'''

import cv2, numpy as np
# kütüphaneler dahil edildi.

oku = cv2.imread("resim_okuma/nesne2.jpeg",0) 
# cv2.imread() metodu ile oku yapılacak dosya belirtilir. ikinci parametre "0" ise resim renk tonlarını siyah/beyaz yapar.

cv2.imshow("Open Cv Test Task",oku)
# imshow metodu ile oku değişkeninde belirtilen objenin görüntülenmesi sağlanır. ilk parametre açılan pencerenin title alanını, ikinci parametre gösterilecek değeri belirler.


cv2.imwrite("resim_okuma/nesne2_gray.png", oku)
# oku değişkenindeki siyah/beyaz tonlamaya çevrilen 'nesne.jpeg' dosyası "cv2.imwrite" metodu ile 'nesne_gray.jpeg veya .png' olarak dizine kayıt edilir.

cv2.waitKey(0)
# kod tamamlandıktan sonra yazılması gereken bir kod bloğudur. Pencere açıldıldıktan sonra herhangi bir tuşa basılmasını bekler. "0" değeri yerine saniye cinsinden rakam değeri belirtilebilir.

cv2.destroyAllWindows()
# pencere üzerinde exit tuşlandığında open cv ye bağlı tüm pencereler kapanır.








