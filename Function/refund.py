from Core.User import User,UserManager
from Core.Attraction import AttractionManager, Attraction
from Core.Tickets import TicketManager
from Core.Inventory import InventoryManager
from Utility.Array import panjangArray

# Program Refund
# Last Update: 17 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk refund ticket.

# procedure refundticket
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
# rfndmanager    : TicketManager
# invtmanager    : InventoryManager
# refundpercent  : integer
def refundticket(user, usermanager, attrmanager, rfndmanager, invtmanager, refundpercent): #sebanyak refund% dari harga tiket akan dikembalikan kepada user
    if (user != None): # User sudah login

        # Input
        idwahana = input("Masukkan ID Wahana\t\t\t: ")
        datetoday = input("Masukkan Tanggal Hari ini (DD/MM/YYYY)\t: ")
        amount = input("Jumlah Tiket yang direfund\t\t: ")

        print()

        # Validasi Sederhana untuk Date
        # Setidaknya harus berformat x/x/x
        d = list(map(int, (datetoday).strip().split('/')))
        while (panjangArray(d) != 3):
            print("Tanggal hari ini tidak valid.")
            datetoday = input("Masukkan Tanggal Hari ini (DD/MM/YYYY)\t: ")
            d = list(map(int, (datetoday).strip().split('/')))

        # Validasi untuk input integer
        while True:
            try:
                amount = abs(int(amount))
                break
            except:
                print("Jumlah tiket tidak valid.")
                amount = input("Jumlah Tiket yang direfund\t\t: ")

        # Validasi untuk input ID Wahana
        # ID Wahana harus bisa ditemukan
        # Ketik 'exit' untuk membatalkan
        while not(attrmanager.findAttraction(idwahana)):
            print("ID Wahana yang dimasukkan tidak valid.\nKetik 'exit' untuk membatalkan.")
            idwahana = input("Masukkan ID Wahana\t\t\t: ")
            if idwahana.lower() == 'exit':
                print("Pembelian tiket dibatalkan.")
                return
        
        print()

        # Karena user = pengguna = pembeli
        # sehingga harus dicari username dengan user tersebut pada UserManager
        username = usermanager.findUserbyObject(user)
        attr = attrmanager.getAttraction(idwahana)

        # User harus memiliki tiket untuk direfund
        if user.getTicket(idwahana) >= amount:

            invtmanager.modify(username, idwahana, ((-1)*amount), True, refundpercent) # Menambah tiket sebanyak minus akan mengurangi tiket user tersebut
                                                                                       # Harga minus supaya uang menjadi kembali
            rfndmanager.add(username, datetoday, idwahana, amount) # Menambah hal refund ini ke data refund
            print(f"Uang refund sudah kami berikan pada akun Anda.\nBerhasil me-refund {amount} tiket.\nTotal penjualan tiket pada wahana ini: {attr.getSale()} tiket.")

        else: # User tidak memiliki tiket
            print("Anda tidak memiliki tiket terkait.")

    else: # User belum login
        print("Anda belum login.")