temperatur = int(input("Masukkan temperatur hari ini: "))
kelembaban = int(input("Masukkan kelembaban hari ini: "))

# Prediksi cuaca berdasarkan input pengguna
if temperatur > 25 and kelembaban > 80:
    prediksi = "Hujan"
elif temperatur > 25 and kelembaban <= 80:
    prediksi = "Cerah"
elif temperatur <= 25 and kelembaban > 80:
    prediksi = "Berawan"
else:
    prediksi = "Berawan dengan sedikit hujan"

print(f"Cuaca hari ini diprediksi: {prediksi}")
