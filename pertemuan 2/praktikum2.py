#=====================================================
#praktikum 2:  konsep ADT file handling (STUDI KASUS)
#Latihan 1: Mmembuat fungsiload data
#=====================================================

#variabel menyimpan data file
nama_file = r"C:\Users\syahi\OneDrive\Documents\PYTHON\algostruk\pertemuan 2\data_mahasiswa.txt"


def baca_data(nama_file):
    data_dict = { } #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} 
    return data_dict

buka_data = baca_data(nama_file)
print ("jumlah data terbaca", len(buka_data)) #melihat berapa data yang di load

#======================================================
#praktikum 2:  konsep ADT file handling (STUDI KASUS)
#Latihan 2: Mmembuat fungsi menampilkan data
#======================================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("/n=== DAFTAR MAHASISWA===")
    print(f"{'NIM' : <10} | {'Nama : <12'} | {'Nilai :>5'}")
    print("-"*35) #membuat garis

    #menampilan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")

tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#=======================================================
#praktikum 2:  konsep ADT file handling (STUDI KASUS)
#Latihan 3: Mmembuat fungsi mencari data
#=======================================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang akan dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("==== DATA MAHASISWA DITEMUKAN ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. pastikan NIM yang dimasukkan benar")

#memanggil fungsi cari data
cari_data(buka_data)

#=====================================================
#praktikum 2:  konsep ADT file handling (STUDI KASUS)
#Latihan 4: Membuat fungsi update data
#=====================================================

#membuat fungsi update data
def ubah_data(data_dict):

    #awali dulu dengan mencari nim/data mahasiswa yang ingin  di update
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. update dibatalkan")

    if nilai_baru <0 or nilai_baru >100:
        print("Nilai harus anatara 0 sampai 100. update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#=====================================================
#praktikum 2:  konsep ADT file handling (STUDI KASUS)
#Latihan 5: Membuat fungsi menyimpan data pada file
#=====================================================

#membuat fungsi menyimpan data dalam file
def simpan_data(nama_file, data_dict):

    with open(nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nama"]
            file.write(f"{nim},{nama},{nilai}")

#memanggil fungsi simpan data
simpan_data(nama_file,buka_data)
print("/nData berhasil disimpan ke file")

#=====================================================
#praktikum 2:  konsep ADT file handling (STUDI KASUS)
#Latihan 6: Membuat menu interaktif
#=====================================================

def main():
    #load data otomatis daat program dimulai
    buka_data = baca_data(nama_file) #fs.1 fungsi load data

    while True:
        print("\n===MENU DATA MAHASISWA===")
        print("1. Tampilkan data mahasiswa")
        print("2. Cari data berdasarkan NIM")
        print("3. Ubah nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #memanggil fs.2 menampilkan data

        elif pilihan == "2":
            cari_data(buka_data) #memanggil fs.3 mencari data
        
        elif pilihan == "3":
            ubah_data(buka_data) #memanggil fs.4 mengubah data

        elif pilihan == "4":
            simpan_data(nama_file, buka_data)  #memanggil fs.5 menyimpan data ke file
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("program selesai.")
            break
    
    if __name__ == "__main__": 
        main()