# ==========================================================
# Nama  : Syahirah Yusriyah Putri 
# NIM   : J0403251003
# Kelas : TPL A1
# Deskripsi : Latihan 2 - Tracing Rekursi 
# ==========================================================

def countdown(n):
    # Base case:
    # Jika n == 0, program berhenti
    if n == 0:
        print("Selesai")
        return

    # Fase Masuk (Stacking)
    print("Masuk:", n)

    # Pemanggilan rekursif
    countdown(n - 1)

    # Fase Keluar (Unwinding)
    print("Keluar:", n)

# Pemanggilan 1
print("=== Countdown 3 ===")
countdown(3)

# Pemanggilan 2
print("\n=== Countdown 2 ===")
countdown(2)


# Mengapa "Keluar" terbalik?
# Karena sistem Call Stack bersifat LIFO (Last In First Out) karena itulah output nya terbalik.
