# percabangan
# check umur
umur = 27
if umur >= 18:
    print("Anda telah cukup umur")
else:
    print("Anda belum cukup umur")

# check nilai
nilai = 85
if nilai >= 90:
    print("nilai A")
elif nilai >= 80:
    print("nilai B")
elif nilai >= 70:
    print("nilai C")
else:
    print("nilai D")

# check bmi
tinggi = 1.74
berat = 71
bmi = berat / (tinggi ** 2)
if bmi < 18.5:
    kategori = "Kurus"
elif bmi < 25:
    kategori = "Normal"
elif bmi < 30:
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print(f"BMI Anda adalah {bmi:.2f} dan kategori {kategori}")
