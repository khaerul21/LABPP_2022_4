#Panjang kapal

#h = ketinggian menara
#b = sudut pengamat terhadap ujung depan kapal
#a = sudut pengamat terhadap ujung belakang kapal

import math
h = int(input("Masukkan ketinggian menara : "))
a = int(input("Masukkan sudut evaluasi pengamat terhadap ujung belakang kapal : "))
b = int(input("Masukkan sudut evaluasi pengamat terhadap ujung depan kapal : "))

#sudut ujung depan kapal (tan b) = depan/samping = h/b
#sudut ujung belakang kapal (tan a) = h/b

depan_kapal = h * (math.tan(math.radians(b)))
belakang_kapal = h * (math.tan(math.radians(a)))
panjang = math.sqrt(math.pow(belakang_kapal - depan_kapal,2))

print ("Panjang kapal adalah" , round(panjang,1) , "m")