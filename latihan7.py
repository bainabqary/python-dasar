# Bekerja dengan file (input output)

with open("latihan7.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Bain\n")

with open("latihan7.txt", "a") as file:
    file.write("\nIni adalah baris baru dari append")

with open("latihan7.txt", "r") as file:
    isi = file.read()
    print("isi file: ")
    print(isi)

with open("latihan7-kegiatan.txt", "w") as file:
    while True:
        kegiatan = input("Masukkan kegiatan anda: ")
        if kegiatan.lower() == "stop":
            break
        file.write(kegiatan + "\n")

print("\nKegiatan anda:")
with open("latihan7-kegiatan.txt", "r") as file:
    isi = file.read()
    print(isi)