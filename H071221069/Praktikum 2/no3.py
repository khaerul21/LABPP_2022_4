import sys
genap = 0
ganjil = 0
positif = 0
negatif = 0

bilangan_1,bilangan_2,bilangan_3,bilangan_4,bilangan_5 = input("masukan 5 bilangan : ").split(" ")

if not bilangan_1.isnumeric():
    if bilangan_1[0] == "-" and len(bilangan_1) > 1:
        negatif += 1
    else:
        sys.exit("inputan tidak valid")

bilangan_1 = int(bilangan_1)

if bilangan_1 > 0:
    positif+= 1

if bilangan_1 % 2 == 0 or bilangan_1 == 0:
    genap+= 1
else:
    ganjil+= 1


if not bilangan_2.isnumeric():
    if bilangan_2[0] == "-" and len(bilangan_2) > 1:
        negatif += 1
    else:
        sys.exit("inputan tidak valid")

bilangan_2 = int(bilangan_2)

if bilangan_2 > 0:
    positif+= 1
if bilangan_2 % 2 == 0 or bilangan_2 == 0:
    genap+= 1
else:
    ganjil+= 1  


if not bilangan_3.isnumeric():
    if bilangan_3[0] == "-" and len(bilangan_3) > 1:
        negatif += 1
    else:
        sys.exit("inputan tidak valid")
  
bilangan_3 = int(bilangan_3)

if bilangan_3 > 0:
    positif+= 1
if bilangan_3 % 2 == 0 or bilangan_3 == 0:
    genap+= 1
else:
    ganjil+= 1 


if not bilangan_4.isnumeric():
    if bilangan_4[0] == "-" and len(bilangan_4) > 1:
        negatif += 1
    else:
        sys.exit("inputan tidak valid")

bilangan_4 = int(bilangan_4)

if bilangan_4 > 0:
    positif+= 1
if bilangan_4 % 2 == 0 or bilangan_4 == 0:
    genap+= 1
else:
    ganjil+= 1


if not bilangan_5.isnumeric():
    if bilangan_5[0] == "-" and len(bilangan_5) > 1:
        negatif += 1
    else:
        sys.exit("inputan tidak valid")

bilangan_5 = int(bilangan_5)

if bilangan_5 > 0:
    positif+= 1
if bilangan_5 % 2 == 0 or bilangan_5 == 0:
    genap+= 1
else:
    ganjil+= 1

 
print(genap, " angka genap")  
print(ganjil, " angka ganjil")
print(positif, " angka positif")
print(negatif, " angka negatif")
