#latihan overloading

class angka:
    def __init__(self,angka):
        self.angka = angka
        
    def __add__(self, objek):
        self.angka = angka
    
    def __add__(self, objek):#magic method
        return self.angka + objek.angka
            
x1 = angka(28)
x2 = angka(30)
x1 + x2 