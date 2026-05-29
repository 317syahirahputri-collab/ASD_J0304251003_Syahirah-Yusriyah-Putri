# ==========================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 12 - Graph II: Shortest Path
# File  : praktikum12.materi1.py
# ==========================================================

# Mengimpor library heapq untuk priority queue
import heapq

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Fungsi algoritma Dijkstra
def dijkstra(graph, start):

    # Menyimpan jarak minimum setiap node
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Memeriksa semua tetangga node
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Menjalankan algoritma
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Hasil shortest path:")
print(hasil)