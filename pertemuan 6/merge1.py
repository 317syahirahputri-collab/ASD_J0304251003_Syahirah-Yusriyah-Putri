# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Merge Sort (Ascending)
# ==========================================================

# Fungsi mergeSort menggunakan metode divide and conquer
# Data dibagi menjadi dua bagian lalu digabung kembali

def mergeSort(data):

    if len(data) > 1:

        mid = len(data)//2

        lefthalf = data[:mid]
        righthalf = data[mid:]

        # rekursi
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        # menggabungkan dua list
        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] <= righthalf[j]:

                data[k] = lefthalf[i]
                i = i + 1

            else:

                data[k] = righthalf[j]
                j = j + 1

            k = k + 1

        while i < len(lefthalf):

            data[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):

            data[k] = righthalf[j]
            j = j + 1
            k = k + 1


data = [54,26,93,17,77,31,44,55,20]

mergeSort(data)

print(data)