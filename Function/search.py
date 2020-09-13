from Core.User import UserManager, User, Role
from Core.Attraction import AttractionManager, Attraction, HeightRestricton, AgeRestriction
from Utility.Array import panjangArray, elAdd

# Program Search User, Show Inventory, dan Search Wahana
# Last Update: 17 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk mencari user/wahana dan menunjukkan inventory ticket seorang user.

# procedure searchUser
# user           : User
# usermanager    : Usermanager
def searchUser(user, manager):

    if (user != None): # Sudah login

        if (user.getRole() != Role.Admin): # Bukan admin

            print("Maaf! Anda bukan admin.")

        else:
            
            # Input
            username = input("Masukkan Username\t\t: ")

            # Jika username ditemukan dalam data
            if (manager.findUser(username)):

                user = manager.getUser(username) #dapatkan user dengan username tersebut
                print(f"Nama Pemain\t\t\t: {user.getName()}")
                print(f"Tinggi Pemain\t\t\t: {user.getHeight()} cm")
                print(f"Tanggal Lahir Pemain\t\t: {user.getDOB()}")

            else: # Tidak ditemukan

                print(f"Pemain dengan username {username} tidak ditemukan.")

    else: # Belum login

        print("Anda belum login.")

# procedure showInventory
# user           : User
# usermanager    : UserManager
# attrmanager    : AttractionManager
def showInventory(user, usermanager, attrmanager):
    
    if (user != None): # sudah login

        if (user.getRole() != Role.Admin): # bukanadmin

            print("Maaf! Anda bukan admin.")
        
        else:
            
            #Input
            username = input("Masukkan Username\t: ")

            # Validasi user sederhana
            # untuk mencari user sampai ketemu
            # 'exit' untuk keluar
            while (usermanager.findUser(username) == False):
                print(f"Username {username} tidak ditemukan.\nKetik 'exit' untuk membatalkan.")
                username = input("Masukkan username pemain\t: ")
                if (username.lower()) == 'exit':
                    print("Melihat jumlah tiket dibatalkan.")
                    return

            # mendapatkan tiket dari username tersebut
            tickets = (usermanager.getUser(username)).getTickets()
            ticketids = (usermanager.getUser(username)).getTicketIDs()

            if panjangArray(tickets) > 0: #Jika panjang lebih dari 0
                print("Kepemilikan Tiket:\n ID Wahana\t | \tNama Wahana\t | \tJumlah Tiket")
                for i in range(panjangArray(tickets)):
                    attr = attrmanager.getAttraction(ticketids[i])
                    if panjangArray(attr.getName()) < 8: # Kalau panjang nama wahan kurang dari 8 tambah tab
                        wahana = attr.getName() + "\t"
                    else:
                        wahana = attr.getName() # kalau panjang nama wahana lebih dari 8 tidak tab
                    print(f" {ticketids[i]}\t\t | \t{wahana}\t | \t{tickets[i]}")
            else:
                print("Pemain tersebut tidak memiliki tiket.")

    else: #belum login

        print("Anda belum login.")

# procedure searchAttraction
# user           : User
# attrmanager    : AttractionManager
def searchAttraction(user, attrmanager):

    # Fungsi lokal Search
    # batasumur     : int
    # batastinggi   : int
    # fungsi untuk mencari wahana dengan batas tinggi dan umur tertentu
    def search(batasumur, batastinggi): 
        result = []
        attractionlist = (attrmanager.getAttractions())[1]
        attractionids = (attrmanager.getAttractions())[0]
        for i in range(panjangArray(attractionlist)):
            attr = attractionlist[i]
            idwahana = attractionids[i]
            if (attr.getAR() == AgeRestriction(batasumur)) and (attr.getHR() == HeightRestricton(batastinggi)): # Jika Wahana tersebut sesuai
                attrstr = str(idwahana) + "\t\t | \t" # Formatting nama dengan tab supaya rapih
                if panjangArray(attr.getName()) < 8: # Jika panjang nama kurang dari 8
                    attrstr = attrstr + attr.getName() + "\t\t | \t"
                else: # panjang nama lebih dari 8
                    attrstr = attrstr + attr.getName() + "\t | \t"
                attrstr = attrstr + str(attr.getTicketPrice())
                result = elAdd(result, attrstr)
        return result

    if (user != None): # User sudah login
        print("Jenis batasan umur:\n1.\tAnak-anak (<17 tahun)\n2.\tDewasa (>=17 tahun)\n3.\tSemua umur\n")
        print("jenis batasan tinggi badan:\n1.\tLebih dari 170 cm\n2.\tTanpa batasan\n")

        # Input
        batasumur = input("Batasan Umur Pemain\t\t: ")
        
        # Validasi pilihan batas umur
        while not(batasumur in ['1', '2', '3']):
            print("Batasan umur tidak valid!")
            batasumur = input("Batasan Umur Pemain\t\t: ")

        # Input
        batastinggi = input("Batasan Tinggi Pemain\t\t: ")

        # Validasi pilihan batas tinggi
        while not(batastinggi in ['1', '2']):
            print("Batasan tinggi badan tidak valid!")
            batastinggi = input("Batasan Tinggi Pemain\t\t: ")

        # Kurangi satu karna array (enum) dari batasumur dan batastinggi mulai dari 0
        batasumur = int(batasumur) - 1
        batastinggi = int(batastinggi) - 1

        # Menggunakan fungsi diatas
        s = search(batasumur, batastinggi)

        if panjangArray(s) == 0: # Jika pencarian = 0

            print("Tidak ada wahana yang sesuai dengan pencarian kamu.")

        else:  # Setidaknya ada pencarian

            print("Hasil Pencarian:\nID Wahana\t | \tNama Wahana\t | \tHarga Tiket")

            for each in s:
                print(each)

    else: # Belum login

        print("Anda belum login.")