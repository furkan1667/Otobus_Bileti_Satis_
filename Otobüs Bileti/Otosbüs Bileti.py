import time


class Yolcu():
    def __init__(self, adi, soyadi, cinsiyeti):
        self.adi = adi
        self.soyadi = soyadi
        self.cinsiyeti = cinsiyeti

    def get_adi(self):
        return self.adi

    def get_soyadi(self):
        return self.soyadi

    def get_cinsiyeti(self):
        return self.cinsiyeti

    def set_adi(self, adi):
        self.adi = adi

    def set_soyadi(self, soyadi):
        self.soyadi = soyadi

    def set_cinsiyeti(self, cinsiyeti):
        self.cinsiyeti = cinsiyeti

    def get_yolcu(self):
        return "{} {}, {}".format(self.adi, self.soyadi, self.cinsiyeti)


a = Yolcu(None, None, None)


class Koltuklar():

    def __init__(self, koltukNo=None, koltukDurum=False, yolcu=None):
        self.koltukNo = koltukNo
        self.koltukDurum = koltukDurum
        self.yolcu = yolcu

    def get_koltukNo(self):
        return self.koltukNo

    def get_koltukDurum(self):
        return self.koltukDurum

    def get_yolcu(self):
        return self.yolcu

    def set_koltukNo(self, koltukNo):
        self.koltukNo = koltukNo

    def set_koltukDurum(self, koltukDurum):
        self.koltukDurum = koltukDurum

    def set_yolcu(self, yolcu):
        self.yolcu = yolcu


d = Koltuklar()


class Otobus():




    def __init__(self, plaka, koltukRezerv, koltukSayısı=42):
        self.koltukSayısı = koltukSayısı
        self.plaka = plaka
        self.koltukRezerv = koltukRezerv


def get_koltukSayısı(self):
    return self.koltuksayısı


def get_plaka(self):
    return self.plaka


def set_koltukSayısı(self, koltukSayısı):
    self.koltukSayısı = koltukSayısı


def set_plaka(self, plaka):
    self.plaka = "28 GRU 454"


def koltukRezerv(self):
    return a.get_yolcu()


c = Otobus(2, 3)


def main():
    koltuklar = ["ŞOFÖR", ]
    for i in range(0, 42):
        koltuklar.append(d.get_koltukNo())

    while 1 == 1:
        try:

            print("""
    ====================================

                 MENÜ

    1- Rezervasyon yap
    2- Bütün yolcuları görüntüle
    3- Bütün koltukları görüntüle
    4- Bütün boş koltukları görüntüle
    5- Çıkış

    ====================================            
    """)
            try:
                kullanıcı = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz: "))
            except:
                print("Lütfen Sadece Sayı Giriniz....")
                continue

            if (
                    kullanıcı > 5 or kullanıcı == 0):
                print("UYARI !!!")
                time.sleep(1)
                print("Lütfen Verilen Seçeneklerden Birisini Seçiniz...")
                continue

            if (kullanıcı == 1):
                print("""

            ------------------------------------------------------------
            |             1  5  9    13  17       23  27  31  35  39   |
            |                                                          |
            |             2  6  10   14  18       24  28  32  36  40   |
            |                                                          |
            |                                                          |
            |                                                          | 
            |             3  7  11   15  19   21  25  29  33  37  41   |
            |   (\__/)                                                 |   
            |   (•  •)    4  8  12   16  20   22  26  30  34  38  42   |   
            |  < 　  /                                                 |  
            ------------------------------------------------------------



            """)

                b = int(input("Lütfen istediğiniz Koltuk Numarasını Giriniz: "))

                try:
                    assert (b > 42)
                    print("UYARI !!!!")
                    time.sleep(1)
                    print("Otobüs 42 Koltuktan Oluşmaktadır")
                    continue
                except:

                    if koltuklar[b] == None:
                        a.set_adi(input("Yolcunun Adı: "))
                        a.set_soyadi(input("Yolcunun Soyadı: "))
                        a.set_cinsiyeti(input("Yolcunun Cinsiyeti (E/K): "))
                        print("Yolcu Bilgileri Doğrulanılıyor....")
                        time.sleep(1)
                        print("Yolcu Kaydedildi....")
                        time.sleep(1)
                        print("""
                    *******************************************************
                                        BİLGİLENDİRME
                        SAYIN YOLCULARIMIZ OTOBÜS PLAKASI 28 GRU 454'tür..
                                   İYİ YOLCULUKLAR DİLERİZ...
                    *******************************************************
                    """)









                    else:
                        print("UYARI !!!!")
                        time.sleep(1)  # koltuk dolu ise verilecek çıktı
                        print("İstediğin Koltuk Daha Önceden Rezerve Edilmiştir...")

            koltuklar[b] = a.get_yolcu()

            if (kullanıcı == 2):  # kullanıcı 2 girer ise aşağıda ki işlemler izlenir

                v = 0
                for o in koltuklar:
                    if o != None:
                        print(str(v + 1), "-", o)  # for döngüsü ile yolcu sayısını öğreniyoruz
                        v = v + 1

                    else:
                        pass

            elif (kullanıcı == 3):  # kullanıcı 3 girer ise aşağıda ki işlemler izlenir
                u = 0
                for u in range(0, 43):
                    print(str(u), "-", koltuklar[u])  # hangi yolcunun hangi koltukta oturduğunu gösterir
                    u = u + 1

            elif (kullanıcı == 4):  # kullanıcı 4 girer ise aşağıda ki işlemler izlenir
                Ü = -1
                for o in koltuklar:
                    Ü = Ü + 1
                    if o == None:
                        print(o)  # Boş koltukları dolana kadar none olarak gösterir

                    else:
                        print((Ü), "-", "DOLU")

                        continue





            elif (kullanıcı == 5):  # kullanıcı 5 girer ise aşağıda ki işlemler izlenir
                print("Programdan Çıkış Yapılıyor.....")
                time.sleep(1)
                print("Program Sonlandırıldı...")  # 5 girer ise programdan çıkmış olur
                break

        except:
            print("Lütfen İlk Önce Rezervasyon Yapınız...")


main()
