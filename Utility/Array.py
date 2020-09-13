# Program Utilitas Array
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi utilitas array yang akan digunakan
# di modul-modul lain.

# Kamus Fungsi:

# panjangArray(array) -> int | untuk mencari panjang array
# cariArray(Apapun tetapi harus setipe dengan element idarray idcari, array of string idarray) -> index
#     Catatan: untuk mencari indexnya hanya dibutuhkan 2 parameter
#              kalau 3 parameter akan seperti dibawah ini
# cariArray(Apapun tetapi harus setipe dengan element idarray idcari, array of string idarray, array of apapun array) 
#                -> hasil dari array ke n dimana n adalah index dari idcari di array idarray
#     Catatan: digunakan untuk mencari
#              misal ada ID = ['001', '002', '003'] dan berhubungan dengan array umur = [17,19,18]
#              untuk mendapatkan umur dengan ID 002 maka digunakan cariArray("002", ID, umur)
#              mengembalikan None saat tidak ada yang dikembalikan
# elAdd(object array, object sesuatu) -> Array
#     Catatan: pengganti append
#              menggabungkan 2 array atau 1 array dengan 1 object apapun (int/string/float/dll.)
# maksimalArray(array of integer, array exclude=[]) -> int | untuk mencari nilai maksimal suatu array, mengembalikan index
#     Catatan:
#              exclude adalah indeks-indeks yang diabaikan guna untuk mencari maksimal ke 2 atau ke 3 atau ke-n
#              exclude bisa dibiarkan kosong/opsional

# Realisasi
def panjangArray(array):
    result = 0 # Anggap array memiliki panjang 0
    for element in array:
        result += 1 # Bertambah selalu setiap ada elemen pada array
    return result # Mengembalikan panjang array

def cariArray(idcari, idarray, array=None):
    if (array != None):
        for i in range(panjangArray(idarray)):
            if idcari == idarray[i]: # saat idcari == idarray
                return array[i]      # return hasil dari array dengan index ke-i
        return None # mengembalikan None jika tidak ditemukan idcari pada array idarray
    else:
        for i in range(panjangArray(idarray)):
            if idcari == idarray[i]: # saat idcari == idarray
                return i      # return hasil dari array dengan index ke-i
        return None # mengembalikan None jika tidak ditemukan idcari pada array idarray

def elAdd(array, tail):
    return array + [tail]

def maksimalArray(array, exclude=[]):
    i = None # Jika array kosong, akan mengembalikan None

    if (panjangArray(array)-panjangArray(exclude) > 0): # Matrix harus memiliki isi
        nilai = -9999999999999 #anggap nilai adalah negatif tak hingga
        i = 0

        for x in range(panjangArray(array)):
            if x in exclude: #Jika x adalah index yang diabaikan
                continue
            if array[x] > nilai:
                nilai = array[x]
                i = x
    return i # akan mengembalikan -1 jika matrix kosong, 
             # akan mengembalikan index jika ada nilai maxnya