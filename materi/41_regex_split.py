import re

text = "Halo, nama saya John. Saya berumur 25 tahun."

# Membagi string berdasarkan spasi
potongan = re.split(r'\s', text)
print(potongan)
