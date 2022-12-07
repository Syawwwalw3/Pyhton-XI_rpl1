# membuat variabel atau box bernama buah
buah = ["apel", "durian", "kiwi", "alpukat", "mangga"]
sayur = ["pokcoy", "sledri", "kangkung", "bayem", "asem"]

#tampilkan data yang ada divariabel buah
#print (buah)

#tampilkan data berurutan dari awal hingga akhir 
#for gerobak in buah:
 #   print(gerobak)

 #tampilan hanya beberapa saja
 #print (buah[0])

#cara menambah nilai di dalam list 
#buah.append("semangka")

#cara menghapus yang ada di dalam buah
#buah.remove("kiwi")

#cara memotong nilai yang ada di box buah
#print (buah[0:4])

#operasi aritmatika
#dagang_hari_ini= buah + sayur
#for grobak in dagang_hari_ini:
 #   print (gerobak)

kasir = input ("mau tambah buah apa lagi ")
buah.append(kasir)
print(buah)