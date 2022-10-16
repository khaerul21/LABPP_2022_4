#faktorial 
from codecs import xmlcharrefreplace_errors


x = int(input("masukan bilangan = " ))
def factorial(x):
    if x==0:
        return 1

    elif x<0:
        return("bilangan tak terdefinisi")
    
    else:
        return(x * factorial(x-1))

print(factorial(x))
        



