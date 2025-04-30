class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_data(self):
        print(f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}")