def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Bir sayıyı sıfıra bölemezsiniz."

while True:
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    secim = input("Seçiminizi yapın (1/2/3/4/5): ")

    if secim == '5':
        print("Çıkılıyor...")
        break

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == '1':
        print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))
    elif secim == '2':
        print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))
    elif secim == '3':
        print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))
    elif secim == '4':
        print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
    else:
        print("Geçersiz giriş. Lütfen geçerli bir seçenek girin.")
