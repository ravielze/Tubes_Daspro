from Utility.Array import panjangArray, elAdd

# Program Utilitas Encrypt Decrypt
# Last Update: 24 April 2020

# Deskripsi:
# Program ini berisikan fungsi-fungsi utilitas untuk mengacak dan menghash suatu text.

def encryptAlphabet(char, x):
    # Untuk huruf A-Z
    if ord(char) >= 65 and ord(char) <= 90:
        m = (ord(char)-65 + x) % 26
        return chr(65+m)
    # Untuk huruf a-z
    if ord(char) >= 97 and ord(char) <= 122:
        m = (ord(char)-97 + x) % 26
        return chr(97+m)
    # Untuk angka
    if ord(char) >= 48 and ord(char) <= 57:
        return (ord(char)-48 + x) % 10
    return char

def decryptAlphabet(char, x):
    # Untuk huruf A-Z
    if ord(char) >= 65 and ord(char) <= 90:
        m = ((ord(char)-65)+(26-x)) % 26
        return chr(65+m)
    # Untuk huruf a-z
    if ord(char) >= 97 and ord(char) <= 122:
        m = ((ord(char)-97)+(26-x)) % 26
        return chr(97+m)
    # Untuk angka
    if ord(char) >= 48 and ord(char) <= 57:
        return (ord(char)-48 + (10-x)) % 10
    return char


# Fungsi untuk memecah suatu string menjadi 3 bagian
# Contoh ganjil: makan menjadi ['ma', 'k', 'an']
# Contoh genap: lama menjadi ['la', None, 'ma']
# Asumsi string tidak kosong
def pecahbagian(string):
    if panjangArray(string) % 2 == 1: # ganjil
        midn = int(panjangArray(string)/2)+1
        head = string[0:(midn-1)]
        mid = string[midn-1]
        tail = string[midn:panjangArray(string)]
        return [head,mid,tail]
    else: # genap
        midn = int(panjangArray(string)/2)
        head = string[0:midn]
        tail = string[midn:panjangArray(string)]
        return [head,None,tail]

# Fungsi untuk untuk mengacak urutan suatu string
# berdasarkan panjang string
# pengacakan ada 3 jenis, panjang modulo 3 == 0,1,2
def acakurutan(string):
    s = panjangArray(string)
    if (s == 1):
        return string
    bagian = pecahbagian(string)
    result = ""
    if (s%3 == 0):
        if bagian[1] == None:
            return bagian[0] + bagian[2]
        else:
            return bagian[0] + bagian[2] + bagian[1]
    elif (s%3 == 1):
        if bagian[1] == None:
            return bagian[2] + bagian[0]
        else:
            return bagian[2] + bagian[0] + bagian[1]
    else:
        if bagian[1] == None:
            return bagian[2] + bagian[0]
        else:
            return bagian[2] + bagian[1] + bagian[0]

# Fungsi untuk menyusun ulang yang sudah diacak
def susunurutan(string):
    s = panjangArray(string)
    if s == 1:
        return string
    bagian = pecahbagian(string)
    if s%2 == 0:
        if (s%3 == 0):
            return string
        else:
            return bagian[2] + bagian[0]
    else:
        if (s%3 == 2):
            return bagian[2] + bagian[1] + bagian[0]
        mid = string[s-1]
        string = string[0:(s-1)]
        if (s%3 == 1):
            bagian = pecahbagian(string)
            return bagian[2] + mid + bagian[0]
        else:
            bagian = pecahbagian(string)
            return bagian[0] + mid + bagian[2]

# Fungsi yang bisa digunakan untuk modul lain dalam mengencrypt password
def Encrypt(string):
    isinteger = False
    if type(string) == int:
        string = str(string)
        isinteger = True
    acak = acakurutan(string)
    result = ""
    for i in range(panjangArray(acak)):
        result += str(encryptAlphabet(acak[i], int(1+(i^i)%5)))
    if isinteger is True:
        return "$!%" + result
    else:
        return result

# Fungsi yang bisa digunakan untuk modul lain dalam mengdecrypt password
def Decrypt(string):
    isinteger = False
    if string[0] == "$" and string[1] == "!" and string[2] == "%":
        string = string[3:panjangArray(string)]
        isinteger = True
    result = ""
    for i in range(panjangArray(string)):
        result += str(decryptAlphabet(string[i], int(1+(i^i)%5)))
    if isinteger:
        return int(susunurutan(result))
    else:
        return susunurutan(result)