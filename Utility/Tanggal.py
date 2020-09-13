# Program Utilitas Tanggal
# Last Update: 14 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi utilitas mengenai tanggal
# yang akan digunakan di modul-modul lain.

# Kamus Fungsi:
# kabisat(int tahun) -> boolean | Fungsi untuk mengecek apakah tahun kabisat/tidak
# hari(bulan, tahun) -> int | Fungsi untuk mendapatkan jumlah hari dalam suatu bulan, tahun
# selisih(array of integer ini, array of integer itu) -> int | Fungsi untuk mengecek jumlah hari dari tanggal ini ke itu

def kabisat(tahun):
    if tahun % 400 == 0:
        return True
    if tahun % 100 == 0:
        return False
    if tahun % 4 == 0:
        return True
    else:
        return False

def hari(bulan, tahun):
    if bulan <= 7:
        if bulan == 2 and kabisat(tahun):
            return 29
        elif bulan == 2:
            return 28
        if bulan % 2 == 0:
            return 30
        else:
            return 31
    else:
        if bulan % 2 == 0:
            return 31
        else:
            return 30

def selisihtgl(ini, itu):
    s = 0 # Anggap selisih 0

    # Jika tanggal ini lebih besar daripada itu, maka dibalik
    if ini[2] > itu[2]:
        return selisihtgl(itu, ini) 
    elif ini[2] == itu[2] and ini[1] > itu[1]:
        return selisihtgl(itu, ini)
    elif ini[1] == itu[1] and ini[0] > itu[0]:
        return selisihtgl(itu, ini)

    while (ini[0] != itu[0] or ini[1] != itu[1] or ini[2] != itu[2]): # Saat hari ini bukan hari itu
        ini[0] += 1 # maju satu hari
        
        if ini[0] > hari(ini[1],ini[2]): # jika hari sudah lewat dari jumlah hari di bulan ini
            ini[0] = 1 # balik ke tanggal 1
            ini[1] += 1 # tambah bulan sebanyak 1

        if ini[1] > 12: # jika bulan sudah lewat dari 12
            ini[1] = 1 # balik ke bulan 1
            ini[2] += 1 # tambah tahun sebanyak 1

        s += 1 # selisih bertambah satu setiap kali maju satu hari
    return s # mengembalikan nilai s
