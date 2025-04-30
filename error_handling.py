def bagi(a,b):
    try:
        hasil = a/b
    except ZeroDivisionError:
        return "Error: Tidak dapat membagi dengan nol"
    else:
        return f"Hasil: {hasil}"
    finally:
        print("Selesai")

print(bagi(10,2))
print(bagi(10,0))