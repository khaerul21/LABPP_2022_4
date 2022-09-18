import math

h = float(input("Ketinggian Menara (dalam satuan meter): "))
a = float(input("Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal: "))
b = float(input("Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal: "))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))

panjang = math.sqrt((belakang - depan)**2)
print("Panjang Kapalnya adalah", round(panjang, 1), "m")