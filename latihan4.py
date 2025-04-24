# List Di Python
# List itu kayak wadah untuk menyimpan banyak item, misalnya angka, string, atau campuran. Elemen di dalam list bisa diubah, dihapus, atau ditambah.

buah = ["apel", "pisang", "jeruk"]
print(buah)               # ['apel', 'pisang', 'jeruk']
print(buah[0])            # apel


#  operasi dasar list
buah.append("mangga")   # ['apel', 'pisang', 'jeruk', 'mangga'] tambah ke akhir
buah.insert(1, "semangka")  # ['apel', 'semangka', 'pisang', 'jeruk', 'mangga'] sisip di indeks 1
buah.remove("pisang")  # ['apel', 'semangka', 'jeruk', 'mangga'] hapus nilai
buah.pop()  # ['apel', 'semangka', 'jeruk'] hapus nilai terakhir
buah.sort()  # ['apel', 'jeruk', 'semangka'] urutkan
buah.reverse()  # ['semangka', 'jeruk', 'apel'] balik urutan

for item in buah:
    print(item)

print("todo list")
tugas = []
# todo = input("Masukkan tugas: ")
# while todo != "stop":
#     tugas.append(todo)
#     todo = input("Masukkan tugas: ")
while True:
    todo = input("Masukkan tugas: ")
    if todo == "stop":
        break
    tugas.append(todo)

print("\ndaftar tugas anda:")
for item in tugas:
    print(f"- {item}")