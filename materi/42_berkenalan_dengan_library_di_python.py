import requests

# URL situs web yang ingin diambil
url = 'https://jsonplaceholder.typicode.com/users'

# Melakukan permintaan GET ke URL
response = requests.get(url)

# Mengecek apakah permintaan berhasil (kode status 200 berarti berhasil)
if response.status_code == 200:
    print('Konten situs web:', response.text)
else:
    print('Permintaan tidak berhasil. Kode status:', response.status_code)
