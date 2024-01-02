nama_nama_buah = ["apple", "banana", "cherry"]
print(nama_nama_buah)

# Tambah data ke list nama_nama_buah
# Otomatis akan jadi urutan yang terakhir
nama_nama_buah.append("orange")
print(nama_nama_buah)

# Print nama buah index ke-3
print(nama_nama_buah[2])

# Tambah 2 buah baru ke list
nama_nama_buah.extend(["strawberry", "grape"])
print(nama_nama_buah)

# Dia boleh duplikat
nama_nama_buah.append("orange")
print(nama_nama_buah)

# Dia boleh berubah
nama_nama_buah[1] = "pisang"
print(nama_nama_buah)
