from mahasiswa import Mahasiswa

class ManajemenMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Mahasiswa {mahasiswa} berhasil ditambahkan")
        
    def tampil_mahasiswa(self):
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa")
        else:
            print("Daftar Mahasiswa:")
            for mhs in self.daftar_mahasiswa:
                mhs.tampilkan_data()
    def cari_mahasiswa(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                print("berikut data mahasiswa yang anda cari")
                return mhs.tampilkan_data()
        return print(f"Mahasiswa dengan NIM {nim} tidak ditemukan")

    def update_mahasiswa(self, nim, nama=None, jurusan=None):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                if nama:
                    mhs.nama = nama
                if jurusan:
                    mhs.jurusan = jurusan
                print(f"Data mahasiswa dengan nim {nim} berhasil diupdate")
                return
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan")

    def hapus_mahasiswa(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                self.daftar_mahasiswa.remove(mhs)
                print(f"Mahasiswa dengan nama {mhs.nama} berhasil dihapus")
                return
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan")