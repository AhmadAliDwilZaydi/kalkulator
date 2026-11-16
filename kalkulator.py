# Latihan memilih perubahan dengan staging
# kalkulator.py - Kalkulator sederhana
from utilitas import format_hasil


def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

if __name__ == "__main__":
    print("Kalkulator Sederhana")
    print(format_hasil("+", 2, 3, tambah(2, 3)))
    # Menampilkan contoh hasil penjumlahan
    print(format_hasil("-", 7, 4, kurang(7, 4)))
    # menampilkan contoh hasil pengurangan
