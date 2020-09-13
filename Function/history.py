from Core.User import User,UserManager, Role
from Core.Attraction import AttractionManager
from Core.Tickets import TicketManager
from Utility.Array import panjangArray, elAdd

# Program Penggunaan Wahana
# Last Update: 15 April 2020

# Deskripsi:
# Program ini berisi prosedur melihat penggunaan suatu wahana.


# procedure history
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
# usedmanager    : TicketManager
def history(user, usermanager, attrmanager, usedmanager):
    if (user != None): # Jika user sudah login
        
        if (user.getRole() != Role.Admin): #Jika user bukan admin

            print("Maaf! Anda bukan admin.")

        else: # User adalah admin

            # Input
            idwahana = input("Masukkan ID Wahana\t\t\t: ")

            print()

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

            # Memanggil data dari ticketmanager penggunaan
            histories = usedmanager.get()
            # Inisiasi matrix kosong
            match = []
            for each in histories:
                if each[2] == idwahana: # Jika idwahana sama dengan yang dicari
                    match = elAdd(match, each)
            
            if panjangArray(match) == 0: # Jika tidak ditemukan apa-apa
                print("Belum ada yang bermain di wahana tersebut.")
            else: # Setidaknya ada satu penemuan
                print("Riwayat:")
                #judul
                for each in match:
                    if panjangArray(each[0]) < 8: # Jika panjang username kurang dari 8, tab 2x
                        username = each[0] + "\t\t | \t "
                    else: 
                        username = each[0] + "\t | \t "
                    print(f"{each[1]}\t | \t{username}{each[3]}")

    else: # Jika belum login
        print("Anda belum login.")