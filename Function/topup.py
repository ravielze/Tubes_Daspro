from Core.User import User, UserManager, Role

# Program Top Up
# Last Update: 17 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk topup user.

# procedure searchUser
# user           : User
# usermanager    : Usermanager
def topup(user, manager):
    if (user != None): # Jika sudah login

        if (user.getRole() != Role.Admin): # Bukan admin

            print("Maaf! Anda bukan admin.")

        else: # Admin

            # Input
            username = input("Masukkan Username\t\t: ")
            saldo = input("Masukkan Tambahan Saldo\t\t: ")

            # Validasi untuk input username
            # Username harus bisa ditemukan
            # Ketik 'exit' untuk membatalkan
            while (manager.findUser(username) == False):
                print(f"Username {username} tidak ditemukan.\nKetik 'exit' untuk membatalkan.")
                username = input("Masukkan username pemain\t\t: ")
                if username.lower() == 'exit':
                    print("Topup dibatalkan.")
                    return

            # Validasi untuk jumlah saldo harus integer
            while True:

                try:
                    saldo = abs(int(saldo))
                    break

                except:
                    print("Tambahan saldo tidak valid.")
                    saldo = input("Masukkan Tambahan Saldo\t\t: ")

            # Mendapatkan user target yang ingin di top up
            user = manager.getUser(username)
            user.modifySaldo(saldo) # Top up
            print(f"Top up berhasil.\nRincian Saldo {user.getName()}:\nSebelum\t\t: {user.getSaldo()-saldo}\nSesudah\t\t: {user.getSaldo()}\nPenambahan\t: +{saldo}")


    else: # Belum login

        print("Anda belum login.")