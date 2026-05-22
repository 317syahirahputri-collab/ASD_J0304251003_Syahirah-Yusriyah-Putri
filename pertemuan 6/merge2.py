# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Merge Sort (Descending)
# ==========================================================

# Merge sort descending

def mergeSort(data):

    if len(data) > 1:

        mid = len(data)//2

        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):

            # kondisi dibalik agar descending
            if lefthalf[i] >= righthalf[j]:

                data[k] = lefthalf[i]
                i += 1

            else:

                data[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):

            data[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):

            data[k] = righthalf[j]
            j += 1
            k += 1


data = [54,26,93,17,77,31,44,55,20]

mergeSort(data)

print(data)