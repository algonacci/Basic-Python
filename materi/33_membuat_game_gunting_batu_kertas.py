import random

# Pilihan yang tersedia
pilihan = ["gunting", "batu", "kertas"]

# Menghasilkan pilihan acak untuk komputer
pilihan_komputer = random.choice(pilihan)

# Minta pemain untuk memilih
print("Selamat datang di permainan Gunting-Batu-Kertas!")
print("Pilihan Anda: gunting, batu, atau kertas.")
pilihan_pemain = input("Pilihan Anda: ").lower()

# Validasi pilihan pemain
if pilihan_pemain not in pilihan:
    print("Pilihan tidak valid. Harap pilih gunting, batu, atau kertas.")
else:
    print(f"Pilihan Anda: {pilihan_pemain}")
    print(f"Pilihan Komputer: {pilihan_komputer}")

    # Menentukan pemenang
    if pilihan_pemain == pilihan_komputer:
        print("Hasil: Seri!")
    elif (
        (pilihan_pemain == "gunting" and pilihan_komputer == "kertas")
        or (pilihan_pemain == "batu" and pilihan_komputer == "gunting")
        or (pilihan_pemain == "kertas" and pilihan_komputer == "batu")
    ):
        print("Anda Menang!")
    else:
        print("Komputer Menang!")

# Menampilkan pesan saat permainan berakhir
print("Terima kasih telah bermain!")
