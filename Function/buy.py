from Core.User import User, UserManager, Role
from Core.Attraction import Attraction, AttractionManager
from Core.Tickets import TicketManager
from Core.Inventory import InventoryManager
from Utility.Array import panjangArray

# Program Beli Tiket
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisi prosedur pembelian ticket.

# Kamus:
# gpay : integer
#    jika gpay = 60 berarti diskon untuk golden user 40%

gpay = 50 # karena diminta diskonnya setengah harga, gpay=50%
# procedure buyticket
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
# bghtmanager    : TicketManager
# invtmanager    : InventoryManager
def buyticket(user, usermanager, attrmanager, bghtmanager, invtmanager):
    if (user != None): # User sudah login
        # Input
        idwahana = input("Masukkan ID Wahana\t\t\t: ")
        datetoday = input("Masukkan Tanggal Hari ini (DD/MM/YYYY)\t: ")
        amount = input("Jumlah Tiket yang dibeli\t\t: ")

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
                amount = input("Jumlah Tiket yang dibeli\t\t: ")

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

        user.calcAge(datetoday) # hitung umur dengan data tanggal hari ini

        # Jika Ketentuan Wahana ada pada kategori pengguna
        if (attr.getAR() in user.getAC() and attr.getHR() in user.getHC()):
            if user.getRole() == Role.User: # Jika user adalah user biasa
                priceperticket = attr.getTicketPrice()
                goldendiscount = 100
            else: # Jika user adalah golden/admin
                goldendiscount = gpay
                priceperticket = int(round(attr.getTicketPrice()*goldendiscount/100))

            if user.getSaldo() >= (priceperticket*amount): # Pengguna harus memiliki saldo
                
                bghtmanager.add(username, datetoday, idwahana, amount) # Memanggil boughtmanager untuk menyimpan data pembelian
                invtmanager.modify(username, idwahana, amount, True, goldendiscount) # Memanggil inventory untuk menyimpan data kepemilikan tiket
                print(f"Selamat bersenang-senang di {attr.getName()}.\nBerhasil membeli {amount} tiket seharga {priceperticket}/tiket.\nTotal penjualan tiket pada wahana ini: {attr.getSale()} tiket.")
                if goldendiscount != 100:
                    print(f"Diskon {100-gpay}% karena akun Golden.")

            else: # tidak punya saldo
                print(f"Saldo Anda tidak cukup.\nSilakan mengisi saldo Anda.\nHarga\t\t: {attr.getTicketPrice()*amount}\nSaldo Anda\t\t: {user.getSaldo()}")

        else: # Jika pengguna tidak memenuhi ketentuan yang ada
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")

    else:
        print("Anda belum login.")
