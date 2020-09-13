from enum import Enum
# Enumerasi hanya diasumsikan sebagai arrayList yang tidak bisa
# diubah. Bernilai 0,1,...,n dan tidak perlu mendeklarasi terus menerus hal yang sama
from Utility.Tanggal import selisihtgl
from Utility.Array import elAdd, panjangArray, cariArray, elAdd
from Core.Data import ArrayData
from Core.Attraction import HeightRestricton,AgeRestriction
from Utility.EncryptDecrypt import Encrypt

# Program User
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi yang berkaitan dengan tipe bentukan
# User. Untuk penjelasan setiap fungsinya ada di atas segmen setiap fungsi.

# Enumerasi Tipe Role
class Role(Enum):
    # Jika dipanggil, akan mengembalikan "Admin", "Golden" atau "User"
    # dipakai hanya untuk pemanggilan array final tanpa deklarasi terus menerus
    def __str__(self):
        return str(self.name)
    Admin = 2
    Golden = 1
    User = 0

hariini = [14,4,2020]

# User
# name      : string
# dob       : string
# password  : string
# role      : string
# saldo     : int

class User:
    def __init__(self, name, dob, height, password, role, saldo=0):
        self.__name = name
        self.__dobstr = dob
        self.__password = password
        if (role.lower() == 'admin'):
            self.__role = Role.Admin
        elif (role.lower() == 'user'):
            self.__role = Role.User
        elif (role.lower() == 'golden'):
            self.__role = Role.Golden
        else:
            raise ValueError('Role should be filled with "Golden" or "User" or "Admin"')
        self.__saldo = saldo
        self.__height = height
        self.__tickets = []
        self.__ticketids = []
        self.__heightcategory = [HeightRestricton.All]
        self.__agecategory = [AgeRestriction.SemuaUmur]

        self.calcHeight() # inisiasi hitung tinggi
        # hitung umur dilakukan setiap kali memasukkan tanggal
        # hari ini, jadi tidak bisa di inisiasi terlebih dahulu
        # sedangkan hitung tinggi bisa di inisiasi karena ada data
        # tinggi yang tidak akan berubah.

    # Prosedur menghitung umur
    # dan menyimpan kedalam User.age
    # serta menghitung kategori apa saja User tersebut
    # disimpan dalam array User.agecategory
    # tanggal   : string
    def calcAge(self, tanggal):
        d = list(map(int, (self.__dobstr).strip().split('/')))
        dt = list(map(int, tanggal.strip().split('/')))
        s = selisihtgl(d,dt)

        self.__agecategory = [AgeRestriction.SemuaUmur]

        self.__age = int(s / (365.2425))
        
        if (self.__age < 17): # Jika umur dibawah 17, tambahkan restriksi anak
            self.__agecategory = elAdd(self.__agecategory, AgeRestriction.Anak)
        else: # Jika umur diatas sama dengan 17, tambahkan restriksi dewasa
            self.__agecategory = elAdd(self.__agecategory, AgeRestriction.Dewasa)

    # Prosedur menghitung kategori tinggi
    # disimpan dalam array User.heightcategory
    def calcHeight(self):
        self.__heightcategory = [HeightRestricton.All]
        if (self.__height >= 170): # Tambahkan restriksi diatas sama dengan 170 saat tinggi diatas 170
            self.__heightcategory = elAdd(self.__heightcategory, HeightRestricton.Above170)

    # getter dan setter
    # Mengembalikan suatu nilai
    # Mengubah suatu nilai
    def getName(self):
        return self.__name
    def getDOB(self):
        return self.__dobstr
    def getPassword(self):
        return self.__password
    def getRole(self):
        return self.__role
    def getSaldo(self):
        return self.__saldo
    def getTickets(self):
        return self.__tickets
    def getTicketIDs(self):
        return self.__ticketids
    def getAge(self):
        return self.__age
    def getHeight(self):
        return self.__height
    def getAC(self):
        return self.__agecategory
    def getHC(self):
        return self.__heightcategory

    def setName(self, newname):
        self.__name = newname
    def setDOB(self, newdob):
        self.__dobstr = newdob
        self.calcAge()
    def setPassword(self, newpwd):
        self.__password = newpwd
    def setHeight(self, height):
        self.__height = height
    def setRole(self, newrole):
        if (newrole.lower() == 'admin'):
            self.__role = Role.Admin
        elif (newrole.lower() == 'user'):
            self.__role = Role.User
        elif (newrole.lower() == 'golden'):
            self.__role = Role.Golden
        else:
            raise ValueError('Role should be filled with "Golden" or "User" or "Admin"')

    # Fungsi untuk mengubah saldo menjadi newsaldo
    def setSaldo(self, newsaldo):
        self.__saldo = newsaldo
    # Fungsi untuk menambah saldo sebanyak amount
    # kalau amount minus, jadi pengurangan
    def modifySaldo(self, amount):
        self.__saldo += amount

    # Fungsi untuk mengubah tiket
    def setTickets(self, newticket, idticket):
        self.__tickets = newticket
        self.__ticketids = idticket
    # Fungsi untuk mendapat tiket dengan idwahana
    def getTicket(self, idwahana):
        if idwahana in self.__ticketids:
            return cariArray(idwahana, self.__ticketids, self.__tickets)
        else:
            return 0

