# Membuka file untuk dibaca
with open('data/data_penting.txt', 'r') as file:
    isi_file = file.read()

print(isi_file)


# Error handling
# try:
#     with open('file_tidak_ada.txt', 'r') as file:
#         isi_file = file.read()
# except FileNotFoundError:
#     print('File tidak ditemukan.')
