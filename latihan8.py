try:
    angka = int(input("Masukkan angka: "))

    kali10 = angka * 10
    print("Angka kamu: ", angka)
    print("Angka kamu dikali 10: ", kali10)
except ValueError:
    print("Input harus angka!")

# try:
#     with open("latihan8.txt", "r") as file:
#         isi = file.read()
#         print(isi)
# except FileNotFoundError:
#     print("File tidak ditemukan")
