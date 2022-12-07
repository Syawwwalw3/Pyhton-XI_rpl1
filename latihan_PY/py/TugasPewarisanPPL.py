#Buat 3 objek, Agama, Islam, Kristen 
#Agama = kelas induk
#Islam , Kristen = kelas turunan



class Agama():
    def _init_(self, nama, agama ):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print(self.nama,"beragama",self.agama)

class sholat(Agama):
    def _init_(self, nama, agama, caraberibadah):
        Agama._init_(self,nama, agama)
        self.caraberibadah = caraberibadah

class sembahyang(Agama):
    def _init_(self, nama, agama, carasembahyang):
        Agama._init_(self,nama, agama)
        self.carasembahyang = carasembahyang


#menampilkan
hisyam = sholat('hisyam','islam','sholat')
hisyam.perkenalan()
print(f'Hisyam beribadah dengan melakukan {hisyam.caraberibadah}\n')

abraham = sembahyang('abraham','kristen','sembahyang')
abraham.perkenalan()
print(f'Abraham beribadah dengan melakukan {abraham.carasembahyang}')