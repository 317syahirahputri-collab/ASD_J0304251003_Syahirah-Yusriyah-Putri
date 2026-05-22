# ================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# Praktikum 12 - Graf II: Shortest Path
# ================================================

# ================================================
# Latihan 3: Mencoba Algoritma Bellman Ford
# ================================================

# Weighted graph dengan bobot NEGATIF
# Dijkstra tidak bisa menangani ini, maka digunakan Bellman-Ford
graph = {
    'A': {'B': 1, 'C': 4},   # A ke B bobot 1, A ke C bobot 4
    'B': {'C': -2, 'D': 5},  # B ke C bobot -2 (negatif!), B ke D bobot 5
    'C': {'D': 1}             # C ke D bobot 1
}

def bellman_ford(graph, start):
    # Inisialisasi semua jarak ke tak terhingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak (jumlah node - 1) kali
    # Kenapa V-1? Karena jalur terpendek maksimal melewati V-1 edge
    for _ in range(len(graph) - 1):

        # Periksa SETIAP edge dalam graph (berbeda dari Dijkstra)
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Relaksasi: jika jarak melalui node ini lebih kecil, perbarui
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

# Jalankan Bellman-Ford dari node 'A'
hasil = bellman_ford(graph, 'A')

# Tampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"  A -> {node} : {distance}")

# ================================================
# Jawaban Analisis:

# 1. Berapa jarak terpendek dari A ke B?
    """Jarak terpendek dari A ke B adalah 1.
    Hanya ada satu jalur: A -> B langsung dengan bobot 1.
    Tidak ada jalur alternatif ke B, jadi jaraknya tetap 1."""

# 2. Berapa jarak terpendek dari A ke C?
    """Jarak terpendek dari A ke C adalah -1.
    Ada dua jalur:
    - A -> C langsung = 4
    - A -> B -> C = 1 + (-2) = -1
    Karena -1 < 4, jalur A -> B -> C dipilih sebagai jalur terpendek.
    Inilah mengapa bobot negatif penting: bisa menghasilkan jarak
    yang lebih kecil dari jalur langsung."""

# 3. Jalur mana yang lebih pendek dari A ke C, jalur langsung atau melalui B?
    """Jalur melalui B jauh lebih pendek:
    - Langsung A -> C = 4
    - Melalui B: A -> B -> C = 1 + (-2) = -1
    Selisih: 4 - (-1) = 5, jalur via B lebih pendek 5 satuan.
    Bobot negatif pada edge B->C (-2) adalah kunci mengapa
    jalur memutar justru lebih pendek dari jalur langsung."""

# 4. Apa perbedaan cara Bellman-Ford vs Dijkstra dalam melakukan relaksasi?
""" 
   DIJKSTRA:
    - Menggunakan priority queue (min-heap)
    - Memproses node berurutan dari jarak terkecil (greedy)
    - Hanya merelaksasi tetangga dari node yang sedang diproses
    - Setiap node hanya diproses SATU KALI
    - Kompleksitas: O((V + E) log V)
    - TIDAK bisa menangani bobot negatif
  BELLMAN-FORD:
    - Tidak menggunakan priority queue
    - Memeriksa SEMUA edge pada setiap iterasi
    - Melakukan relaksasi sebanyak (V-1) kali putaran penuh
    - Edge yang sama bisa direlaksasi berkali-kali
    - Kompleksitas: O(V * E) — lebih lambat dari Dijkstra
    - BISA menangani bobot negatif
    - Bisa mendeteksi negative cycle (jika masih ada perubahan setelah V-1 iterasi, berarti ada siklus negatif)"""
# ================================================