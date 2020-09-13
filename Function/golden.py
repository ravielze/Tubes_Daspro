from Core.User import Role, User, UserManager

# Program Upgrade Gold
# Last Update: 20 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk mengupgrade user menjadi
# akun golden.

# Kamus:
# price : integer
#    Jumlah yang harus dibayar untuk menjadi golden user

price = 300

def upgradegold(sender, usermanager):
    if (sender != None): # Jika pengirim command sudah login

        if (sender.getRole() != Role.Admin): # pengirim command bukan admin
            print("Maaf! Anda bukan admin.")
        else:

            # Input
            username = input("Masukkan Username yang ingin diupgrade\t: ")

            # Validasi untuk input username
            # Username harus bisa ditemukan
            # Ketik 'exit' untuk membatalkan
            while (usermanager.findUser(username) == False):
                print(f"Username {username} tidak ditemukan.\nKetik 'exit' untuk membatalkan.")
                username = input("Masukkan username pemain\t\t: ")
                if username.lower() == 'exit':
                    print("Topup dibatalkan.")
                    return

            # Mendapatkan user target yang ingin di top up
            user = usermanager.getUser(username)
        
            if (user == Role.Admin): # user adalah admin
                print("Anda adalah admin, admin tidak bisa mengupgrade akun.")

            elif (user == Role.Golden): # user adalah golden
                print("Anda sudah memiliki akun golden.")

            else: # user adalah user

                if (user.getSaldo() < price):
                    print(f"Saldo yang akun tersebut miliki tidak cukup untuk mengupgrade akun.\nHarga: {price}")
                else:
                    user.modifySaldo((-1)*price)
                    user.setRole("Golden")
                    print(f"Berhasil mengupgrade user {username}!\n{user.getName()} sekarang adalah Golden User.\nHarga Upgrade: {price}\nSisa Saldo Anda: {user.getSaldo()}")

    else: # User belum login
        print("Anda belum login.")
