# Jenis enkapsulasi : public, protected, private

# Membuat public class

class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;
        
#instansilasi
segitiga_besar = segitiga(100,80)

#print
print('Ini adalah public class')
print(f'Alas : (segitiga_besar.alas)')
print(f'Tinggi : (segitiga_besar.tinggi)')
print(f'Tinggi : (segitiga_besar.luas)\n')

#membuat protected class
class mobil: #class induk
    def __init__(self,merk):
        self._merk = merk #protected class declaration
        
class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk) #pangggil merk dibagian sini
        self._total_gear = total_gear
        
        def pamer(self):
            #hak akses _merk dari subclass
            print(f'ini adalah mobil {self._merk} dengan total gear nya (self._total_gear)\n')
            
#instansiasi
ferrari = mobilefwan('ferrari',8)
ferrari.pamer()

#membuat private class
class motor:
    def __init__(self,merk):
        self.__merk = merk #private class declaration
        
    def tampilankan_merk(self):
        print(f'Merk motornya : (self.__merk)')
        
#instansilasi
moge = motor('Harley')
print(f'Merk motornya : (moge.__merk)')
moge.tampilankan_merk()