import math

#menghitung volume bola 
PI = math.pi
d = float(input('Masukan Diameter Bola '))
r = d/2
v = 4/3 * PI * r ** 3
p =round(v,2)
print ('JADI VOLUME BOLA =' ,p,'m kubik')
