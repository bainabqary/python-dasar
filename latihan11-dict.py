data = {
    "nama": "Bain",
    "umur": 27,
    "tinggi": 1.74
}

print(data["nama"])  # Bain

data["umur"] = 17
print(data)

mahasiswa = {
    "001": {"nama": "Bain", "jurusan": "Informatika"},
    "002": {"nama": "Bani", "jurusan": "Sistem Informasi"}
}

print(mahasiswa["001"]["jurusan"])  # Informatika