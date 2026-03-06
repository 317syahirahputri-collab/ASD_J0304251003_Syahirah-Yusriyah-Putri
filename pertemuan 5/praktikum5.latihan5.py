# ==========================================================
# Nama  : Syahirah Yusriyah Putri 
# NIM   : J0403251003
# Kelas : TPL A1
# Deskripsi : Studi Kasus - Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):

    # Base case
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Backtracking
    for angka in ["0", "1", "2"]:
        if angka not in hasil:  # Mencegah angka berulang
            buat_pin(panjang, hasil + angka)


print("=== PIN 2 Digit ===")
buat_pin(2)

print("\n=== PIN 3 Digit ===")
buat_pin(3)


# Total kombinasi:
# 2 digit = 3^2 = 9
# 3 digit = 3^3 = 27
#
# Untuk mencegah angka berulang:
# Tambahkan kondisi:
# if angka not in hasil:
# sebelum pemanggilan rekursif seperti pada line 17, maka tidak akan ada angka yang muncul berulang.