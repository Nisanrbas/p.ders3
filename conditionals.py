# şart blokları

istenilenKredi=10000
hesap=9505
minOlmasıGerekenHesap=10000

if hesap>=minOlmasıGerekenHesap:
  
  print("keredi verilebilir")
  print("ödemeler hesaplandı")

elif hesap>=9000 and hesap<=9500:
    print("müdüre sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("Genelmüdüre sorulacak")

else:
    print("kredi almak için bakiye yetersiz")



print("islem sonu")
