# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPL A1
# ========================================================== 
# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 
# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file): 
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 

    Output: 
    - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int} 
    """ 
    stok_dict = {} 
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # hilangkan new line
            kode, nama_barang, stok = baris.split(",")  # pisahkan kolom
            stok_dict[kode] = {"nama": nama_barang, "stok": int(stok)}
    return stok_dict

buka_data = baca_stok(NAMA_FILE)
print("Jumlah item stock terbaca:", len(buka_data))
# TODO: Buka file dan baca seluruh baris 
# Hint: with open(nama_file, "r", encoding="utf-8") as f: 
# TODO: Untuk setiap baris: 
# - gunakan strip() untuk menghilangkan \n 
# - split(",") untuk memisahkan kolom 
# - simpan ke dictionary 

# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 
def simpan_stok(nama_file, stok_dict): 

    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in stok_dict:
            nama_barang = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            baris = f"{kode},{nama_barang},{stok}.strip()"
            f.write(baris)

simpan_stok(NAMA_FILE, buka_data)
print("Data berhasil disimpan.")

""" 
Menyimpan seluruh data stok ke file teks. 
Format per baris: KodeBarang,NamaBarang,Stok 
""" 
# TODO: Tulis ulang seluruh isi file berdasarkan stok_dict 
# Hint: with open(nama_file, "w", encoding="utf-8") as f: 
pass 
  
# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict): 
    print("\n=== DAFTAR STOCK BARANG KANTIN ===")
    print(f"{'KODE' : <10} | {'NAMA BARANG' : <20} | {'JUMLAH' :>7}")
    print("-"*45)

    for kode in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode]["nama_barang"]
        jumlah = stok_dict[kode]["jumlah"]
        print(f"{kode:<10} | {nama_barang:<20} | {int(jumlah):>7}")

    if not stok_dict:
        print("Stok kosong.")
        return
    
    tampilkan_semua(buka_data)
    """ 
    Menampilkan semua barang di stok_dict. 
    """ 



    print("Kode | Nama Barang        | Stok")
    print("-" * 35)
    for kode, info in stok_dict.items():
        print(f"{kode:<4} | {info['nama']:<18} | {info['stok']}")
# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 
def cari_barang(stok_dict): 
    """ 
    Mencari barang berdasarkan kode barang. 
    """ 
    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict:
        data = stok_dict[kode]
        print("Barang ditemukan:")
        print(f"Kode : {kode}")
        print(f"Nama : {data['nama']}")
        print(f"Stok : {data['stok']}")
    else:
        print("Barang tidak ditemukan.")

# TODO: Cek apakah kode ada di dictionary 
# Jika ada: tampilkan detail barang 
# Jika tidak ada: tampilkan 'Barang tidak ditemukan' 
pass 
# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict):
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode = input("Masukkan kode barang baru: ").strip() 

    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip() 

    try:
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print("Barang baru berhasil ditambahkan.") 
    simpan_stok(NAMA_FILE, stok_dict)

# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): 
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """ 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() 
 
    if kode not in stok_dict: 
        print("Kode barang tidak ditemukan.")
        return
 
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 
 
    pilihan = input("Masukkan pilihan (1/2): ").strip() 

    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah < 0:
            print("Jumlah tidak boleh negatif.")
            return
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    
    stock_sekarang = stok_dict[kode]["stok"]

    if pilihan == "1":
        stok_dict[kode]["stok"] = stock_sekarang + jumlah
        print(f"Stok untuk {kode} berhasil ditambah. Stok baru: {stok_dict[kode]['stok']}")
 
    elif pilihan == "2":
        if stock_sekarang - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] = stock_sekarang - jumlah
        print(f"Stok untuk {kode} berhasil dikurangi. Stok baru: {stok_dict[kode]['stok']}")
    else:
        print("Pilihan tidak valid. Update dibatalkan.")
        return
    
# ------------------------------- 
# Program Utama 
# ------------------------------- 
    def main(): 
    # Membaca data dari file saat program mulai 
        stok_barang = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 
# Menjalankan program utama 
    if __name__ == "__main__": 
        main()