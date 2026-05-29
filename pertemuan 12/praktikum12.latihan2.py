# ================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# ================================================

# ================================================
# Latihan 2: Implementasi Algoritma Dijkstra
# ================================================

import heapq  # Modul untuk priority queue (min-heap)

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 1, 'C': 4},  # A ke B bobot 1, A ke C bobot 4
    'B': {'C': 2, 'D': 5},  # B ke C bobot 2, B ke D bobot 5
    'C': {'D': 1},           # C ke D bobot 1
    'D': {}                  # D adalah node tujuan akhir
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak ke tak terhingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node start ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue berisi tuple (jarak, node)
    # heapq selalu mengambil elemen dengan nilai terkecil lebih dulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari yang sudah tercatat, lewati
        # (artinya node ini sudah diproses dengan jarak lebih kecil sebelumnya)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru melalui node saat ini
            distance = current_distance + weight

            # Jika jarak baru lebih kecil dari jarak yang sudah diketahui
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Perbarui jarak
                # Masukkan tetangga ke priority queue dengan jarak baru
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Jalankan Dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')

# Tampilkan hasil jarak terpendek dari A ke semua node
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"  A -> {node} : {distance}")

# ================================================
# Jawaban Analisis:

# 1. Berapa jarak terpendek dari A ke C?
    """Jarak terpendek dari A ke C adalah 3.
    Bukan lewat jalur langsung A->C (bobot 4),
    melainkan lewat A->B->C = 1 + 2 = 3.
    Dijkstra menemukan ini karena saat memproses B (jarak 1),
    ia menemukan jarak ke C = 1+2 = 3, lebih kecil dari 4."""

# 2. Berapa jarak terpendek dari A ke D?
    """Jarak terpendek dari A ke D adalah 4.
    Jalurnya: A -> B -> C -> D = 1 + 2 + 1 = 4.
    Lebih pendek dari A -> B -> D = 1 + 5 = 6."""

# 3. Node mana saja yang dikunjungi sebelum mencapai D?
    """Urutan kunjungan node:
    - A (jarak 0) → diproses pertama karena jarak = 0
    - B (jarak 1) → tetangga A dengan jarak terkecil
    - C (jarak 3) → diperbarui dari B, lebih kecil dari jalur langsung A->C
    - D (jarak 4) → diperbarui dari C
    Jadi node yang dikunjungi sebelum D: A, B, C"""

# 4. Mengapa Dijkstra tidak bisa digunakan untuk graph dengan bobot negatif?
    """Dijkstra menggunakan prinsip GREEDY: setelah sebuah node diproses
    (diambil dari priority queue), jaraknya dianggap FINAL dan tidak
    akan diperbarui lagi. Asumsi ini hanya valid jika semua bobot positif,
    karena menambah edge positif selalu menghasilkan jarak yang lebih besar.
    Jika ada bobot negatif, bisa saja ada jalur yang lebih pendek melalui
    node yang sudah "selesai" diproses, sehingga hasil Dijkstra bisa salah.
    Untuk graph berbobot negatif, digunakan algoritma Bellman-Ford."""
# ================================================