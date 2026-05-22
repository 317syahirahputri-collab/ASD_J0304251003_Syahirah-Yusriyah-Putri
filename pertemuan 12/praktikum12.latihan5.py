# ================================================
# Nama  : Syahirah Yusriyah Putri
# NIM   : J0403251003
# Kelas : TPLA1
# ================================================

# ================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ================================================

import heapq  # Modul priority queue untuk algoritma Dijkstra

# Graph berbobot merepresentasikan hubungan antar kota
# Bobot = jarak/waktu tempuh antar kota (dalam satuan tertentu)
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},  # Bogor ke Jakarta=5, ke Depok=2
    'Jakarta': {'Bandung': 7},               # Jakarta ke Bandung=7
    'Depok':   {'Jakarta': 2, 'Bandung': 6}, # Depok ke Jakarta=2, ke Bandung=6
    'Bandung': {}                             # Bandung = tujuan akhir
}

def dijkstra(graph, start):
    # Inisialisasi semua node dengan jarak tak terhingga
    distances = {node: float('inf') for node in graph}

    # Node awal memiliki jarak 0 ke dirinya sendiri
    distances[start] = 0

    # Priority queue dimulai dengan node awal
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari antrian
        current_distance, current_node = heapq.heappop(priority_queue)

        # Abaikan jika jarak ini sudah tidak relevan (ada yang lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Proses setiap tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak melalui current_node
            distance = current_distance + weight

            # Lakukan relaksasi jika ditemukan jalur lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Tentukan node awal
start_node = 'Bogor'

# Jalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Tampilkan output jarak terpendek dari Bogor ke semua kota
print(f"Jarak terpendek dari {start_node}:")
for node, distance in hasil.items():
    print(f"  {start_node} -> {node} : {distance}")

# ================================================
# Jawaban Analisis:

# Output yang diharapkan:
#   Bogor -> Bogor   : 0
#   Bogor -> Jakarta : 4
#   Bogor -> Depok   : 2
#   Bogor -> Bandung : 8

# 1. Node awal yang digunakan apa?
    """Node awal yang digunakan adalah 'Bogor'.
    Bogor ditetapkan sebagai titik keberangkatan (start_node),
    sehingga semua perhitungan jarak dimulai dan diukur dari Bogor.
    Jarak Bogor ke dirinya sendiri = 0."""

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
    """Node dengan jarak paling kecil dari Bogor adalah DEPOK dengan jarak 2.
    Ini karena edge Bogor -> Depok memiliki bobot 2, yang merupakan
    bobot terkecil dari semua edge yang keluar dari Bogor.
    Depok menjadi node pertama yang diproses setelah Bogor."""

# 3. Node mana yang memiliki jarak paling besar dari node awal?
    """Node dengan jarak paling besar dari Bogor adalah BANDUNG dengan jarak 8.
    Semua kemungkinan jalur ke Bandung:
    - Bogor -> Jakarta -> Bandung       = 5 + 7 = 12
    - Bogor -> Depok -> Bandung         = 2 + 6 = 8  ✓ (TERPENDEK)
    - Bogor -> Depok -> Jakarta -> Bandung = 2 + 2 + 7 = 11
    Jarak terpendek ke Bandung = 8, dan ini adalah jarak terbesar
    dibanding node lainnya (Depok=2, Jakarta=4)."""

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini:

    """INISIALISASI:
    distances = {Bogor:0, Jakarta:∞, Depok:∞, Bandung:∞}
    priority_queue = [(0, 'Bogor')]

    ITERASI 1 — Proses Bogor (jarak=0):
    - Periksa tetangga: Jakarta dan Depok
    - Jakarta: 0+5=5 < ∞ → distances[Jakarta] = 5
    - Depok  : 0+2=2 < ∞ → distances[Depok]   = 2
    - queue = [(2,'Depok'), (5,'Jakarta')]

    ITERASI 2 — Proses Depok (jarak=2, terkecil):
    - Periksa tetangga: Jakarta dan Bandung
    - Jakarta : 2+2=4 < 5 → distances[Jakarta]  = 4 (diperbarui!)
    - Bandung  : 2+6=8 < ∞ → distances[Bandung] = 8
    - queue = [(4,'Jakarta'), (5,'Jakarta_lama'), (8,'Bandung')]

    ITERASI 3 — Proses Jakarta (jarak=4):
    - Periksa tetangga: Bandung
    - Bandung: 4+7=11 > 8 → tidak diperbarui
    - queue = [(5,'Jakarta_lama'), (8,'Bandung')]

    ITERASI 4 — Proses Jakarta_lama (jarak=5):
    - 5 > distances[Jakarta]=4 → DILEWATI (sudah usang)

    ITERASI 5 — Proses Bandung (jarak=8):
    - Tidak ada tetangga → selesai

    HASIL AKHIR:
    Bogor=0, Depok=2, Jakarta=4, Bandung=8"""
# ================================================