# UserManager
# filename  : string
class UserManager:
    def __init__(self, filename):
        self.__file = ArrayData(filename, ['Empty(index)', '01/01/01', "(index)", "emptyline(index)", "(index)", "User", 0])
        self.__users = []
        self.__userids = []

    # Fungsi untuk mengubah array of user menjadi matrix
    # digunakan untuk diimplementasikan pada fungsi save
    # untuk menyimpan kembali kedalam csv
    def getUsersAsList(self):
        result = []
        for i in range(panjangArray(self.__userids)):
            user = self.__users[i]
            arr = [] # ini adalah array dalam satu baris
            arr = elAdd(arr, user.getName()) # penambahan elemen tiap baris
            arr = elAdd(arr, user.getDOB()) # hal yang sama dengan atas
            arr = elAdd(arr, user.getHeight()) # hal yang sama dengan atas
            arr = elAdd(arr, (self.__userids[i]).lower()) # hal yang sama dengan atas
            arr = elAdd(arr, user.getPassword()) # hal yang sama dengan atas
            arr = elAdd(arr, user.getRole()) # hal yang sama dengan atas
            arr = elAdd(arr, user.getSaldo()) # hal yang sama dengan atas
            result = elAdd(result, arr) # masukkan kedalam kolom
            #print(result)
        return result

    # Fungsi untuk Mengembalikan Matrix yang berisi array id dan array user
    def getAllUsers(self):
        return [self.__userids, self.__users]

    # Fungsi untuk mengambil semua data dari CSV dan mengaksesnya ke dalam matrix
    # Lalu matrix akan di transpos ke dalam 2 array
    # Satu array berisi semua id user
    # Satu array berisi semua user
    # Index kedua array tersebut disusun secara ordinal sehingga perujukan data pada index ke n pada 
    # array idwahana sama dengan perujukan data dengan index ke n pada array wahana
    # self.__file adalah ArrayData yang memiliki fungsi read()
    def load(self):
        self.__data = (self.__file).read()
        if panjangArray(self.__data) > 0:
            x = 0
            for u in self.__data:
                newuser = User(u[0], u[1], int(u[2]), u[4], u[5], int(u[6]))
                self.__userids = elAdd(self.__userids, ((u[3]).lower()))
                self.__users = elAdd(self.__users, newuser)

    # Fungsi untuk menyimpan matrix ke dalam CSV
    # self.__file adalah ArrayData yang memiliki fungsi write(...)
    # self.getUsersAsList() adalah fungsi diatas
    # yang berguna untuk mentraspose 2 array menjadi matrix
    def save(self):
        (self.__file).write(self.getUsersAsList())

    # Fungsi untuk mengubah nama file CSV
    # Panggil fungsi ini terlebih dahulu baru disimpan
    def changeFilename(self, filename):
        self.__file = ArrayData(filename, ['Empty(index)', '01/01/01', "(index)", "emptyline(index)", "(index)", "User", 0])

    # Fungsi untuk mencari user
    # apakah ada atau tidak dengan username
    # mengembalikan Boolean
    def findUser(self, username):
        if (username.lower()) in (self.__userids):
            return True
        return False

    # Fungsi untuk mencari username dengan user
    # mengembalikan username/String
    def findUserbyObject(self, user):
        return cariArray(user, self.__users, self.__userids)

    # Fungsi untuk mencari user dengan username
    # mengembalikan User
    def getUser(self, username):
        return cariArray(username, self.__userids, self.__users)

    # Fungsi untuk menambah user baru
    def addUser(self, username, new):
        if (self.findUser(username.lower()) == False):
            self.__users = elAdd(self.__users, new)
            self.__userids = elAdd(self.__userids, username)