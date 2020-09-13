from enum import Enum
# Enumerasi hanya diasumsikan sebagai arrayList yang tidak bisa
# diubah. Bernilai 0,1,...,n dan tidak perlu mendeklarasi terus menerus hal yang sama
from Core.Data import ArrayData
from Utility.Array import panjangArray, elAdd, cariArray

# Program Wahana
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi yang berkaitan dengan tipe bentukan
# Attraction atau wahana. Untuk penjelasan setiap fungsinya ada di atas segmen
# setiap fungsi.

# Enumerasi Tipe Batasan Umur
class AgeRestriction(Enum):
    # Jika dipanggil, akan mengembalikan "Anak-Anak" atau "Semua Umur"
    # dipakai hanya untuk pemanggilan array final tanpa deklarasi terus menerus
    def __str__(self):
        if (str(self.name) == 'Anak'):
            return "Anak-Anak"
        if (str(self.name) == 'SemuaUmur'):
            return "Semua Umur"
        return str(self.name)

    Anak = 0
    Dewasa = 1
    SemuaUmur = 2

# Enumerasi Tipe Batasan Tinggi
class HeightRestricton(Enum):
    # Jika dipanggil, akan mengembalikan ">=170" atau "Tanpa Batasan"
    # dipakai hanya untuk pemanggilan array final tanpa deklarasi terus menerus
    def __str__(self):
        if (str(self.name) == 'Above170'):
            return ">=170"
        if (str(self.name) == 'All'):
            return "Tanpa Batasan"
        return str(self.name)
    Above170 = 0
    All = 1

# Attraction atau Wahana
# name              : string
# ticketprice       : int
# agerestriction    : string
# heightrestriction : string
class Attraction:
    def __init__(self, name, ticketprice, ager, heightr):

        self.__name = name
        self.__ticketprice = ticketprice
        if (ager.lower() == 'anak-anak'):
            self.__ager = AgeRestriction.Anak
        elif (ager.lower() == 'dewasa'):
            self.__ager = AgeRestriction.Dewasa
        elif (ager.lower() == 'semua umur'):
            self.__ager = AgeRestriction.SemuaUmur
        else:
            raise ValueError('Age Restriction should be filled with "Anak-Anak" or "Dewasa" or "Semua Umur"')

        if (heightr == '>=170'):
            self.__heightr = HeightRestricton.Above170
        elif (heightr.lower() == 'tanpa batasan'):
            self.__heightr = HeightRestricton.All
        else:
            raise ValueError('Height Restriction should be filled with ">=170" or "Tanpa Batasan"')

        # tiket yang terjual
        self.__sale = 0

    # Getter dan Setter
    # Mengembalikan suatu nilai
    # Mengubah suatu nilai
    def getName(self):
        return self.__name[0:16]
    def getAR(self):
        return self.__ager
    def getHR(self):
        return self.__heightr
    def getTicketPrice(self):
        return self.__ticketprice
    def getSale(self):
        return self.__sale

    def setName(self, newname):
        self.__name = newname
    def setTicketPrice(self, ticketprice):
        self.__ticketprice = ticketprice

    def setAgeRestriction(self, ager):
        if (ager.lower() == 'anak-anak'):
            self.ager = AgeRestriction.Anak
        elif (ager.lower() == 'dewasa'):
            self.ager = AgeRestriction.Dewasa
        elif (ager.lower() == 'semua umur'):
            self.ager = AgeRestriction.SemuaUmur
        else:
            raise ValueError('Age Restriction should be filled with "Anak-Anak" or "Dewasa" or "Semua Umur"')
    def setHeightRestriction(self, heightr):
        if (heightr == '>=170'):
            self.heightr = HeightRestricton.Above170
        elif (heightr.lower() == 'tanpa batasan'):
            self.heightr = HeightRestricton.All
        else:
            raise ValueError('Height Restriction should be filled with ">=170" or "Tanpa Batasan"')

    # Untuk menambahkan jika ada penjualan
    def newSale(self, amount):
        self.__sale += amount

