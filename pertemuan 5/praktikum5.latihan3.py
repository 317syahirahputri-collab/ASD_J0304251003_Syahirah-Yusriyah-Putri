# ==========================================================
# Nama  : Syahirah Yusriyah Putri 
# NIM   : J0403251003
# Kelas : TPL A1
# Deskripsi : Latihan 3 - Mencari Nilai maksimum
# ==========================================================

def cari_maks(data, index=0):

    # Base case: jika sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]

    # Recursive case: cari maksimum dari sisa list
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


# maks 1
angka1 = [3, 7, 2, 9, 5]
print("List:", angka1)
print("Nilai maksimum:", cari_maks(angka1))

# maks 2
angka2 = [10, 4, 15, 8]
print("\nList:", angka2)
print("Nilai maksimum:", cari_maks(angka2))


# Penjelasan:
# Fungsi bergerak sampai elemen terakhir, lalu membandingkan dari belakang ke depan.