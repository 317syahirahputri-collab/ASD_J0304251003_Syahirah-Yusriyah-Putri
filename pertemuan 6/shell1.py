# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Shell Sort (Ascending)
# ==========================================================

# Fungsi gapInsertionSort digunakan untuk melakukan insertion sort
# tetapi dengan jarak tertentu (gap)

def gapInsertionSort(data,start,gap):

    for i in range(start+gap,len(data),gap):

        currentvalue = data[i]
        position = i

        # membandingkan elemen dengan jarak gap
        while position>=gap and data[position-gap] > currentvalue:

            data[position] = data[position-gap]

            position = position-gap

        data[position] = currentvalue


# fungsi utama shell sort
def shellSort(data):

    sublistcount = len(data)//2

    # selama gap masih lebih dari 0
    while sublistcount > 0:

        for startposition in range(sublistcount):

            gapInsertionSort(data,startposition,sublistcount)

        sublistcount = sublistcount // 2


data = [54,26,93,17,77,31,44,55,20]

shellSort(data)

print(data)