class AttractionManager:
    def __init__(self, filename):
        self.__file = ArrayData(filename, ['EmptyWahana(index)', 'WahanaEmpty(index)', 999999, "Semua Umur", "Above170"])
        self.__idlist = []
        self.__attractions = []

    # Fungsi untuk mengubah array of attraction menjadi matrix
    # digunakan untuk diimplementasikan pada fungsi save
    # untuk menyimpan kembali kedalam csv
    def getAttractionsAsList(self):
        result = []
        for i in range(panjangArray(self.__idlist)):
            attr = self.__attractions[i]
            arr = [] # ini adalah array dalam satu baris
            arr = elAdd(arr, self.__idlist[i]) # penambahan elemen tiap baris
            arr = elAdd(arr, attr.getName()) # hal yang sama dengan atas
            arr = elAdd(arr, attr.getTicketPrice()) # hal yang sama dengan atas
            arr = elAdd(arr, attr.getAR()) # hal yang sama dengan atas
            arr = elAdd(arr, attr.getHR()) # hal yang sama dengan atas
            result = elAdd(result, arr) # masukkan kedalam kolom
        return result

    # Fungsi untuk mengambil semua data dari CSV dan mengaksesnya ke dalam matrix
    # Lalu matrix akan di transpos ke dalam 2 array
    # Satu array berisi semua id wahana
    # Satu array berisi semua wahana
    # Index kedua array tersebut disusun secara ordinal sehingga perujukan data pada index ke n pada 
    # array idwahana sama dengan perujukan data dengan index ke n pada array wahana
    # self.__file adalah ArrayData yang memiliki fungsi read()
    def load(self):
        self.__data = (self.__file).read()
        if panjangArray(self.__data)> 0:
            for a in self.__data:
                try: # Jika ada error, maka akan diskip
                    newattraction = Attraction(a[1], int(a[2]), a[3], a[4])
                    self.__idlist = elAdd(self.__idlist, a[0])
                    self.__attractions = elAdd(self.__attractions, newattraction)
                except: # error
                    continue

    # Fungsi untuk menyimpan matrix ke dalam CSV
    # self.__file adalah Data yang memiliki fungsi write(...)
    # self.getAttractionsAsList() adalah fungsi diatas
    # yang berguna untuk mentraspose 2 array menjadi matrix
    # self.__file adalah ArrayData yang memiliki fungsi write(...)
    def save(self):
        (self.__file).write(self.getAttractionsAsList())

    # Fungsi untuk mengubah nama file CSV
    # Panggil fungsi ini terlebih dahulu baru disimpan
    def changeFilename(self, filename):
        self.__file = ArrayData(filename, ['EmptyWahana(index)', 'WahanaEmpty(index)', 999999, "Semua Umur", "Above170"])

    # Fungsi untuk mencari idwahana
    # apakah ada atau tidak
    # mengembalikan Boolean
    def findAttraction(self, idwahana):
        if idwahana in (self.__idlist):
            return True
        return False

    # Fungsi untuk mendapatkan Attraction atau Wahana
    # dengan menginput idwahananya
    def getAttraction(self, idwahana):
        if self.findAttraction(idwahana):
            return cariArray(idwahana, self.__idlist, self.__attractions)
        else:
            raise ValueError(f'Attraction with ID {idwahana} is not found.')

    # Fungsi untuk Mengembalikan Matrix yang berisi array id dan array wahana
    def getAttractions(self):
        return [self.__idlist, self.__attractions]

    # Fungsi untuk Menambah wahana
    def addAttraction(self, idwahana, new):
        if (self.findAttraction(idwahana) == False):
            self.__idlist = elAdd(self.__idlist, idwahana)
            self.__attractions = elAdd(self.__attractions, new)
            return True
        else:
            return False