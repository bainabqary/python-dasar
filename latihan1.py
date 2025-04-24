nama = "Bain"
umur = 27
tinggi = 1.74
berat = 73

# bmi = berat / (tinggi / 100) ** 2
bmi = berat / (tinggi ** 2)


print("Nama saya adalah", nama)
print("Umur saya adalah", umur)
print("Tinggi saya adalah", tinggi)
print("Berat saya adalah", berat)
print(f"BMI saya adalah {bmi:.2f}")