def pembagian(angka_1:int,angka_2:int):
    try:
        hasil = angka_1/angka_2
        return hasil
    except ZeroDivisionError:
        return "tidak bisa dibagi 0"

angka_1 = int(input("masukkan angka pertama : "))
angka_2 = int(input("masukkan angka ke-2 : "))
print(pembagian(angka_1,angka_2))

