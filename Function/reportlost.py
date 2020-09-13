from Core.User import User,UserManager
from Core.Attraction import AttractionManager
from Core.Tickets import TicketManager
from Core.Inventory import InventoryManager
from Utility.Array import panjangArray

# Program Laporan Kehilangan Tiket
# Last Update: 20 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk menggunakan tiket.

# procedure kehilangan tiket
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
# lostmanager    : TicketManager
# invtmanager    : InventoryManager
def lostticket(user, usermanager, attrmanager, lostmanager, invtmanager):
    if (user != None): # User sudah login
        # Input
        idwahana = input("Masukkan ID Wahana\t\t\t: ")
        datetoday = input("Masukkan Tanggal Hari ini (DD/MM/YYYY)\t: ")
        amount = input("Jumlah Tiket yang dihilangkan\t\t: ")

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
                amount = input("Jumlah Tiket yang digunakan\t\t: ")

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

        username = usermanager.findUserbyObject(user) #mencari username dengan user yang menggunakan prosedur ini

        if user.getTicket(idwahana) >= amount: # Jika tiket memiliki sesuai jumlah

            invtmanager.modify(username, idwahana, (-1)*amount) # Kurangi tiket 
            lostmanager.add(username, datetoday, idwahana, amount) # Tambahkan ke data kehilangan
            print("Laporan kehilangan tiket Anda telah direkam.")

        else: # Tidak memiliki tiket
            print("Anda tidak memiliki tiket terkait.")

    else: # Belum login
        print("Anda belum login.")