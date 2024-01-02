import smtplib

# Konfigurasi SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sociopath.xyz@gmail.com'
smtp_password = ''

# Baca daftar email dari file
with open('data/data_email.txt', 'r') as file:
    email_list = file.read().splitlines()

# Membuat pesan email
subject = 'Contoh Subject Email'
message_body = 'Ini adalah isi pesan email.'

# Inisialisasi koneksi SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Mengirim pesan ke setiap email dalam daftar
    for email_address in email_list:
        msg = f'Subject: {subject}\n\n{message_body}'
        server.sendmail(smtp_username, email_address, msg)

    # Menutup koneksi SMTP
    server.quit()

    print('Pesan email berhasil terkirim ke semua alamat dalam file.')
except Exception as e:
    print('Terjadi kesalahan saat mengirim email:', str(e))
