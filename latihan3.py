# for loop
print("# for loop")
for i in range(10):
    print(f"Perulangan ke-{i}")

# input angka untuk perulangan
print("# input angka untuk perulangan")
ulangi = int(input("Berapa kali kamu mau mencetak nama: "))
for i in range(ulangi):
    print("Bain is my name")

# while loop
print("# while loop")
count = 1
while count < 10:
    print(f"Count adalah {count}")
    count += 1

# input angka untuk while loop
print("# input angka untuk while loop")
total = 0
angka = int(input("Masukkan angka (0 untuk selesai): "))
while angka != 0:
    total += angka
    angka = int(input("Masukkan angka (0 untuk selesai): "))
print(f"Total angka yang kamu masukkan adalah {total}")
