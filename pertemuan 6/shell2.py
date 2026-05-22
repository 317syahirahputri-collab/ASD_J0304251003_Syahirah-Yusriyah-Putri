# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Shell Sort (Descending)
# ==========================================================

# Shell sort descending

def gapInsertionSort(data,start,gap):

    for i in range(start+gap,len(data),gap):

        currentvalue = data[i]
        position = i

        # kondisi dibalik agar descending
        while position>=gap and data[position-gap] < currentvalue:

            data[position] = data[position-gap]

            position = position-gap

        data[position] = currentvalue


def shellSort(data):

    sublistcount = len(data)//2

    while sublistcount > 0:

        for startposition in range(sublistcount):

            gapInsertionSort(data,startposition,sublistcount)

        sublistcount = sublistcount // 2


data = [54,26,93,17,77,31,44,55,20]

shellSort(data)

print(data)