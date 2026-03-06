# ==========================================================
# Nama  : Syahirah Yusriyah Putri 
# NIM   : J0403251003
# Kelas : TPL A1
# Deskripsi : Latihan 4 - Kombinasi huruf (backtracking)
# ==========================================================

def kombinasi(n, hasil=""):

    # Base case
    if len(hasil) == n:
        print(hasil)
        return

    # Choose & Explore
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


print("=== Kombinasi n=2 ===")
kombinasi(2)

print("\n=== Kombinasi n=3 ===")
kombinasi(3)


# Jumlah kombinasi = 2^n
# n=2 menghasilkan 4 kombinasi
# n=3 menghasilkan 8 kombinasi