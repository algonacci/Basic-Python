temperatur = 28
kelembaban = 85

# Prediksi cuaca
if temperatur > 25 and kelembaban > 80:
    prediksi = "Hujan"
elif temperatur > 25 and kelembaban <= 80:
    prediksi = "Cerah"
elif temperatur <= 25 and kelembaban > 80:
    prediksi = "Berawan"
else:
    prediksi = "Berawan dengan sedikit hujan"

print(f"Cuaca hari ini diprediksi: {prediksi}")
