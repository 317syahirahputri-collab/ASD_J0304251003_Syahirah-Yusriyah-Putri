# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Bubble Sort (Ascending)
# ==========================================================

# Fungsi shortBubbleSort digunakan untuk mengurutkan data
# menggunakan algoritma Bubble Sort yang lebih efisien

def shortBubbleSort(alist):

    exchanges = True      # variabel untuk mengecek apakah ada pertukaran data
    passnum = len(alist)-1  # jumlah iterasi maksimum (panjang list - 1)

    # perulangan akan berjalan selama passnum > 0 dan masih ada pertukaran data
    while passnum > 0 and exchanges:

        exchanges = False   # diasumsikan tidak ada pertukaran

        # perulangan untuk membandingkan elemen yang bersebelahan
        for i in range(passnum):

            # jika elemen kiri lebih besar dari elemen kanan
            if alist[i] > alist[i+1]:

                exchanges = True  # berarti terjadi pertukaran

                # proses pertukaran nilai
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        # mengurangi jumlah iterasi karena elemen terbesar sudah berada di posisi akhir
        passnum = passnum - 1


# data yang akan diurutkan
alist=[20,30,40,90,50,60,70,80,100,110]

# memanggil fungsi sorting
shortBubbleSort(alist)

# menampilkan hasil pengurutan
print(alist)