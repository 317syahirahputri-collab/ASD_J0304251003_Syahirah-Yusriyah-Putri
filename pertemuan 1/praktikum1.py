#=========================================================
#praktikum 1 : Konsep ADT dan File Handling
#Pelatihan Dasar 1 : Membaca seluruh isi file data
#=========================================================

print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe data :",type(isi_file))

#membuka file per baris
print("====Membuka file per baris====")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke-", jumlah_baris)
        print("isi nya :", baris)

#=========================================================
#praktikum 1 : Konsep ADT dan File Handling
#Pelatihan Dasar 2 : pasing data
#=========================================================
print("====Membuka file per baris====")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke-", jumlah_baris)
        print("isi nya :", baris)

#parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom kolom data

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data data satuan dan simpan ke variabel
        print("NIM:", nim,"|Nama :", nama, "|Nilai :", nilai)

#========================================================================
#praktikum 1 : Konsep ADT dan File Handling
#Pelatihan Dasar 3 : Membaca data dan menyimpannya ke struktur list
#========================================================================

data_list =[] #inisialisasi list untuk menampung data

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #menyimpan data ke list
print("====Menampilkan List====")
print(data_list)
print("contoh record ke 1", data_list[0])
print("contoh record ke 2", data_list[1])

#========================================================================
#praktikum 1 : Konsep ADT dan File Handling
#Pelatihan Dasar 4 : Membaca data dan menyimpan ke struktur data dictionary
#========================================================================

data_dict = {} #inisialisasi dictionary

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data data satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("===Menampilkan data Dictionary===")
print(data_dict)