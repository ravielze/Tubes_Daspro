import csv,os

# Program Pembacaan CSV Menjadi Array
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi utilitas yang akan digunakan
# untuk membaca file csv menjadi array

# Kamus Fungsi:
# Constructor(String namafile, Array defaultempty)
# rename(String namafile)
# write(Array array)
# size() -> int
# read() -> Array of Array

from Utility.Array import panjangArray, elAdd

# ArrayData
# file          : string
# defaultempty  : array
#
#    Catatan tambahan:
#
#    defaultempty adalah array yang akan menggantikan apabila terdapat
#    baris kosong pada file
#    contoh:
#
#    namadanumur.csv
#    Abdi,28
#    Budi,15
#     
#    Tuti,17
#     
#    Santi,20
#    {file csv selesai}
#
#    tes.py
#    data = ArrayData('namadanumur', ['Empty(index)', index])
#    array = data.read()
#    data.write(array)
#
#    file python selesai dan dijalankan
#    perubahan pada csv akan menjadi sbg berikut
#
#    namadanumur.csv
#    Abdi,28
#    Budi,15
#    Empty2,2
#    Tuti,17
#    Empty4,4
#    Santi,20
#    {file csv selesai}
#
#    Baris kosong akan diganti dengan nama Empty(index) dan umur index
#    file csv selesai/file python selesai bukan mark, hanya komentar.
class ArrayData:

    # Constructor
    def __init__(self, file, defaultempty):
        self.__file = file
        self.__defaultempty = defaultempty
        if not os.path.exists('Data'):
            os.mkdir('Data')

    # Fungsi untuk menulis file
    def write(self, arrays):
        with open("Data/" + self.__file + '.csv', mode='w', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            for x in arrays:
                writer.writerow(x)

    # Fungsi untuk membaca suatu file ke array
    # Baris kosong akan diisi dengan __defaultempty
    def read(self):
        try:
            with open("Data/" + self.__file + '.csv', mode='r', newline='') as f:
                reader = csv.reader(f, dialect='excel')

                result = [] # Inisiasi Array Hasil
                i = 0
                for row in reader:
                    newrow = []
                    if (row != []): # Jika baris ada isi
                        for x in range(panjangArray(row)):
                            now = row[x]
                            try:
                                newrow = elAdd(newrow, int(now)) # coba convert ke integer
                            except ValueError:
                                newrow = elAdd(newrow, now) # kalau gagal convert jadi integer

                    else: # Jika baris tidak ada isi
                        for x in range(panjangArray(self.__defaultempty)):
                            now = self.__defaultempty[x] 

                            try:
                                newrow = elAdd(newrow, int(now)) # coba convert ke integer
                            except ValueError:
                                newrow = elAdd(newrow, (now).replace("(index)", str(i))) # kalau gagal convert jadi integer

                    result += [newrow]
                    i += 1
        except:
            result = [] # Jika file tidak ditemukan, mengembalikan array kosong
        return result