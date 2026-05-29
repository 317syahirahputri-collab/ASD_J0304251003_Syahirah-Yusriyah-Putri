# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 4 - Studi Kasus Jaringan Kabel Antar Gedung
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
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

print("Minimum Spanning Tree Jaringan Kabel:\n")

for edge in mst:
    print(edge)

print("\nTotal biaya minimum =", total_weight)

# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Algoritma apa yang digunakan?
"""
Program ini menggunakan algoritma Kruskal.

Algoritma Kruskal bekerja dengan cara mengurutkan seluruh edge
berdasarkan bobot terkecil, kemudian memilih edge yang tidak
membentuk cycle sampai semua node terhubung.
"""

# 2. Edge mana saja yang dipilih?
"""
Edge yang dipilih dalam MST adalah:
- GedungC - GedungD = 1
- GedungA - GedungC = 2
- GedungB - GedungD = 3

Ketiga edge tersebut dipilih karena menghasilkan total biaya
yang paling minimum.
"""

# 3. Berapa total biaya minimum?
"""
Total biaya minimum yang diperoleh adalah 6.

Perhitungannya:
1 + 2 + 3 = 6
"""

# 4. Mengapa MST cocok digunakan pada kasus ini?
"""
Karena MST dapat membantu menghubungkan seluruh gedung
menggunakan biaya kabel yang paling minimum.

Dengan menggunakan MST, seluruh gedung tetap dapat saling
terhubung tanpa perlu memasang kabel tambahan yang tidak diperlukan.

Konsep ini sangat cocok diterapkan pada pembangunan jaringan
internet, listrik, maupun infrastruktur lainnya agar lebih efisien.
"""