# cities=["Ankara","istanbul","İzmir"]

# for city in cities:
#     print(city)
# for sayi in range(10):#range sınırı belirler kadar dahil değildir
#     print(sayi)

# for sayi in range(0,10,2):#range sınırı belirler kadar dahil değildir 0 başlangıc 10 nereye adar 2 arttırma sayısı
#     print(sayi)

# sayac=1
# while sayac<=10:
#     print(sayac)
#     sayac=sayac+1




sayi=int(input("sayı giriniz: ")) 
faktoriyel=1
for sayi1 in range(2,sayi+1):
    faktoriyel=sayi1*faktoriyel
   
print(faktoriyel)
