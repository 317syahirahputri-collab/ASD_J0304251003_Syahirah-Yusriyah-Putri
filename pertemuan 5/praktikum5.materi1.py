# ==========================================================
# Praktikum 5 - Materi 1
# Syahirah Yusriyah Putri - J0403251003
# Rekursi 1: Faktorial
# ==========================================================
def faktorial(n):
 # Base case: berhenti ketika n = 0
 if n == 0:
    return 1
 # Recursive case: masalah diperkecil menjadi faktorial(n-1)
 return n * faktorial(n - 1)
print(faktorial(5)) # Output: 120
print(faktorial(7)) # Output: 5040
print(faktorial(15)) # Output: 1307674368000