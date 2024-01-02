import requests
import json

# URL tujuan
url = 'https://jsonplaceholder.typicode.com/posts'

# Data yang akan dikirim
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Header dengan tipe konten JSON
headers = {
    'Content-type': 'application/json; charset=UTF-8'
}

# Melakukan permintaan POST dengan data JSON
response = requests.post(url, data=json.dumps(data), headers=headers)

# Mengecek apakah permintaan berhasil (kode status 201 berarti berhasil)
if response.status_code == 201:
    response_json = response.json()
    print('Respon:', response_json)
else:
    print('Permintaan POST tidak berhasil. Kode status:', response.status_code)
