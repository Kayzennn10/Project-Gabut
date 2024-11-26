print("Masukan Angka 1, 2, 3, 4")
angka = int(input("Masukan angka!"))

match angka:
    case 1:
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
    case 2:
        def get_input():
            nama = input("Masukkan nama: ")
            sistolik = int(input("Masukkan tekanan darah sistolik (mmHg): "))
            diastolik = int(input("Masukkan tekanan darah diastolik (mmHg): "))
            denyut_nadi = int(input("Masukkan denyut nadi (bpm): "))
            return nama, sistolik, diastolik, denyut_nadi

        def cek_kondisi(sistolik, diastolik, denyut_nadi):
            if sistolik > 180 or diastolik > 120:
                return "Krisis hipertensi. Segera cari bantuan medis!"
            else:
                rekomendasi = []
                
                # Cek tekanan darah
                if sistolik > 140 or diastolik > 90:
                    rekomendasi.append("Hipertensi. Konsultasikan dengan dokter.")
                elif 120 <= sistolik <= 139 or 80 <= diastolik <= 89:
                    rekomendasi.append("Prehipertensi.")
                else:
                    rekomendasi.append("Tekanan darah normal.")
                
                # Cek denyut nadi
                if denyut_nadi > 100:
                    rekomendasi.append("Denyut nadi tinggi. Periksa kondisi jantung.")
                elif denyut_nadi < 60:
                    rekomendasi.append("Denyut nadi rendah. Periksa gejala bradikardia.")
                else:
                    rekomendasi.append("Denyut nadi normal.")
                
                return " ".join(rekomendasi)

        def main():
            count = 0
            while count < 3:
                nama, sistolik, diastolik, denyut_nadi = get_input()
                hasil = cek_kondisi(sistolik, diastolik, denyut_nadi)
                print(f"\nHasil untuk {nama}:")
                print(hasil)
                count += 1
                if count < 3:
                    print("\nMasukkan data untuk pasien berikutnya.")

        if __name__ == "__main__":
            main()
    case 3:
        print("Masih kosong")
    case _:
        print("Masukan angka yang valid")
