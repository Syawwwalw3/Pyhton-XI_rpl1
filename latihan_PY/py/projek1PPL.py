# #selamat datang di jophel
# print("selamat datang di jphotel")
# print("--selamat datang , silaka pilih--")
# print("---no----tipe-----harga--")
# print("---1----suite-----1.000.000--")
# print("---2----royal-----500.000--")
# print("---3----bpjs-----250.000--")

# #sampe resepsionis (input data)

# cust = input("masukan nama lengkap :")
# tipe = int(input("tipe kamar : "))
# lama_inap = int(input("masukan lama inap :"))

# #tipe kamar 
# if tipe == 1:
#     print("suit")
# elif tipe == 2:
#     print ("royal")
# elif tipe == 3:
#     print("bpjs")


# ##bikin struk jp hotel

# print("pelanggan atas nama :",cust)
# if tipe == 1:
#     print("suit")
# elif tipe == 2:
#     print ("royal")
# elif tipe == 3:
#     print("bpjs")


# print("lama menginap: ",lama_inap)
# print("tipe kamar yg di palih",tipe)

#fungsi garis
def garis():
    print("=================================")

# SELAMAT DATANG DI JPHOTEL
garis()

print("--Selamat Datang DI JPHOTEL--")
print("--NO----TIPE--------HARGA--")
print("--01----Suite---1.000.000--")
print("--02----Royal-----500.000--")
print("--03----BPJS------250.000--")

# Sampe Resepsionis (input data)


cust = input("Masukan nama lengkap : ")
tipe = int(input("Tipe Kamar : "))
lama_inap = int(input("Masukan lama inap : "))

# struk JPHOTEL
print("Pelanggan atas nama : ", cust)
# tipe kamar
garis()
if tipe == 1:
   tipe_kamar=("suite")
elif tipe == 2:
    tipe_kamar=("royal")
elif tipe == 3:
    tipe_kamar=("bpjs")


#kalkulasi harga total
if tipe == 1:
    total_harga = 10000000*lama_inap
elif tipe == 2:
    total_harga = 500000*lama_inap
elif tipe == 3:
    total_harga = 250000*lama_inap


#sturk jphotel
print("pelangan atas nama : ",cust)
print("tipe kamar yg di pilih : ",tipe_kamar)
print("Lama menginap : ", lama_inap)
garis()
print("total :","Rp",total_harga,"00")