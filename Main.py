import Function.loadsave as LS
from Function.signuplogin import signup, login
from Function.search import searchUser, searchAttraction, showInventory
from Function.use import useticket
from Function.buy import buyticket
from Function.refund import refundticket
from Function.kritiksaran import listFeedback, sendFeedback
from Function.createattraction import createattraction
from Function.topup import topup
from Function.history import history
from Function.bestwahana import bestwahana
from Function.golden import upgradegold
from Function.reportlost import lostticket

# Program Utama Willy Wangky
# Last Update: 20 April 2020

# Deskripsi:
# Program ini berisi program utama untuk menjalankan semua fungsi
# dan prosedur yang ada.
#
# Program yang dijalankan adalah program ini.
# Letakkan file csv anda pada folder Data
#
# Jika file csv anda belum terenkripsi, letakkan pada folder Data lalu
# jalankan program FileEncrypt.py

user = None # Awalnya user kosong, terisi apabila berhasil login
usermanager = None
attrmanager = None

try: # Dipakai untuk mengantisipasi keluar dengan CTRL+C / KeyboardInterupt 
     # KeyboardInterrupt akan sama dengan command exit/keluar
    while True: # Dilakukan terus menerus sampe keluar
        # Input Command
        # replace digunakan untuk fleksibilitas
        # sehingga command-command yang menggunakan garis bawah
        # bisa diganti dengan spasi atau sebaliknya
        cmd = ((input("$ ")).lower()).replace(" ", "_")

        # Jika input adalah load, lakukan load
        if cmd == 'load':
            if usermanager == None and attrmanager == None:
                LS.load()
                usermanager = LS.usermanager
                attrmanager = LS.attrmanager
                bghtmanager = LS.bghtmanager
                invtmanager = LS.invtmanager
                usedmanager = LS.usedmanager
                rfndmanager = LS.rfndmanager
                feedmanager = LS.feedmanager
                lostmanager = LS.lostmanager
            else:
                print('Anda sudah melakukan load file.')
            continue

        # Jika usermanager dan attrmanager masih None, berarti belum pernah load
        # sehingga, hal ini harus diantisipasi dengan cara seperti ini.
        if usermanager == None or attrmanager == None:
            print("Untuk melakukan sesuatu, anda perlu melakukan command 'load'.")
            continue
        
        # Jika command save, lakukan save
        if cmd == 'save':
            LS.save()

        # Jika command signup, lakukan signup
        elif cmd == 'signup':
            signup(user, usermanager)

        # Jika command login, lakukan login
        elif cmd == 'login':
            if user == None: # Jika user masih kosong atau belum ada yang login, lakukan login
                user = login(input("Masukkan username\t\t: "), input("Masukkan password\t\t: "), usermanager)
                # fungsi login mereturn None jika salah password/username tidak ditemukan
                # sehingga, jika user tidak none, berarti berhasil login
                if user != None:
                    print(f"Selamat bersenang-senang, {user.getName()}!")
            else: # Sebaliknya, sudah ada user yang login
                print("Anda sudah login.\nSilakan 'logout' untuk keluar.")

        elif cmd == 'logout': # untuk logout/keluar sebagai user tertentu
            if (user == None): # Belum login
                print("Anda belum login.")
            else: # Sudah login maka berhasil logout
                print(f"Berhasil logout, Sampai jumpa kembali {user.getName()}!")
                user = None

        # Jika fungsi adalah cari pemain, lakukan cari pemain
        elif cmd == 'cari_pemain':
            searchUser(user, usermanager)

        # Jika fungsi adalah cari wahana, lakukan pencarian wahana
        elif cmd == 'cari':
            searchAttraction(user, attrmanager)

        # Jika fungsi adalah beli tiket, lakukan pembelian tiket
        elif cmd == 'beli_tiket':
            buyticket(user, usermanager, attrmanager, bghtmanager, invtmanager)

        # Jika fungsi main, lakukan penggunaan tiket
        elif cmd == 'main':
            useticket(user, usermanager, attrmanager, usedmanager, invtmanager)

        # Jika fungsi refund, lakukan pengajuan refund
        elif cmd == 'refund':
            refundticket(user, usermanager, attrmanager, rfndmanager, invtmanager, 50)

        # Jika fungsi adalah kritik/saran, lakukan pengiriman kritik/saran
        elif cmd == 'kritik_saran':
            sendFeedback(user, usermanager, attrmanager, feedmanager)

        # Jika fungsi lihat laporan, perlihatkan laporan
        elif cmd == 'lihat_laporan':
            listFeedback(user, feedmanager)

        # Jika tambah wahana, lakukan penambahan wahana
        elif cmd == 'tambah_wahana':
            createattraction(user, usermanager, attrmanager)
        
        # Jika fungsi top up, lakukan prosedur top up
        elif cmd == 'topup':
            topup(user, usermanager)

        # Jika fungsi adalah riwayat wahana, perlihatkan riwayat wahana
        elif cmd == 'riwayat_wahana':
            history(user, usermanager, attrmanager, usedmanager)

        # Untuk memperlihatkan jumlah tiket pemain
        elif cmd == 'tiket_pemain':
            showInventory(user, usermanager, attrmanager)
        
        # Untuk memperlihatkan best wahana
        elif cmd == 'best_wahana':
            bestwahana(attrmanager)

        # Fungsi untuk upgrade gold
        elif cmd == 'upgrade_gold':
            upgradegold(user, usermanager)

        # Jika fungsi tiket hilang, laporkan kehilangan tiket
        elif cmd == 'tiket_hilang':
            lostticket(user, usermanager, attrmanager, lostmanager, invtmanager)

        # Keluar
        elif cmd == 'exit':
            LS.keluar()
            break

        else: # tidak ditemukan
            print("Maaf, command tersebut tidak ditemukan.")
except KeyboardInterrupt: # Jika distop paksa dengan CTRL+C
    LS.keluar()