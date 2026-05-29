# ================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# ================================================

# ================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ================================================

# Representasi weighted graph menggunakan dictionary bersarang
# Setiap key adalah node, valuenya adalah dictionary tetangga beserta bobotnya
graph = {
    'A': {'B': 4, 'C': 2},  # A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},           # B terhubung ke D (bobot 5)
    'C': {'B': 1, 'D': 1},  # C terhubung ke B (bobot 1) dan D (bobot 1)
    'D': {}                  # D tidak punya tetangga (node tujuan akhir)
}

# Menghitung total bobot jalur 1: A -> B -> D
# graph['A']['B'] = bobot dari A ke B = 4
# graph['B']['D'] = bobot dari B ke D = 5
jalur_1 = graph['A']['B'] + graph['B']['D']  # 4 + 5 = 9

# Menghitung total bobot jalur 2: A -> C -> B -> D
# graph['A']['C'] = bobot dari A ke C = 2
# graph['C']['B'] = bobot dari C ke B = 1 (tidak langsung ke D)
# Catatan: di graph ini C->D = 1, bukan C->B->D
jalur_2 = graph['A']['C'] + graph['C']['D']  # 2 + 1 = 3 (A -> C -> D)

print("Jalur 1: A -> B -> D =", jalur_1)  # Output: 9
print("Jalur 2: A -> C -> D =", jalur_2)  # Output: 3

# Membandingkan kedua jalur dan mencetak jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ================================================
# Jawaban Analisis:

# 1. Berapa total bobot jalur A -> B -> D?
    """Jalur A -> B -> D:
    - A ke B = 4
    - B ke D = 5
    Total = 4 + 5 = 9"""

# 2. Berapa total bobot jalur A -> C -> D?
    """Jalur A -> C -> D:
    - A ke C = 2
    - C ke D = 1
    Total = 2 + 1 = 3"""

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
    """Jalur terpendek adalah A -> C -> D dengan total bobot = 3 karena 3 < 9"""

# 4. Apakah jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
    """Benar, jalur terpendek TIDAK selalu ditentukan dari jumlah
    edge yang paling sedikit. Jalur terpendek ditentukan dari
    total BOBOT (weight) terkecil. Contoh pada kasus ini:
    - Jalur A->B->D memiliki 2 edge, tapi total bobot = 9
    - Jalur A->C->D juga memiliki 2 edge, total bobot = 3
   Dalam weighted graph, yang diperhitungkan adalah total bobot,
    bukan jumlah edge/langkah yang ditempuh."""
# ================================================