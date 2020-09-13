from Core.User import User,UserManager
from Core.Attraction import Attraction,AttractionManager
from Core.Data import ArrayData
from Utility.Array import panjangArray, elAdd

# Program Kritik Saran
# Last Update: 15 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi untuk menyimpan dan membaca
# file kritik dan saran CSV menjadi array.

# FeedbackManager
# filename  : string
class FeedbackManager:
    def __init__(self, filename):
        self.__file = ArrayData(filename, ['emptyline(index)', '01/01/01', 'WahanaEmpty(index)', 'Empty Feedback(index)'])
        self.__critics = []

    # Fungsi untuk mengambil semua data dari CSV dan mengaksesnya ke dalam matrix
    # self.__file adalah ArrayData yang memiliki fungsi read()
    def load(self):
        self.__data = (self.__file).read()
        if panjangArray(self.__data) > 0:
            for c in self.__data:
                self.__critics = elAdd(self.__critics, c)

    # Fungsi untuk menyimpan matrix menjadi CSV
    # self.__file adalah ArrayData yang memiliki fungsi write(...)
    def save(self):
        (self.__file).write(self.__critics)

    # Fungsi untuk mengubah nama file CSV
    # Panggil fungsi ini terlebih dahulu baru disimpan
    def changeFilename(self, filename):
        self.__file = ArrayData(filename, ['Empty(index)', '01/01/01', 'WahanaEmpty(index)', 'Empty Feedback(index)'])

    # Fungsi untuk menambahkan kritik dan saran yang baru
    def add(self, username, date, idwahana, text):
        new = [username, date, idwahana, text]
        self.__critics = elAdd(self.__critics, new)

    # Fungsi untuk mendapatkan matrix kritik saran
    def get(self):
        return self.__critics