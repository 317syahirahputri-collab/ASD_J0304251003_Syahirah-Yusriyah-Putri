# ================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# ================================================

# ================================================
# Latihan 4: Studi Kasus Jalur Terpendek Antar Lokasi Kampus
# ================================================

import heapq  # Untuk priority queue dalam algoritma Dijkstra

# Graph merepresentasikan lokasi-lokasi di kampus beserta bobot jaraknya
# Bobot = waktu tempuh (menit) antar lokasi
graph = {
    'Gerbang':        {'Perpustakaan': 3, 'Kantin': 2},
    'Perpustakaan':   {'Lab': 4, 'Aula': 1},
    'Kantin':         {'Lab': 2, 'Aula': 7},
    'Lab':            {'Aula': 1},
    'Aula':           {}  # Tujuan akhir, tidak punya tetangga keluar
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak ke tak terhingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari titik awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: [(jarak, node)]
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak ini sudah usang (ada yang lebih kecil), lewati
        if current_distance > distances[current_node]:
            continue

        # Kunjungi semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak ke tetangga melalui node saat ini
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, lakukan pembaruan
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Jalankan Dijkstra mulai dari Gerbang
hasil = dijkstra(graph, 'Gerbang')

# Tampilkan jarak terpendek dari Gerbang ke semua lokasi
print("Jarak terpendek dari Gerbang:")
for node, distance in hasil.items():
    print(f"  Gerbang -> {node} : {distance} menit")

# ================================================
# Jawaban Analisis:

# 1. Lokasi mana yang paling dekat dari Gerbang?
    """Lokasi paling dekat dari Gerbang adalah KANTIN dengan jarak 2 menit.
    Gerbang terhubung langsung ke dua tempat:
    - Gerbang -> Kantin = 2 menit
    - Gerbang -> Perpustakaan = 3 menit
    Kantin memiliki bobot terkecil, sehingga menjadi node pertama
    yang diproses setelah Gerbang."""

# 2. Berapa jarak terpendek dari Gerbang ke Aula?
    """Jarak terpendek dari Gerbang ke Aula adalah 4 menit.
    Semua kemungkinan jalur:
    - Gerbang -> Perpustakaan -> Aula         = 3 + 1 = 4 ✓ (TERPENDEK)
    - Gerbang -> Kantin -> Lab -> Aula        = 2 + 2 + 1 = 5
    - Gerbang -> Kantin -> Aula               = 2 + 7 = 9
    - Gerbang -> Perpustakaan -> Lab -> Aula  = 3 + 4 + 1 = 8
    Jalur terpendek: Gerbang -> Perpustakaan -> Aula = 4 menit"""

# 3. Apakah jalur terpendek ke Lab selalu berasal dari Kantin? Jelaskan!
    """Dalam kasus ini dari Gerbang, jalur terpendek ke Lab MEMANG melalui
    Kantin, tetapi ini tidak selalu berlaku untuk semua kasus.
    Perbandingan jalur ke Lab:
    - Gerbang -> Kantin -> Lab        = 2 + 2 = 4 menit (terpendek)
    - Gerbang -> Perpustakaan -> Lab  = 3 + 4 = 7 menit
    Dari Gerbang, Kantin memberikan jalur lebih pendek ke Lab.
    Namun jika node awalnya berbeda (misal dari Perpustakaan),
    jalur terpendek ke Lab bisa langsung Perpustakaan -> Lab = 4,
    tanpa melalui Kantin sama sekali."""

# 4. Mengapa Dijkstra tepat digunakan pada kasus ini?
    """Dijkstra tepat digunakan karena:
    a) Semua bobot edge POSITIF (waktu tempuh tidak bisa negatif)
    b) Graf berarah (perjalanan dari A ke B tidak berarti ada jalur B ke A)
    c) Butuh jarak terpendek dari SATU sumber ke SEMUA tujuan (single-source)
    d) Efisiensi: O((V+E) log V) cocok untuk graf kampus yang tidak terlalu besar
    e) Bobot merepresentasikan waktu nyata yang selalu >= 0,
       sehingga asumsi greedy Dijkstra (jarak final setelah diproses) valid."""
# ================================================