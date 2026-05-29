# ==========================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 12 - Graph II: Shortest Path
# File  : praktikum12.materi2.py
# ==========================================================

# Fungsi algoritma Bellman-Ford
def bellman_ford(graph, start):

    # Menyimpan jarak awal semua node
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Relaksasi seluruh edge sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():

                # Jika ditemukan jalur lebih kecil
                if distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

# Menjalankan algoritma
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Hasil shortest path Bellman-Ford:")
print(hasil)

# Penjelasan:
# Jalur langsung A -> B = 5
# Jalur A -> C -> B = 4 + (-2) = 2
# Jalur melalui C lebih kecil