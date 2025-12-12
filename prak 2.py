# ==============================
# Program Gabungan: Operator, Kondisi, dan Perulangan
# ==============================

def operator_aritmatika():
    print("\n=== OPERASI ARITMATIKA ===")
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua  : "))

    print("\nHasil Operasi:")
    print(f"Penjumlahan: {a} + {b} = {a + b}")
    print(f"Pengurangan: {a} - {b} = {a - b}")
    print(f"Perkalian  : {a} * {b} = {a * b}")
    print(f"Pembagian  : {a} / {b} = {a / b}")
    print(f"Modulus    : {a} % {b} = {a % b}")

def kondisi_genap_ganjil():
    print("\n=== KONDISI GENAP / GANJIL ===")
    bil = int(input("Masukkan sebuah bilangan: "))
    if bil % 2 == 0:
        print(f"{bil} adalah bilangan GENAP.")
    else:
        print(f"{bil} adalah bilangan GANJIL.")

def perulangan_deret():
    print("\n=== PERULANGAN DERET BILANGAN ===")
    n = int(input("Masukkan nilai N: "))
    print("Deret bilangan dari 1 sampai", n, ":")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()  # baris baru

# ==============================
# MENU UTAMA
# ==============================
while True:
    print("\n==============================")
    print("PROGRAM OPERATOR, KONDISI, PERULANGAN")
    print("==============================")
    print("1. Operator Aritmatika")
    print("2. Kondisi (Genap/Ganjil)")
    print("3. Perulangan (Deret Bilangan)")
    print("4. Keluar")
    print("==============================")

    pilih = input("Pilih menu [1-4]: ")

    if pilih == "1":
        operator_aritmatika()
    elif pilih == "2":
        kondisi_genap_ganjil()
    elif pilih == "3":
        perulangan_deret()
    elif pilih == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
