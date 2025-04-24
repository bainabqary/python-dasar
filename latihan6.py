# function (fungsi)

# def hitung_bmi(berat, tinggi):
#     bmi = berat / (tinggi ** 2)

#     if bmi < 18.5:
#         kategori = "Kurus"
#     elif bmi < 25:
#         kategori = "Normal"
#     elif bmi < 30:
#         kategori = "Gemuk"
#     else:
#         kategori = "Obesitas"
    # print(f"BMI kamu: {bmi:.2f}")
    # print(f"Kategori: {kategori}")

def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        kategori = "Kurus"
    elif bmi < 25:
        kategori = "Normal"
    elif bmi < 30:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    return kategori

data = {}
data["berat"] = int(input("Masukkan berat anda: "))
data["tinggi"] = float(input("Masukkan tinggi anda: "))
bmi_saya = hitung_bmi(data["berat"], data["tinggi"])
kategori_bmi_saya = kategori_bmi(bmi_saya)

print(f"BMI kamu: {bmi_saya:.2f}")
print(f"Kategori: {kategori_bmi_saya}")