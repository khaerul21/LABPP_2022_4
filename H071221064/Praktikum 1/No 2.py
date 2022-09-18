#format detik ke dalam format jam:menit:detik
n = int(input('detik : ' ))

jam = n // 3600
sisa = n % 3600
menit = sisa // 60
detik = sisa % 60

print("%02d : %02d : %02d"%(jam,menit,detik))