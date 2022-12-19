from abc import ABCMeta, abstractmethod

class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass

class BiayaUtama(Item):
    def __init__(self, contents):
        self.contents = contents
    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price

class UangPendaftaran(Item):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.return_price

class UangKuliahPertama(Item):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.return_price

class UangTraining(Item):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.return_price

class UangPenginapan(Item):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.return_price

class UangKonsumsi(Item):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.return_price

if __name__ == '__main__':
    biaya = []
    biaya.append(UangPendaftaran(200000))
    biaya.append(UangKuliahPertama(1500000))

    biaya_utama = BiayaUtama(biaya)

    biaya_mpt = []
    biaya_mpt.append(UangTraining(100000))
    biaya_mpt.append(UangPenginapan(200000))
    biaya_mpt.append(UangKonsumsi(150000))

    biaya_total = []
    biaya_total.append(biaya_utama)
    biaya_total.append(biaya_mpt)
    biaya_utama = BiayaUtama(biaya_total)

    print('Total price : ' + str(biaya_utama.return_price()))




