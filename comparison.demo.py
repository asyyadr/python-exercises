# Girilen 2 sayıdan hangisi büyüktür?
a = int(input('Number 1: '))
b = int(input('Number 2: '))

if (a > b):
    print(f"{a} is greater than {b}")
if (a < b):
    print(f"{b} is greater than {a}")
if (a == b):
    print(f"{a} is equal to {b}")

# Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın
x = float(input('Vize 1: '))
y = float(input('Vize 2: '))
z = float(input('Final: '))
result1 = (((x+y)/2)*(60/100)) + (z*(40/100))
if result1 >= 50:
    print('GEÇTİ')
else:
    print('KALDI')

# Girilen bir sayının tek mi çift mi olduğunu yazdırın
number = int(input('Number: '))
if (number % 2 == 0):
    print(f"{number} çifttir.")
else:
    print(f"{number} tektir.")

# Girilen bir sayının negatif pozitif durumunu yazdırın
number1 = float(input("Number: "))
if (number1 > 0):
    print(f"{number1} is positive")
elif (number1 == 0):
    print(f"{number1} is neutral")
else:
    print(f"{number1} is negative")

# Parola ve email bilgisini isteyip doğruluğunu kontrol edin
#   (email: email@asyaduru.com parola: abc1230)
mail = input('E-mail: ')
password = input('Password: ')
if (mail == 'email@asyaduru.com' and password == 'abc1230'):
    print('Signing in, please wait...')
else:
    print('Wrong e-mail or password, please try again.')
