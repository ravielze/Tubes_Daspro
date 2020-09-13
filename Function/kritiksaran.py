from Core.User import User,UserManager, Role
from Core.Attraction import AttractionManager
from Core.Feedback import FeedbackManager
from Utility.Array import panjangArray, elAdd

# Program Kritik Saran
# Last Update: 15 April 2020

# Deskripsi:
# Program ini berisi prosedur mengirimkan kritik/saran dan membaca kritik/saran.

# procedure sendFeedback
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
# feedmanager    : FeedbackManager
def sendFeedback(user, usermanager, attrmanager, feedmanager):
    if (user != None): # Jika user sudah login

        # Input
        idwahana = input("Masukkan ID Wahana\t\t\t: ")
        datelapor = input("Masukkan Tanggal Pelaporan (DD/MM/YYYY)\t: ")
        kritiksaran = input("Kritik/Saran Anda\t\t\t: ")

        print()

        # Validasi Sederhana untuk Date
        # Setidaknya harus berformat x/x/x
        d = list(map(int, (datelapor).strip().split('/')))
        while (panjangArray(d) != 3):
            print("Tanggal hari ini tidak valid.")
            datelapor = input("Masukkan Tanggal Pelaporan (DD/MM/YYYY)\t: ")
            d = list(map(int, (datelapor).strip().split('/')))

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

        # Karena user = pengguna = kritik/saran
        # sehingga harus dicari username dengan user tersebut pada UserManager
        username = usermanager.findUserbyObject(user)

        # Menambahkan saran ke ticketmanager
        feedmanager.add(username, datelapor, idwahana, kritiksaran)
        print("Kritik dan saran Anda kami terima.")

    else: # Jika belum login
        print("Anda belum login.")

# procedure listFeedback
# user           : User
# feedmanager    : FeedbackManager
def listFeedback(user, feedmanager):
    
    # Fungsi Lokal getAsListOfString()
    # menghasilkan array of string
    def getAsListOfString():
        result = []
        for each in feedmanager.get():
            if panjangArray(str(each[0])) < 8: # Jika panjang username kurang dari 8, tab 2x
                username = str(each[0]) + "\t"
            else:
                username = str(each[0])
            dstr = str(each[2]) + "\t\t | \t" + str(each[1]) + "\t | \t" + username + "\t | \t" + str(each[3])
            result = elAdd(result, dstr)
        return result

    # Fungsi sortir dengan algoritma bubble sort
    # menghasilkan array
    def sortiralphabet(array):
        n = panjangArray(array)
    
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1] :
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    if (user != None): # Jika user sudah login

        if (user.getRole() == Role.Admin): # Jika user adalah admin

            if panjangArray(getAsListOfString()) > 0: # Setidaknya ada satu

                print("Kritik dan saran: \nID Wahana\t | \tTanggal Kritik\t | \tUsername\t | \tIsi Kritik")
                for s in sortiralphabet(getAsListOfString()):
                    print(s)
            else: # tidak ada apapun
                
                print("Tidak ada laporan.")

        else: # Bukan admin
            print("Maaf! Anda bukan admin.")

    else: # belum login
        print("Anda belum login.")

        