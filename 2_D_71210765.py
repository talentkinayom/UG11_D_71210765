kalimat = input("Masukkan sebuah kata/kalimat :")
karakter = input("Masukkan karakter yang ingin disisipkan :")

def sisipHuruf():
    a = kalimat.upper()
    print(karakter.join(list(a)))

def sisipKata():
    b = kalimat.title()
    print(karakter.join(b.split()))

sisipHuruf()
sisipKata()