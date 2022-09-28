# mengkonversi nilai bentuk angka ke huruf 
 
 

x= int(input('nilai ='))

if x >= 90 and x <= 100:
    hasil= 'A'
    print('> nilai dari', x, "= '", hasil, "'")
elif x >= 80 and x < 90 :
    hasil= 'B'
    print('> nilai dari', x, "= '", hasil, "'") 
elif x >= 70 and x < 80:
    hasil= 'C'
    print('> nilai dari', x, "= '", hasil, "'")
elif x>= 60 and x < 70:
    hasil= 'D'
    print('> nilai dari', x, "= '", hasil, "'") 
elif x>= 40 and x < 60:
    hasil= 'E'
    print('> nilai dari', x, "= '", hasil, "'")
elif x < 40 and x > 0:
    hasil= 'F'
    print('> nilai dari', x, "= '", hasil, "'")    

else :
    print('inputan salah, masukan nilai 0-100')
    
    
