# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 5 - Tugas Mandiri MST
# Kasus: Jaringan Jalan Antar Kota
# ==========================================================

# Daftar edge: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

# Proses algoritma Kruskal
for weight, u, v in edges:

    # Memastikan edge tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:\n")

for edge in mst:
    print(edge)

print("\nTotal bobot minimum =", total_weight)

# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Kasus apa yang dipilih?
"""
Kasus yang dipilih adalah jaringan jalan antar kota.
"""

# 2. Algoritma apa yang digunakan?
"""
Algoritma yang digunakan adalah algoritma Kruskal.

Algoritma ini memilih edge dengan bobot paling kecil terlebih dahulu
agar diperoleh jalur dengan total biaya minimum.
"""

# 3. Edge mana saja yang dipilih dalam MST?
"""
Edge yang dipilih yaitu:
- Bogor - Depok = 2
- Depok - Jakarta = 3
- Depok - Bandung = 4

Edge tersebut dipilih karena dapat menghubungkan seluruh kota
dengan total bobot paling kecil.
"""

# 4. Berapa total bobot MST?
"""
Total bobot MST yang dihasilkan adalah 9.

Perhitungannya:
2 + 3 + 4 = 9
"""

# 5. Mengapa edge tertentu tidak dipilih?
"""
Karena edge tersebut memiliki bobot yang lebih besar dan tidak
dibutuhkan lagi untuk menghubungkan seluruh kota.

Contohnya edge Bogor - Jakarta dan Jakarta - Bandung tidak dipilih
karena semua kota sudah saling terhubung menggunakan jalur dengan
biaya yang lebih kecil.

Jika edge tersebut tetap digunakan, maka total biaya jaringan
akan menjadi lebih besar dan kurang efisien.
"""