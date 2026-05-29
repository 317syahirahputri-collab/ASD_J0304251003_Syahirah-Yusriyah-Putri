# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")

for edge in edges:
    print(edge)

print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
"""
Graph awal masih memiliki semua edge yang tersedia sehingga
masih terdapat beberapa jalur yang saling terhubung dan bisa
membentuk cycle.

Sedangkan spanning tree hanya mengambil edge yang benar-benar
dibutuhkan agar semua node tetap terhubung tanpa adanya cycle.

Jadi, spanning tree bisa dibilang merupakan versi lebih sederhana
dan lebih efisien dari graph awal karena jumlah edge yang digunakan
lebih sedikit.
"""

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
"""
Karena jika terdapat cycle, berarti ada jalur tambahan yang
sebenarnya tidak diperlukan untuk menghubungkan node.

Cycle juga membuat penggunaan edge menjadi berlebihan dan
menyebabkan biaya koneksi menjadi lebih besar.

Dalam penerapan nyata seperti jaringan internet atau kabel listrik,
cycle dapat menyebabkan pemborosan biaya pemasangan.
"""

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
"""
Karena spanning tree hanya mengambil edge minimum yang diperlukan
untuk menghubungkan seluruh node.

Jika jumlah edge terlalu banyak, maka kemungkinan besar graph akan
membentuk cycle.

Secara teori, jika terdapat n node maka spanning tree hanya memiliki
n - 1 edge agar semua node tetap terhubung dengan efisien.
"""