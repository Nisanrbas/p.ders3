products=["Mouse","Laptop","Keyboard"]
print(products)
print(type(products))
products.append("Telefon")
print(products)


students1=["Engin","Cavit","Berkay"]  #referans tip tir : list,diziler,class heapta gercekleşir
students2=["Kerem","Halil","Nisa"]

students1=students2
students2[0]="Ayse"
print(students1)
print(students2)


sayi1=10                            #değer tip: sayısal veri tipleri değer tipidir. Boolen ,int, float
sayi2=20                              #iki değerde bellekte farklı tutulduğu için sonuç böyle cıkmıştır.stacta gercekleşir
sayi1=sayi2
sayi2=60
print(sayi1)

isim="Engin"
print(isim[0])