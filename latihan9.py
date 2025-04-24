# modul dan package

import datetime
import random

sekarang = datetime.datetime.now()
print(f"sekarang adalah {sekarang.time()}")

angka = random.randint(1, 10)
input_angka = int(input("Tebak angka dari 1-10: "))
if input_angka == angka:
    print("Tebakkanmu benar!")
else:
    print(f"Tebakkanmu salah! Angka yang benar adalah {angka}")