# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])
    edges = []

    # Menambahkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Node awal apa yang digunakan?
"""
Node awal yang digunakan pada program adalah node A.
"""

# 2. Edge mana yang dipilih pertama kali?
"""
Edge pertama yang dipilih adalah A-C dengan bobot 2.

Hal ini karena dari node A, edge tersebut memiliki bobot paling kecil
dibandingkan edge lainnya.
"""

# 3. Bagaimana Prim menentukan edge berikutnya?
"""
Algoritma Prim memilih edge dengan bobot paling kecil yang
menghubungkan node yang sudah dikunjungi dengan node yang
belum dikunjungi.

Proses ini dilakukan secara bertahap sampai semua node
berhasil terhubung menjadi satu spanning tree.
"""

# 4. Berapa total bobot MST yang dihasilkan?
"""
Total bobot MST yang dihasilkan adalah 6.

Edge yang dipilih yaitu:
A-C = 2
C-D = 1
D-B = 3

Jika dijumlahkan:
2 + 1 + 3 = 6
"""

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
"""
Perbedaan utama terletak pada cara pemilihan edge.

Kruskal memilih edge dengan bobot paling kecil dari seluruh graph
secara global.

Sedangkan Prim memulai dari satu node awal lalu memperluas
tree sedikit demi sedikit dengan memilih edge terkecil yang
terhubung ke node berikutnya.

Jadi, Kruskal lebih fokus pada edge sedangkan Prim lebih fokus
pada pengembangan node atau tree.
"""