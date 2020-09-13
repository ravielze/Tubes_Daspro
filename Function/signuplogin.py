from Core.User import UserManager, User, Role
from Utility.EncryptDecrypt import Encrypt, Decrypt
from Utility.Array import panjangArray

# Program Signup dan Login
# Last Update: 17 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk signup user dan login user.

# procedure refundticket
# user           : User
# manager        : Usermanager
def signup(user, manager):
    if (user != None): # Jika sudah login
        if (user.getRole() != Role.Admin): # Bukan admin
            print("Maaf! Anda bukan admin.")
        else:
            # Input
            name = input("Masukkan nama pemain\t\t\t\t: ")
            dob = input("Masukkan tanggal lahir pemain (DD/MM/YYYY)\t: ")
            tb = input("Masukkan tinggi badan pemain (cm)\t\t: ")
            username = input("Masukkan username pemain\t\t\t: ")
            pwd = input("Masukkan password pemain\t\t\t: ")
            
            print()

            # Validasi username
            # Username harus 1-16 character
            while panjangArray(username) <= 1 or panjangArray(username) > 16 or (manager.findUser(username)):
                if (manager.findUser(username)):
                    print("Username yang diinginkan tidak tersedia.")
                else:
                    print("Username harus terdiri dari 2-16 character.")
                username = input("Masukkan username pemain\t\t\t: ")
                continue

            # Validasi Sederhana untuk Date
            # Setidaknya harus berformat x/x/x
            d = list(map(int, (dob).strip().split('/')))
            while (panjangArray(d) != 3):
                print("Tanggal lahir pemain tidak valid!")
                dob = input("Masukkan tanggal lahir pemain (DD/MM/YYYY)\t: ")
                d = list(map(int, (dob).strip().split('/')))

            # Validasi sederhana untuk tinggi badan
            # Nilai tinggi badan harus 1-250cm
            while True:
                try:
                    tb = int(tb)
                    if (tb <= 0 or tb > 250):
                        print("Tinggi badan pemain tidak valid! (1-250 cm)")
                        tb = input("Masukkan tinggi badan pemain (cm)\t\t: ")
                        continue
                    break
                except:
                    print("Tinggi badan pemain tidak valid!")
                    tb = input("Masukkan tinggi badan pemain (cm)\t\t: ")

            # Validasi password
            # Password minimal 8 character
            while panjangArray(pwd) < 8:
                print("Password minimal terdiri dari 8 character.")
                pwd = input("Masukkan password pemain\t\t\t: ")

            print()
            
            pwd = Encrypt(pwd)

            # Membuat user baru
            newUser = User(name, dob, tb, pwd, 'User', 0)
            manager.addUser(username, newUser) # Menambahkan ke data
            print(f"Selamat menjadi pemain, {name}. Selamat bermain.")
    else: # Belum login
        print("Anda belum login.")

# fungsi login
# username          : string
# pwd               : string
# manager           : UserManager
def login(username, pwd, manager):
    def error(): # Prosedur lokal untuk eror
        print('Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!')

    user = None
    if (manager.findUser(username) == False): #Jika tidak ditemukan user
        error()
    else: 
        user = manager.getUser(username) # Mendapatkan user
        if (Decrypt(user.getPassword()) != pwd): # Jika user salah password
            error()
            user = None
    # variabel user akan bernilai sesuatu jika login berhasil
    # none jika gagal.
    return user