# ==========================================================
# Nama  : Syahirah Yusriyah Putri 
# NIM   : J0403251003
# Kelas : TPL A1
# Deskripsi : Latihan 1 - Rekursi Pangkat
# ==========================================================

# Fungsi rekursif untuk menghitung a^n
def pangkat(a, n):
    # Base case:
    # Jika pangkat (n) = 0, maka hasilnya adalah 1
    # Karena bilangan apapun berpangkat 0 hasilnya 1
    if n == 0:
        return 1

    # Recursive case:
    # a^n = a × a^(n-1)
    # Masalah diperkecil dengan mengurangi n satu per satu
    return a * pangkat(a, n - 1)

# Pemanggilan fungsi
print(pangkat(2, 4))  # Output: 16
print(pangkat(3, 0))  # Output: 243


# =========================
# PENJELASAN DISKUSI
# =========================
# Contoh alur pangkat(2,4):
# pangkat(2,4)
# = 2 * pangkat(2,3)
# = 2 * 2 * pangkat(2,2)
# = 2 * 2 * 2 * pangkat(2,1)
# = 2 * 2 * 2 * 2 * pangkat(2,0)
# = 2 * 2 * 2 * 2 * 1  (Base case)
# = 16
#
# Base case menghentikan rekursi.
# Recursive case memperkecil masalah hingga mencapai base case.