# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Bubble Sort (Descending)
# ==========================================================

# Fungsi Bubble Sort untuk mengurutkan data secara menurun (descending)

def shortBubbleSort(alist):

    exchanges = True
    passnum = len(alist)-1

    while passnum > 0 and exchanges:

        exchanges = False

        for i in range(passnum):

            # kondisi dibalik agar urutan menjadi dari besar ke kecil
            if alist[i] < alist[i+1]:

                exchanges = True

                # menukar posisi dua elemen
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        passnum = passnum - 1


alist=[20,30,40,90,50,60,70,80,100,110]

shortBubbleSort(alist)

print(alist)