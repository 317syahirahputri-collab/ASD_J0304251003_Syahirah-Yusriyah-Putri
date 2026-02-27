# ==========================================================
# Praktikum 5 - Materi 2
# Syahirah Yusriyah Putri - J0403251003
# Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n) # fase stacking
    hitung(n - 1) # pemanggilan rekursif
    print("Keluar:", n) # fase unwinding

hitung(3)
hitung(5)
hitung(10)