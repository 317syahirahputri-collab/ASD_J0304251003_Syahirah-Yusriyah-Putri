# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Selection Sort (Ascending)
# ==========================================================

# Fungsi selectionSort digunakan untuk mengurutkan data
# dengan mencari nilai terbesar pada setiap iterasi

def selectionSort(data):

    # iterasi dimulai dari indeks terakhir menuju awal
    for fillslot in range(len(data)-1,0,-1):

        positionOfMax = 0  # menyimpan posisi nilai terbesar sementara

        # mencari nilai terbesar dalam bagian list yang belum terurut
        for location in range(1,fillslot+1):

            if data[location] > data[positionOfMax]:
                positionOfMax = location

        # proses pertukaran posisi
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


# data yang akan diurutkan
data = [54,26,93,17,77,31,44,55,20]

# memanggil fungsi sorting
selectionSort(data)

# menampilkan hasil
print(data)