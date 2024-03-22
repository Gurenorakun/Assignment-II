from datetime import datetime, timedelta

def tanggal_depan(days):
    tanggal_sekarang = datetime.now()

    tanggal_nanti = tanggal_sekarang + timedelta(days=days)

    string_tanggal_nanti = tanggal_nanti.strftime("%A, %B %d, %Y")

    print("Tanggal nanti: ", string_tanggal_nanti)

days = int(input("Input angka: "))

tanggal_depan(days)