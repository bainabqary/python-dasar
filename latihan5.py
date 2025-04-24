# dictionary
# dictionary isi nya key dan value

orang = {
    "nama": "Bain",
    "umur": 27,
    "tinggi": 1.74,
    "berat": 73
}

print(orang["nama"])
print(orang["umur"])
print(orang["tinggi"])
print(orang["berat"])

# menambahkan
orang["pekerjaan"] = "Programmer"

# mengganti
orang['berat'] = 71

# menghapus
del orang['tinggi']

print(orang)
for key, value in orang.items():
    print(f"{key}: {value}")

data = {}
data["nama"] = input("Masukkan nama anda: ")
data["umur"] = input("Masukkan umur anda: ")
data["tinggi"] = input("Masukkan tinggi anda: ")

print("\nIni Adalah data kamu:")
for i, n in data.items():
    print(f"{i}: {n}")
