# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 2 - Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Edge mana yang dipilih pertama kali?
"""
Edge pertama yang dipilih adalah C-D dengan bobot 1.

Hal ini karena algoritma Kruskal selalu memprioritaskan edge
dengan bobot paling kecil terlebih dahulu setelah data diurutkan.
"""

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
"""
Karena tujuan utama dari Minimum Spanning Tree adalah mendapatkan
total bobot atau biaya sekecil mungkin.

Dengan memilih edge yang bobotnya kecil terlebih dahulu,
algoritma dapat menghasilkan koneksi yang lebih efisien dan hemat biaya.
"""

# 3. Berapa total bobot MST yang dihasilkan?
"""
Total bobot MST yang dihasilkan adalah 6.

Hasil tersebut diperoleh dari penjumlahan:
C-D = 1
A-C = 2
B-D = 3

Sehingga:
1 + 2 + 3 = 6
"""

# 4. Mengapa edge tertentu tidak dipilih?
"""
Karena edge tersebut dapat membentuk cycle atau memiliki bobot
yang lebih besar dibanding edge lainnya.

Contohnya edge A-B dan A-D tidak dipilih karena seluruh node
sudah berhasil terhubung tanpa harus menggunakan edge tersebut.

Jika edge tambahan tetap dipilih, maka graph menjadi tidak efisien
karena terdapat jalur yang sebenarnya tidak diperlukan.
"""