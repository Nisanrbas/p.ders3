#class lar referans tiptedir.objelere karşılık gelir.a
#ortak kodları def icine fonksiyonların icine yazılır ve defalarca kullanılacak kodu direk yazarız.ve düzeltebiliriz

class Banka:

    def krediBasvuru(self):
        print("Merhaba")
    def krediHesapla(self):
        print("Hesaplar yapıldı")

banka=Banka()

banka.krediBasvuru()

#bunları ortak bbir class ta toplayabiliriz