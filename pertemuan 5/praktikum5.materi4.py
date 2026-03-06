# ==========================================================
# Praktikum 5 - Materi 4
# Syahirah Yusriyah Putri - J0403251003
# Backtracking 1: KOmbinasi biner (n)
# ==========================================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")
biner(3)