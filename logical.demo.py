# Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
a = float(input('Sayı: '))
result1 = a > 0 and a < 100
if result1 is True:
    print('Sayı 0-100 arasındadır.')
else:
    print('Sayı 0-100 arasında değildir.')

# Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
b = float(input('Sayı: '))
result2 = b > 0 and (b % 2 == 0)
if result2 is True:
    print(f'{b} pozitif ve çift bir sayıdır.')
else:
    print(f'{b} pozitif ve çift bir sayı değildir.')
#////////////////////////////
d = float(input('Sayı: '))
pozitif = (d > 0)
cift = (d % 2 == 0)
if pozitif and cift:
    print(f"{d} hem pozitif hem çift bir sayıdır.")
elif pozitif:
    print(f"{d} yalnızca pozitif bir sayıdır.")
elif cift:
    print(f"{d} yalnızca çift bir sayıdır.")
else:
    print(f"{d} ne pozitif ne de çift bir sayıdır.")

# Email ve parola bilgileri ile giriş kontrolü yapınız.
orgmail = 'batman@gmail.com'
orgpassword = 'abc123'

email = input('Email: ')
password = input('Password: ')

if (email == orgmail) and (password == orgpassword):
    print('Signing in..')
else:
    print('Wrong email or password!')

# Girilen 3 sayıyı büyüklük olarak  karşılaştırınız.
sayilar = []
sayi1 = float(input('1. Sayı: '))
sayi3 = float(input('2. Sayı: '))
sayi2 = float(input('3. Sayı: '))
sayilar.extend([sayi1, sayi2, sayi3])
sayilar.sort(reverse=True)
siralama = str(sayilar).replace(',', '>')
print(siralama)

# Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#  Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
#  a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#  b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input('1. Vize: '))
vize2 = float(input('2. Vize: '))
final = float(input('Final: '))
ortalama = ((((vize1 + vize2)/ 2)*6/10)+(final*4/10))
if (ortalama >= 50) and (final >= 50):
    print('GEÇTİ.')
elif (final >= 70):
    print('GEÇTİ.')
else:
    print('KALDI.')

# Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül: (Kilo/ boy uzunluğunun karesi)
#   0-18.4    => Zayıf
#   18.5-24.9 => Normal
#   25.0-29.9 => Fazla Kilolu
#   30.0-34.9 => Şişman (Obez)

ad = input('Kişinin adı: ')
kilo = float(input('Kişinin kilosu: '))
boy = float(input('Kişinin boyu: '))
indeks = (kilo/boy**2)
if (indeks >= 0) and (indeks<= 18.4):
    print(f"{ad} zayıftır.")
elif (indeks <= 24.9):
    print(f"{ad} normal kilodadır.")
elif (indeks <= 29.9):
    print(f"{ad} fazla kiloludur.")
elif (indeks <= 34.9):
    print(f"{ad} şişmandır (obez).")
else:
    print('Hesaplanamadı. Bilgileri tekrar kontrol ediniz.')
