#Buat 3 objek, orang , pelajar, pekerja
#orang = kelas induk
#pelajar , pekerja = kelas turunan

class orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        print("Fuungsi init dieksekusi")
        
    def perkenalan(self):
        print("Helo nama saya",self.nama,"dari",self.asal)
        
class pelajar(orang):
    def __init__(self, nama, asal, sekolah):
        orang.__init__(self,nama, asal)
        self.sekolah = sekolah 
       
class pekerja(orang):
    def __init__(self, nama, asal, kantor):
       super().__init__(nama, asal)
       self.kantor = kantor
       
andi = orang('Andi', 'Jakarta\n')
andi.perkenalan()

tito = pelajar('Tito', 'Subang' , 'SMKJP1')
tito.perkenalan()
print(f'Saya Sekolah di {tito.sekolah}\n')

cahyo = pekerja('Cahyo', 'Bandung','SMKJP1')
cahyo.perkenalan()
print(f'Saya Kerja di {cahyo.kantor}')