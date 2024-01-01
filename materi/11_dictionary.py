nama_mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(nama_mobil)

# Akses dengan nama key-nya
print(nama_mobil["brand"])

# Bisa juga menggunakan .get()
print(nama_mobil.get("model"))

# Tidak boleh duplikat
# Karena akan diambil nilai yang terbaru
nama_mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(nama_mobil)

# Mengetahui panjang dictionary
print(len(nama_mobil))

# Kita bisa mendapatkan key dari sebuah dictionary
x = nama_mobil.keys()
print(x)

# Bisa juga menambahkan data key-value pair baru
nama_mobil["color"] = "white"
print(nama_mobil)

# Kita juga bisa mendapatkan value dari sebuah dictionary
y = nama_mobil.values()
print(y)

# Bisa juga menghapus key misalnya year
nama_mobil.pop("year")
print(nama_mobil)
