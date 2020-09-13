from Core.Data import ArrayData
from Core.Attraction import AttractionManager,Attraction
from Core.User import User,UserManager
from Utility.Array import elAdd, panjangArray

# Program Ticket
# Last Update: 15 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi untuk menyimpan dan membaca
# file yang berhubungan dengan tiket seperti refund, pembelian dan penggunaan.
# Satu program ini bisa dipanggil di variabel yang berbeda sehingga bisa
# dibedakan mana yang refund, pembelian dan penggunaan.

class TicketManager:
    def __init__(self, filename):
        self.__file = ArrayData(filename, ['emptyline(index)', '01/01/01', 'WahanaEmpty(index)', 0])

        self.__history = []

    # Fungsi untuk mengambil semua data dari CSV dan mengaksesnya ke dalam matrix
    # self.__file adalah ArrayData yang memiliki fungsi read()
    def load(self):
        self.__data = (self.__file).read()
        if panjangArray(self.__data) > 0:
            for c in self.__data:
                try:
                    c[3] = int(c[3])
                except ValueError as e:
                    c[3] = 0 # Kalau Jumlah Tiket bukan Integer, maka akan diubah menjadi 0

                self.__history = elAdd(self.__history, c)

    # Fungsi untuk menyimpan matrix menjadi CSV
    # self.__file adalah ArrayData yang memiliki fungsi write(...)
    def save(self):
        (self.__file).write(self.__history)

    # Fungsi untuk mengubah nama file CSV
    # Panggil fungsi ini terlebih dahulu baru disimpan
    def changeFilename(self, filename):
        self.__file = ArrayData(filename, ['emptyline(index)', '01/01/01', 'WahanaEmpty(index)', 0])

    # Fungsi untuk menambahkan kritik dan saran yang baru
    def add(self, username, date, idwahana, amount):
        new = [username, date, idwahana, amount]
        self.__history = elAdd(self.__history, new)

    # Fungsi untuk mendapatkan matrix kritik saran
    def get(self):
        return (self.__history)