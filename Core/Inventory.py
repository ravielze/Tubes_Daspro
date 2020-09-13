from Core.Data import ArrayData
from Core.User import User,UserManager
from Core.Attraction import AttractionManager,Attraction
from Utility.Array import elAdd, panjangArray, cariArray

# Program Inventory
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi untuk memproses jumlah tiket
# yang dimiliki setiap user. Fungsi ini harus dipanggil setelah
# UserManager dan AttractionManager dimuat karena fungsi disini
# terkait memanggil data dari sana.

# InventoryManager
# usermanager   : UserManager
# attrmanager   : AttractionManager
# filename      : String
class InventoryManager:
    def __init__(self, attrmanager, usermanager, filename):
        self.__file = ArrayData(filename, ['emptyline(index)', 'WahanaEmpty(index)', 0])
        self.__um = usermanager
        self.__am = attrmanager
    
    # Fungsi untuk mengambil semua data dari CSV dan memasukkan kedalam UserManager
    # UserManager akan mengubah User tersebut supaya bisa memiliki kepemilikan tiket.
    def load(self):
        self.__data = (self.__file).read()
        if panjangArray(self.__data) > 0:
            for i in self.__data:
                try:
                    self.modify(i[0], i[1], int(i[2]))
                except ValueError as e:
                    continue #Jika jumlah tiket bukan integer maka akan di skip

    # Fungsi untuk mengambil data tiket dari semua user
    # yang disimpan pada usermanager self.__um dengan
    # mengembalikan matrix
    def getAllUsersInventoryAsList(self):
        userids = ((self.__um).getAllUsers())[0]
        users = ((self.__um).getAllUsers())[1]
        result = []
        for i in range(panjangArray(userids)):
            for idwahana in users[i].getTicketIDs():
                if users[i].getTicket(idwahana) > 0: # Jika tiket positif tak nol
                    result = elAdd(result, [userids[i], idwahana, users[i].getTicket(idwahana)])
        return result

    # Fungsi untuk menyimpan matrix ke dalam CSV
    # self.__file adalah ArrayData yang memiliki fungsi write(...)
    def save(self):
        (self.__file).write(self.getAllUsersInventoryAsList())

    # Fungsi untuk mengubah nama file CSV
    # Panggil fungsi ini terlebih dahulu baru disimpan
    def changeFilename(self, filename):
        self.__file = ArrayData(filename, ['emptyline(index)', 'WahanaEmpty(index)', 0])
                
    # Fungsi yang digunakan untuk memodifikasi jumlah tiket seseorang
    # normal adalah boolean dimana, jika True, akan menambah penjualan wahana tersebut
    # serta mengambil uang dari orang
    # False jika fungsi ini digunakan untuk inisiasi data dari CSV
    # Factor adalah diskon
    # Jika amount negatif, user akan mendapat saldo
    def modify(self, username, idwahana, amount, normal=False, factor=100):
        user = (self.__um).getUser(username)
        attr = (self.__am).getAttraction(idwahana)

        if user != None: # User ditemukan
            inventory = user.getTickets() #mendapatkan array of int yg berisi jumlah tiket
            ids = user.getTicketIDs()
            index = cariArray(idwahana, ids) # cariArray akan menghasil kan index (int), None jika tidak ditemukan
            if index != None: # Sudah ada
                inventory[index] += amount # menambahkan jumlah
            else: # belum ada
                ids = elAdd(ids, idwahana) #tambah baru
                inventory = elAdd(inventory, amount)

            if normal: # Penjelasan normal ada di komentar diatas fungsi
                attr.newSale(amount)
                price = int(round(factor*attr.getTicketPrice()/100))
                user.modifySaldo((-1)*amount*price)
            user.setTickets(inventory, ids)