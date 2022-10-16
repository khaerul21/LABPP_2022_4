#cari FPB dari dua bilangan
def hitung_FPB(a,b):
    if (b==0):
        return a
    else:
        return hitung_FPB(b,a%b)

a = int(input('masukan bilangan'))
b = int(input('masukan bilangan'))
if a == 0 or b == 0:
    print('infinity')
elif a < 0 :
    print(f'FPB dari {a} dan {b} = {-hitung_FPB(a,b)}')
elif b < 0 :
    print(f'FPB dari {a} dan {b} = {hitung_FPB(a,b)}')
else:
    print(f'FPB dari {a} dan {b} = {hitung_FPB(a,b)}')
          
        




    
    
    