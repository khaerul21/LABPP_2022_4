#Konversi detik ke jam:menit:detik

print ("====== Konversi detik ke jam:menit:detik ======")
detik_awal = int(input("masukkan jumlah detik yang diinginkan : "))

jam = detik_awal // 3600
sisa_detik = detik_awal % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print ("%03d:%02d:%02d" % (jam, menit, detik))