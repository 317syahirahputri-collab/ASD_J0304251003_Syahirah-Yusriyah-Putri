# ====== Stock Barang di Kantin ======

#penyimpanan data file
nama_file = r"C:\Users\syahi\OneDrive\Documents\PYTHON\algostruk\pertemuan 2\stock_barang.txt"

#menyimpan data stock barang kantin
def baca_data_stock(nama_file):
    data_dict = { } #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            kode, nama_barang, jumlah = baris.split(",") #ambil data per item data
            data_dict[kode] = {"nama_barang": nama_barang, "jumlah": int(jumlah)} 
    return data_dict

def simpan_data_stock(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in data_dict:
            nama_barang = data_dict[kode]["nama_barang"]
            jumlah = data_dict[kode]["jumlah"]
            baris = f"{kode},{nama_barang},{jumlah}\n"
            file.write(baris)

#memuat data stock dari file
data_stock = baca_data_stock(nama_file)
print("Jumlah item stock terbaca:", len(data_stock))

#menampilkan data stock
def tampilkan_data_stock(data_dict):
    print("\n=== DAFTAR STOCK BARANG KANTIN ===")
    print(f"{'KODE' : <10} | {'NAMA BARANG' : <20} | {'JUMLAH' :>7}")
    print("-"*45)

    for kode in sorted(data_dict.keys()):
        nama_barang = data_dict[kode]["nama_barang"]
        jumlah = data_dict[kode]["jumlah"]
        print(f"{kode:<10} | {nama_barang:<20} | {int(jumlah):>7}")

tampilkan_data_stock(data_stock)

#mencari data stock barang
def cari_data_stock(data_dict):
    kode_cari = input("Masukkan KODE barang yang akan dicari: ").strip()

    if kode_cari in data_dict:
        nama_barang = data_dict[kode_cari]["nama_barang"]
        jumlah = data_dict[kode_cari]["jumlah"]

        print("==== DATA BARANG DITEMUKAN ====")
        print(f"KODE        : {kode_cari}")
        print(f"NAMA BARANG : {nama_barang}")
        print(f"JUMLAH      : {jumlah}")
    else:
        print("Data barang tidak ditemukan.")

cari_data_stock(data_stock)

#update stock barang
def ubah_data_stock(data_dict):
    kode_ubah = input("Masukkan KODE barang yang akan diubah stoknya: ").strip()

    if kode_ubah in data_dict:
        nama_barang = data_dict[kode_ubah]["nama_barang"]
        jumlah_lama = data_dict[kode_ubah]["jumlah"]
        print(f"Stok lama untuk {nama_barang} (KODE: {kode_ubah}) adalah {jumlah_lama}")

        try:
            jumlah_baru = int(input("Masukkan jumlah stok baru: "))
            data_dict[kode_ubah]["jumlah"] = jumlah_baru
            print("Stok berhasil diperbarui.")
        except ValueError:
            print("Input tidak valid. Stok tidak diubah.")
    else:
        print("Data barang tidak ditemukan.")

ubah_data_stock(data_stock)
simpan_data_stock(nama_file, data_stock)
print("Data stock barang telah disimpan kembali ke file.")

#menyimpan data stock barang kembali ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in data_dict:
            nama_barang = data_dict[kode]["nama_barang"]
            jumlah = data_dict[kode]["jumlah"]
            baris = f"{kode},{nama_barang},{jumlah}\n"
            file.write(baris)

simpan_data(nama_file, data_stock)
print("Data stock barang telah disimpan kembali ke file.")

#menambah data stock barang baru
def tambah_data_stock(data_dict):
    kode_baru = input("Masukkan KODE barang baru: ").strip()

    if kode_baru in data_dict:
        print("KODE sudah ada. Penambahan dibatalkan.")
        return

    nama_barang = input("Masukkan NAMA BARANG: ").strip()
    try:
        jumlah = int(input("Masukkan JUMLAH stok: "))
        data_dict[kode_baru] = {"nama_barang": nama_barang, "jumlah": jumlah}
        print("Data barang baru berhasil ditambahkan.")
    except ValueError:
        print("Jumlah harus berupa angka. Penambahan dibatalkan.")
tambah_data_stock(data_stock)
simpan_data_stock(nama_file, data_stock)
print("Data stock barang telah disimpan kembali ke file.")

  #menu interaktif
def main():
    data_stock = baca_data_stock(nama_file)

    while True:
        print("\n=== MENU STOCK BARANG KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang") 
        print("3. Ubah stok barang")
        print("4. Tambah barang baru")
        print("5. Simpan data")
        print("6. Keluar")

        pilihan = input("Pilih menu : ").strip()

        if pilihan == "1":
            tampilkan_data_stock(data_stock)

        elif pilihan == "2":
            cari_data_stock(data_stock)

        elif pilihan == "3":
            ubah_data_stock(data_stock)

        elif pilihan == "4":
            tambah_data_stock(data_stock)

        elif pilihan == "5":
            simpan_data_stock(nama_file, data_stock)
            print("Data berhasil disimpan ke file!")    

        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini.")
            break      
        
# Menjalankan program utama 
    if __name__ == "__main__": 
        main()