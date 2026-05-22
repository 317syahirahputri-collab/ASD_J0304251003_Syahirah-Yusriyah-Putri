# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Insertion Sort (Descending)
# ==========================================================

# Insertion Sort untuk urutan descending
# Descending berarti dari nilai terbesar ke terkecil

def insertionSort(data):

    for index in range(1, len(data)):

        currentvalue = data[index]
        position = index

        # kondisi dibalik agar menghasilkan urutan menurun
        while position > 0 and data[position-1] < currentvalue:

            data[position] = data[position-1]

            position = position - 1

        data[position] = currentvalue


data = [54,26,93,17,77,31,44,55,20]

insertionSort(data)

print(data)