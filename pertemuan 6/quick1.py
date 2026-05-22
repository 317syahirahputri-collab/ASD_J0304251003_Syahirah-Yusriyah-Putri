# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Quick Sort (Ascending)
# ==========================================================

# fungsi utama quick sort
def quickSort(data):

    # memanggil fungsi helper dengan indeks awal dan akhir
    quickSortHelper(data,0,len(data)-1)


def quickSortHelper(data,first,last):

    # jika indeks awal masih lebih kecil dari indeks akhir
    if first < last:

        # mencari posisi pivot yang tepat
        splitpoint = partition(data,first,last)

        # rekursi untuk bagian kiri pivot
        quickSortHelper(data,first,splitpoint-1)

        # rekursi untuk bagian kanan pivot
        quickSortHelper(data,splitpoint+1,last)


# fungsi untuk membagi data berdasarkan pivot
def partition(data,first,last):

    pivotvalue = data[first]  # pivot diambil dari elemen pertama

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        # mencari elemen yang lebih besar dari pivot
        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        # mencari elemen yang lebih kecil dari pivot
        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        # jika kedua penanda bertemu
        if rightmark < leftmark:
            done = True
        else:
            # menukar posisi elemen kiri dan kanan
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    # menukar pivot dengan posisi yang benar
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark


data = [54,26,93,17,77,31,44,55,20]

quickSort(data)

print(data)