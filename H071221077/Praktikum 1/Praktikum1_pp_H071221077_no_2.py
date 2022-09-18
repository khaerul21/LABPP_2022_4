#konversi detik ke jam:menit:detik

nilai = int(input("Detik : "))

jam = int(nilai / (3600))
sisa_detik = int(nilai % 3600)

menit = int(sisa_detik / 60)
detik = int(nilai % 60)

print("%02d:%02d:%02d" % (jam, menit, detik))