from mahasiswa import Mahasiswa
from manajemen import ManajemenMahasiswa

manajemen = ManajemenMahasiswa()

while True:
    print("\nPilih Menu di bawah ini")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Update Mahasiswa")
    print("5. Hapus Mahasiswa")
    print("6. Keluar")
    pilihan = input("Masukan Pilihan Anda: ")

    if pilihan == "1":
        nim = input("Masukan NIM:")
        nama = input("Masukan Nama: ")
        jurusan = input("Masukan Jurusan:")
        mhs = Mahasiswa(nama, nim, jurusan)
        manajemen.tambah_mahasiswa(mhs)
        print(f"Mahasiswa {nama} berhasil ditambahkan")
    elif pilihan == "2":
        manajemen.tampil_mahasiswa()
    elif pilihan == "3":
        nim = input("Masukan NIM mahasiswa yang sedang anda cari: ")
        manajemen.cari_mahasiswa(nim)
    elif pilihan == "4":
        nim = input("Masukan NIM mahasiswa yang ingin anda update: ")
        nama = input("Masukan Nama Mahasiswa yang ingin anda update: ")
        jurusan = input("Masukan Jurusan Mahasiswa yang ingin anda update: ")
        manajemen.update_mahasiswa(
            nim, 
            nama if nama else None,
            jurusan if jurusan else None
        )
    elif pilihan == "5":
        nim = input("Masukan NIM mahasiswa yang ingin anda hapus: ")
        manajemen.hapus_mahasiswa(nim)
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program ini")
        break
    else:
        print("Pilihan Tidak Tersedia")