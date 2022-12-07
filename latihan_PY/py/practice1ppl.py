#buatlah enkapsulasi
#buatlah masing masing parameter;
# siswa = public
# guru = protected
# kesek = private

#tampilkan
# 1. siswa namanya euroski
# 2. guru namanaya bu anita
# 3. kepsek namanya lilik

from typing import ClassVar


class siswa:
    def __init__(self, siswa):
        self.siswa = siswa
        
suuu = siswa("Euroski")
    
print('ini adalah public class')
print(f'nama : {suuu.siswa}\n')
    

class guru:
    def __init__(self, nama):
        self._nama = nama
    
class anita(guru):
    def __init__(self, nama):
        super().__init__(nama)
        
    def cantik(self):
        print(f'guru kami bernama {self._nama}')  
        
bu_guru = anita('bu anita\n')
bu_guru.cantik()
      
      
class kepsek:
    def __init__(self, nama):
        self.__nama = nama
        
    def tampilkan_nama(self):
        print(f'kepsek terhormat {pak.__nama}')
        
pak = kepsek('Pak L')
pak.tampilkan_nama()
    
