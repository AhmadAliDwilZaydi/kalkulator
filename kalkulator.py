# Latihan memilih perubahan dengan staging
# kalkulator.py - Kalkulator sederhana
from utilitas import format_hasil, pangkat


def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: pembagian dengan nol"
    return a / b

def maksimum(a, b):
    if a > b:
        return a
    return b

if __name__ == "__main__":
    print("Kalkulator Empat Operasi")
    print(format_hasil("+", 2, 3, tambah(2, 3)))
    # Menampilkan contoh hasil penjumlahan
    print(format_hasil("-", 7, 4, kurang(7, 4)))
    # menampilkan contoh hasil pengurangan
    print(format_hasil("x", 6, 7, kali(6, 7)))
    # menampilkan contoh hasil perkalian
    print(format_hasil(":", 8, 2, bagi(8, 2)))
    # menampilkan contoh hasil pembagian
    print("Maksimum dari 10 dan 7 =", maksimum(10, 7))
    print(format_hasil("^", 2, 10, pangkat(2, 10)))
