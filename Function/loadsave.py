from Core.User import UserManager
from Core.Attraction import AttractionManager
from Core.Feedback import FeedbackManager
from Core.Tickets import TicketManager
from Core.Inventory import InventoryManager
from Utility.Array import panjangArray
from Core.Sale import connect

# Program LoadSave
# Last Update: 15 April 2020

# Deskripsi:
# Program ini berisi prosedur dan fungsi untuk load, save dan keluar
# Variable usermanager, attrmanager, usedmanager, invtmanager, rfndmanager
# lostmanager, bghtmanager, dan feedmanager pada file ini akan dipakai oleh
# file Main

# Inisiasi Global Variabel
usermanager = None
attrmanager = None
usedmanager = None
invtmanager = None
rfndmanager = None
lostmanager = None
bghtmanager = None
feedmanager = None
# Akan terisi setelah di load

# Prosedur Keluar
# Digunakan saat ingin keluar
# Ditanyakan ingin save/tidak
# Jawaban berupa Y/N
def keluar():
    o = 'x'
    while (o != 'Y' and o != 'N'):
        o = input("\nApakah anda mau menyimpan file yang sudah dilakukan (Y/N)?\n$ ").upper()
    if o == 'Y':
        save()
    print("\n\n\n")

# Fungsi namaFile
# textinput         : String
# default           : String
# Fungsi ini digunakan untuk membuat nama file hanya bisa karakter tertentu
# Dan memperbolehkan user menginput '~' saja
# Jika input hanya berupa '~' saja, maka nama file akan menjadi default
def namaFile(textinput, default=None):
    nama = (input(textinput)).lower()
    if nama == '~' and default != None:
        return default
    nama = nama.replace(".csv", "")
    for i in range(panjangArray(nama)):
        if ord(nama[i]) >= 97 and ord(nama[i]) <= 122:
            continue
        if ord(nama[i]) >= 48 and ord(nama[i]) <= 57:
            continue
        if ord(nama[i]) in [33, 35, 36, 37, 38, 40, 41, 42, 43, 45, 47, 60, 61, 62, 63, 64, 124, 126, 95]:
            continue
        nama[i] = '_'
    return nama

# Prosedur Load
# Prosedur ini untuk load data
def load():
    global usermanager, attrmanager, bghtmanager, usedmanager, invtmanager, rfndmanager, feedmanager, lostmanager

    usermanager = UserManager(namaFile("Masukkan nama File User\t\t\t\t: ", 'user'))
    usermanager.load()

    attrmanager = AttractionManager(namaFile("Masukkan nama File Daftar Wahana\t\t: ", 'wahana'))
    attrmanager.load()

    bghtmanager = TicketManager(namaFile("Masukkan nama File Pembelian Tiket\t\t: ", 'pembelian'))
    bghtmanager.load()
    
    usedmanager = TicketManager(namaFile("Masukkan nama File Penggunaan Tiket\t\t: ", 'penggunaan'))
    usedmanager.load()
    
    invtmanager = InventoryManager(attrmanager, usermanager, namaFile("Masukkan nama File Kepemilikan Tiket\t\t: ", 'tiket'))
    invtmanager.load()
    
    rfndmanager = TicketManager(namaFile("Masukkan nama File Refund Tiket\t\t\t: ", 'refund'))
    rfndmanager.load()
    
    feedmanager = FeedbackManager(namaFile("Masukkan nama File Kritik dan Saran\t\t: ", 'kritiksaran'))
    feedmanager.load()

    lostmanager = TicketManager(namaFile("Masukkan nama File Kehilangan Tiket\t\t: ", 'kehilangan'))
    lostmanager.load()
    
    connect(attrmanager, bghtmanager, rfndmanager) # Sinkronisasi data pembelian dan refund dengan data penjualan tiap wahana
    print("File perusahaan Willy Wangky's Chocolate Factory telah dimuat.")

# Prosedur save
# Fungsi untuk melakukan save
# default adalah nama file dimana akan disave
def save():
    global usermanager, attrmanager, bghtmanager, usedmanager, invtmanager, rfndmanager, feedmanager, lostmanager

    usermanager.changeFilename(namaFile("Masukkan nama File User\t\t\t\t: ", 'user'))
    usermanager.save()

    attrmanager.changeFilename(namaFile("Masukkan nama File Daftar Wahana\t\t: ", 'wahana'))
    attrmanager.save()

    bghtmanager.changeFilename(namaFile("Masukkan nama File Pembelian Tiket\t\t: ", 'pembelian'))
    bghtmanager.save()
    
    usedmanager.changeFilename(namaFile("Masukkan nama File Penggunaan Tiket\t\t: ", 'penggunaan'))
    usedmanager.save()
    
    invtmanager.changeFilename(namaFile("Masukkan nama File Kepemilikan Tiket\t\t: ", 'tiket'))
    invtmanager.save()
    
    rfndmanager.changeFilename(namaFile("Masukkan nama File Refund Tiket\t\t\t: ", 'refund'))
    rfndmanager.save()
    
    feedmanager.changeFilename(namaFile("Masukkan nama File Kritik dan Saran\t\t: ", 'kritiksaran'))
    feedmanager.save()

    lostmanager.changeFilename(namaFile("Masukkan nama File Kehilangan Tiket\t\t: ", 'kehilangan'))
    lostmanager.save()
    print("File perusahaan Willy Wangky's Chocolate Factory telah disimpan.")