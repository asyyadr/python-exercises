# Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyetini 
#   alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az
#   18 ve eğitim durumu lise ya da üniversite olmalıdır.

name = input('İsim: ')
age = int(input('Yaş: '))
education = input('Eğitim durumu: ')


if (age >= 18) and ((education == 'lise') or (education == 'üniversite')):
    print(f'{name}, Ehliyet alabilirsiniz.')
elif (age < 18):
    if ((education == 'lise') or (education == 'üniversite')) is True:
        print(f'{name}, Yaşınız ehliyet almaya uygun değildir.')
    else:
        print(f'{name}, Yaşınız ve eğitim durumunuz ehliyet almaya uygun değildir.')
elif ((education == 'lise') and (education == 'üniversite')) is False:
    print(f'{name}, Eğitim durumunuz ehliyet almaya uygun değildir.')

# Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya
#  göre not aralığına karşılık gelen not bilgisini yazdırınız.
#  0-24   => 0
#  25-44  => 1
#  45-54  => 2
#  55-69  => 3
#  70-84  => 4
#  85-100 => 5

a = float(input('1. Not: '))
b = float(input('2. Not: '))
c = float(input('3. Not: '))
ort = ((a+b+c)/3)
if ort <= 24:
    print('Not bilgisi => 0')
elif ort <= 44:
    print('Not bilgisi => 1')
elif ort <= 54:
    print('Not bilgisi => 2')
elif ort <= 69:
    print('Not bilgisi => 3')
elif ort <= 84:
    print('Not bilgisi => 4')
elif ort <= 100:
    print('Not bilgisi => 5')
else:
    print('Yanlış bilgi girdiniz.')

# Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki
#  bilgilere göre hesaplayınız.
#  1. Bakım => 1. yıl
#  2. Bakım => 2. yıl
#  3. Bakım => 3. yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı
#  hesaplayınız.
# *** datetime modülünü kullanmanız gerekiyor.
import datetime

tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2:
    print('2. servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3. servis aralığı')
else:
    print('hatalı süre bilgisi.')
