#Menghitung volume dan luas permukaan kerucut
#Rumus volume kerucut = ⅓ 𝜋.r².t
#Rumus luas lingkaran = 𝜋.r²
#Rumus luas permukaan = 𝜋.r.s
#r = jari-jari
#t = tinggi
#S = garis pelukis
#Rumus garis pelukis = √(r² + t²)

import math
r = int(input("Masukkan nilai jari-jari : "))
t = int(input("Masukkan nilai tinggi : "))

S = math.sqrt(r**2 + t**2)

volume = 1/3 * math.pi * r**2 * t
luas = (math.pi * r * S) + math.pi * r**2

print("===> Volume kerucut : " , round(volume,2))
print("===> Luas permukaan kerucut : " , round(luas,2))
