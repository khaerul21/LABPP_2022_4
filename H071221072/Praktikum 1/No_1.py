'''Mifthahul Hoiri Bachrudin Basir
    H071221072'''
#Menghitung panjang kapal
import math

h = int(input('h: '))

a = int(input('a: '))
x = math.tan(math.radians(a))

b = int(input('b: '))
y = math.tan(math.radians(b))

hasil = round(h * x - h * y,1)
z = (hasil ** 2) ** 0.5
print(z,'m')

