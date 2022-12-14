from abc import ABC, abstractclassmethod
# Polymorphism = parent class punya fungsi sama dengan child class tapi isinya itu beda.
# Encapsulation = membatasi akses atribut 
# Inheritance = warisan
# Abstract = cetak biru dari class

#Abstract Class
class Tanaman(ABC):
    def menghasilkan_rasa(self):
        pass

#class parent dar sebuah class
class Buah(Tanaman):                            
    def __init__(self, jenis, rasa):
        self._jenis= jenis      # ini encapsulation
        self._rasa= rasa        # ini encapsulation

    # method buah
    def getjenis(self):
        return self._jenis
    # method buah
    def setjenis(self, jenis):
        self._jenis= jenis
    # method buah
    def menghasilkan_rasa(self):
        pass

#class child
class Durian(Buah):                 #inheritance (Durian inheritance dari buah)
    def __init__(self, jenis, rasa):
        super().__init__(jenis, rasa)
    # method Durian
    def menghasilkan_rasa(self):
        print('buah durian menghasilkan rasa yang begitu manis ')

class Lemon(Buah):                     #inheritancde
    def __init__(self, jenis, rasa):
        super().__init__(jenis, rasa)
    # method lemon
    def menghasilkan_rasa(self):
        print('buah lemon menghasilkan rasa yang kecut sekali ')

#interface
def tes_menghasilkan_rasa(buah):  #polymorphism
    buah.mengeluarkan_rasa()

#object
a = Durian("durian", True)
b = Lemon("Lemon", False)

#pemanggilan interface pada  kedua object dan nanti akan langsung keluar outputnya
a.menghasilkan_rasa()   #polymorphism nya
b.menghasilkan_rasa()   #polymorphism nya
