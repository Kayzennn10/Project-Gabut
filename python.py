nama = (input("Masukan Nama Kamu!"))
suhu_tubuh = int(input("isi suhu tubuh kamu!"))
detak_jantung = int(input("isi detak jantung kamu!"))

if suhu_tubuh > 37.5:
 if suhu_tubuh > 39 and suhu_tubuh < 50:
    print("harus segera dirawat!")
 else:
    print("cukup istirahat saja!")
else:
  if detak_jantung < 100:
    print("detak jantung terlalu tinggi, butuh pemeriksaan lebih lanjut.")
  else:
    print("detak jantung normal, perbanyak istirahat dan minum cairan.")
print(f"nama {nama} \nsuhu {suhu_tubuh} \ndetak_jantung {detak_jantung}")   