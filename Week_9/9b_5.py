from collections import namedtuple

Cuaca = namedtuple("Cuaca", ["tanggal", "suhu", "kondisi"])

senin=Cuaca("2025-04-21", 30, "Cerah")
selasa=Cuaca("2025-04-22", 28, "Berawan")
rabu=Cuaca("2025-04-23", 26, "Hujan Ringan")

print("Laporan Cuaca Harian:\n")

print("pada hari senin tanggal",senin.tanggal,"memiliki suhu sekitar",senin[1],"dengan kondisi cuaca",getattr(senin, "kondisi"))

