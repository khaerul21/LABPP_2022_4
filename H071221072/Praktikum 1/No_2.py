'''Mifthahul Hoiri Bachrudin Basir
    H071221072'''
#Konversi detik ke jam
data = int(input("Masukkan detik: "))
jam = (data//3600)
sisa = (data % 3600)
menit = (sisa //60)
detik = (sisa % 60)

print("%02d : %02d : %02d" % (jam,menit,detik))
