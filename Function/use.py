from Core.User import User,UserManager
from Core.Attraction import AttractionManager
from Core.Tickets import TicketManager
from Core.Inventory import InventoryManager
from Utility.Array import panjangArray

# Program Pengunaan Tiket
# Last Update: 17 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk menggunakan tiket.

# procedure menggunakan tiket
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
# usedmanager    : TicketManager
# invtmanager    : InventoryManager
def useticket(user, usermanager, attrmanager, usedmanager, invtmanager):
    if (user != None): # User sudah login
        # Input
        idwahana = input("Masukkan ID Wahana\t\t\t: ")
        datetoday = input("Masukkan Tanggal Hari ini (DD/MM/YYYY)\t: ")
        amount = input("Jumlah Tiket yang digunakan\t\t: ")

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
        attr = attrmanager.getAttraction(idwahana)

        user.calcAge(datetoday) # hitung umur dengan data tanggal hari ini

        # Jika Ketentuan Wahana ada pada kategori pengguna
        if (attr.getAR() in user.getAC() and attr.getHR() in user.getHC()):

            if user.getTicket(idwahana) >= amount: # Jika tiket memiliki sesuai jumlah

                invtmanager.modify(username, idwahana, (-1)*amount) # Kurangi tiket 
                usedmanager.add(username, datetoday, idwahana, amount) # Tambahkan ke data pengunaan
                print(f"Terima kasih telah bermain.\nBerhasil memakai {amount} tiket.")

            else: # Tidak memiliki tiket
                print("Anda tidak memiliki tiket terkait.")

        else: # Jika pengguna tidak memenuhi ketentuan yang ada
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")

    else: # Belum login
        print("Anda belum login.")