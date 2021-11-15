class mahasiswa:
    kampus = 'UNTAN'
    jurusan = 'Rekayasa Sistem Komputer'

joko = mahasiswa()
print(joko.kampus)
print(joko.jurusan)

class karyawan:
    nama = "Joko Udin"
    jabatan = "Manager"
    gaji = "Rp.4.500.000"
    lama_berkerja = "2 Tahun"

joko = karyawan()
print(joko.nama)
print(joko.jabatan)
print(joko.gaji)
print(joko.lama_berkerja)

class Mahasiswa:
    #Kelas ini digunakan untuk mendefinisikan mahasiswa
    kampus = 'UNTAN'
    jurusan = 'Rekayasa Sistem Komputer'

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilan_profil(self):
        print("\n")
        print("Nama     :", self.nama)
        print("NIM      :", self.nim)
        print("Kampus   :", Mahasiswa.kampus)
        print("Jurusan  :", Mahasiswa.jurusan)

def main():
    mhs1 = Mahasiswa('Udin','H12345')
    mhs1.tampilan_profil()

    mhs2 = Mahasiswa('Joko','H12567')
    mhs2.tampilan_profil()

if __name__ =="__main__":
    main()

class hasildata:
    hasil = 'Hasil datanya adalah'

    def __init__(self, nama, asal, usia, pekerjaan):
        self.nama = nama
        self.asal = asal
        self.usia = usia
        self.pekerjaan = pekerjaan

    def tampilan_data(self):
        print("\n")
        print("Berikut adalah data uang didapat dari", self.nama,",", hasildata.hasil)
        print("Nama      :", self.nama)
        print("Asal      :", self.asal)
        print("Usia      :", self.usia)
        print("Pekerjaan :", self.pekerjaan)

def main():
    org1 = hasildata("Udin", "Bengkayang", "27", "Buruh")
    org1.tampilan_data()

    org2 = hasildata("Jamal", "Pontianak", "30", "Mahasiswa")
    org2.tampilan_data()

if __name__=="__main__":
    main()
