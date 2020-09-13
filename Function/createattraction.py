from Core.Attraction import AttractionManager, Attraction
from Core.User import User, UserManager, Role
from Utility.Array import panjangArray

# Program Beli Tiket
# Last Update: 15 April 2020

# Deskripsi:
# Program ini berisi prosedur pembuatan wahana.


# procedure createattraction
# user           : User
# usermanager    : Usermanager
# attrmanager    : AttractionManager
def createattraction(user, usermanager, attrmanager):

    if (user != None): # Jika user sudah login

        if (user.getRole() != Role.Admin): # Jika user yang menggunakan bukan admin

            print("Maaf! Anda bukan admin.")

        else:

            # Input
            idwahana = (input("Masukkan ID Wahana\t\t\t\t: ")).upper()
            name = input("Masukkan Nama Wahana\t\t\t\t: ")
            price = input("Masukkan Harga Tiket\t\t\t\t: ")
            batasumur = input("Batasan Umur (Anak-anak/Dewasa/Semua Umur)\t: ").lower()
            batastinggi = input("Batasan Tinggi Badan (>=170/Tanpa Batasan)\t: ").lower()
            
            print()
            
            # Asumsi IDWahana benar

            # Validasi harga harus integer
            while True:
                try:
                    price = abs(int(price))
                    break
                except:
                    print("Harga Tiket tidak valid.")
                    price = input("Masukkan Harga Tiket\t\t\t\t: ")

            # Validasi batasan tinggi dan batasan umur
            while (batastinggi != '>=170' and batastinggi != 'tanpa batasan'):
                print("Batasan Tinggi tidak valid.")
                batastinggi = input("Batasan Tinggi Badan (>=170/Tanpa Batasan)\t: ").lower()

            while (batasumur != 'anak-anak' and batasumur != 'semua umur' and batasumur != 'dewasa'):
                print("Batasan Umur tidak valid.")
                batasumur = (input("Batasan Umur (Anak-anak/Dewasa/Semua Umur)\t: ")).lower()

            print()
            
            # Pembuatan Atraksi baru
            newAttraction = Attraction(name, price, batasumur, batastinggi)
            # Menambahkan atraksi baru kedalam data
            if attrmanager.addAttraction(idwahana, newAttraction): #Jika penambahan berhasil (tidak ada id wahana yang sama)

                print(f"Wahana {name} telah ditambahkan.")
            else:
                print(f"Wahana dengan id {idwahana} sudah ada, silakan buat id lain.")
                createattraction(user, usermanager, attrmanager) #Ulang fungsi ini

    else: # Jika user belum login

        print("Anda belum login.")