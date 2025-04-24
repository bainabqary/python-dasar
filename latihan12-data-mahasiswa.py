import json
import csv

data_mahasiswa = {}

def tambah_mahasiswa():
    nim = input("Masukkan NIM mahasiswa: ")

    # validasi nim harus angka
    if not nim.isdigit():
        print("NIM harus angka.\n")
        return

    # validasi nim tidak boleh ada yang sama
    if nim in data_mahasiswa:
        print(f"Mahasiswa dengan NIM {nim} sudah ada.\n")
        return
    
    nama = input("Masukkan nama mahasiswa: ")
    jurusan = input("Masukkan jurusan mahasiswa: ")

    # validasi nama dan jurusan tidak boleh kosong
    if not nama or not jurusan:
        print("Nama dan jurusan tidak boleh kosong.\n")
        return

    data_mahasiswa[nim] = {"nama": nama, "jurusan": jurusan}
    print(f"Mahasiswa {nama} berhasil ditambahkan.\n")

def lihat_mahasiswa():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.\n")
    else:
        print("\nData Mahasiswa:")
        for nim, data in data_mahasiswa.items():
            print(f"NIM: {nim}, Nama: {data['nama']}, Jurusan: {data['jurusan']}")
        print()

def cari_mahasiswa():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.\n")
    else:
        nim = input("Masukkan NIM mahasiswa: ")
        if nim in data_mahasiswa:
            data = data_mahasiswa[nim]
            print(f"\nData Mahasiswa NIM {nim}:")
            print(f"Nama: {data['nama']}")
            print(f"Jurusan: {data['jurusan']}")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.\n")

def hapus_mahasiswa():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.\n")
    else:
        nim = input("Masukkan NIM mahasiswa: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print(f"Mahasiswa dengan NIM {nim} berhasil dihapus.\n")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.\n")

def simpan_mahasiswa():
    with open("data_mahasiswa.json", "w") as f:
        json.dump(data_mahasiswa, f)
        print("Data mahasiswa berhasil disimpan ke data_mahasiswa.json\n")

def muat_data():
    global data_mahasiswa
    try:
        with open("data_mahasiswa.json", "r") as f:
            data_mahasiswa = json.load(f)
            print("Data mahasiswa berhasil dimuat dari data_mahasiswa.json\n")
    except FileNotFoundError:
        data_mahasiswa = {}
        print("File data_mahasiswa.json tidak ditemukan.\n")

def export_csv():
    if not data_mahasiswa:
        print("Data mahasiswa masih kosong, tidak ada yang di export\n")
    else:
        with open("data_mahasiswa.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["NIM", "Nama", "Jurusan"])
            for nim, data in data_mahasiswa.items():
                writer.writerow([nim, data["nama"], data["jurusan"]])
            print("Data mahasiswa berhasil diexport ke data_mahasiswa.csv\n")

def menu():
    muat_data()
    while True:
        print("== Menu Data Mahasiswa ==")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Export Data Mahasiswa")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            lihat_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            export_csv()
        elif pilihan == "6":
            simpan_mahasiswa()
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan (1-6).\n")

menu()