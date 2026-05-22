# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Insertion Sort (Ascending)
# ==========================================================

# Fungsi insertionSort untuk mengurutkan data secara ascending
# Ascending berarti dari nilai terkecil ke terbesar

def insertionSort(data):

    # perulangan dimulai dari indeks ke-1
    for index in range(1, len(data)):

        currentvalue = data[index]   # menyimpan nilai yang sedang diperiksa
        position = index             # posisi awal nilai tersebut

        # membandingkan dengan elemen sebelumnya
        while position > 0 and data[position-1] > currentvalue:

            # menggeser elemen ke kanan
            data[position] = data[position-1]

            position = position - 1

        # menempatkan nilai pada posisi yang benar
        data[position] = currentvalue


data = [54,26,93,17,77,31,44,55,20]

insertionSort(data)

print(data)