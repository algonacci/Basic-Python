import re

text = "Halo, nama saya John. Saya berumur 25 tahun."

hasil = re.search("John", text)

if hasil:
    print("Ditemukan:", hasil.group())
else:
    print("Tidak ditemukan")
