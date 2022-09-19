#Menghitung panjang kapal
import math

h = int(input('h: '))

a = int(input('a: '))
x =math.radians(math.tan(a))

b = int(input('b: '))
y =math.tan(math.radians(b))

hasil = round(h * x - h * y,1)
c = (hasil ** 2)**0.5
print(c,'m')

