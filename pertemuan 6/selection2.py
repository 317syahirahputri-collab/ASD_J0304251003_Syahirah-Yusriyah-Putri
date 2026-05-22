# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Selection Sort (Descending)
# ==========================================================

# Fungsi selectionSort untuk mengurutkan data secara descending

def selectionSort(data):

    for fillslot in range(len(data)-1,0,-1):

        positionOfMax = 0

        # mencari nilai terkecil
        for location in range(1,fillslot+1):

            if data[location] < data[positionOfMax]:
                positionOfMax = location

        # proses pertukaran nilai
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [54,26,93,17,77,31,44,55,20]

selectionSort(data)

print(data)