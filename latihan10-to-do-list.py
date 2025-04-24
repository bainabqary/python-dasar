def tampilkan_menu():
    print("\n*** Menu To-Do List ***")
    print("1. Tambahkan tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Keluar dan simpan")
    pilihan = input("Pilih menu: ")
    return pilihan
    
def tampilkan_tugas(tugas):
    if not tugas:
        print("Belum ada tugas")
    else:
        print("\nDaftar tugas:")
        for i, t in enumerate(tugas, 1):
            print(f"{i}. {t}")

def simpan_tugas(tugas):
    with open("to-do-list.txt", "w") as file:
        for t in tugas:
            file.write(f"{t}\n")
    print("Tugas berhasil disimpan ke 'to-do-list.txt'.")

tugas = []

while True:
    pilihan = tampilkan_menu()
    
    if pilihan == "1":
        nama_tugas = input("Masukkan nama tugas: ")
        tugas.append(nama_tugas)
        print("Tugas berhasil ditambahkan!")
    elif pilihan == "2":
        tampilkan_tugas(tugas)
    elif pilihan == "3":
        tampilkan_tugas(tugas)
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(tugas):
                tugas.pop(nomor - 1)
                print("Tugas berhasil dihapus!")
            else:
                print("Nomor tugas tidak valid!")
        except ValueError:
            print("Masukkan angka yang benar!")
    elif pilihan == "4":
        simpan_tugas(tugas)
        print("Program selesai. Tugas telah disimpan.")
        break
    else:
        print("Pilihan tidak valid!")
        