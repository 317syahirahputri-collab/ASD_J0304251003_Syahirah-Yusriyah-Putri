# ==========================================================
# Praktikum 6
# Syahirah Yusriyah Putri - J0403251003
# Soal Pak Budi - Menentukan kandidat
# ==========================================================

# Data nilai tes potensi akademik pelamar

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Mengurutkan data dari nilai tertinggi ke terendah
data.sort(reverse=True)

print("Nilai setelah diurutkan (descending):")
print(data)

# Mengambil 5 nilai tertinggi
top5 = data[:5]

print("5 kandidat dengan nilai tertinggi:")
print(top5)