import random

# Menghasilkan angka acak antara 1 dan 100
angka_rahasia = random.randint(1, 100)

# Minta pengguna untuk menebak angka
print("Selamat datang di permainan tebak-tebakan angka!")
print("Saya telah memilih sebuah angka antara 1 dan 100.")
tebakan = None
jumlah_tebakan = 0

while tebakan != angka_rahasia:
    try:
        tebakan = int(input("Tebak angka: "))
        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("Angka terlalu kecil. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar. Coba lagi.")
        else:
            print(
                f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {jumlah_tebakan} tebakan.")
    except:
        print("Masukkan angka yang valid.")

# Menampilkan pesan saat permainan berakhir
print("Terima kasih telah bermain!")
