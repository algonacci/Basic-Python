def prediksi_cuaca(temperatur, kelembaban):
    if temperatur > 25 and kelembaban > 80:
        return "Hujan"
    elif temperatur > 25 and kelembaban <= 80:
        return "Cerah"
    elif temperatur <= 25 and kelembaban > 80:
        return "Berawan"
    else:
        return "Berawan dengan sedikit hujan"


temperatur = int(input("Masukkan temperatur hari ini: "))
kelembaban = int(input("Masukkan kelembaban hari ini: "))
hasil_prediksi = prediksi_cuaca(temperatur, kelembaban)

print(f"Cuaca hari ini diprediksi: {hasil_prediksi}")
