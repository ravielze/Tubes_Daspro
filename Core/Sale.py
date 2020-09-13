from Utility.Array import panjangArray, cariArray
from Core.Attraction import Attraction, AttractionManager
from Core.Tickets import TicketManager

# Program Sinkronisasi Data Penjualan Wahana
# Last Update: 20 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk menyinkronkan data pembelian user dan refund user
# dengan data penjualan wahana pada awal program dijalankan.

def connect(attrmanager, bghtmanager, rfndmanager):
    attractionids = (attrmanager.getAttractions())[0]
    attractions = (attrmanager.getAttractions())[1]

    boughtdata = bghtmanager.get()
    if panjangArray(boughtdata) > 0:
        for x in boughtdata:
            idnumber = cariArray(x[2], attractionids) # mencari idwahana yang terdaftar di pembelian pada array id wahana
            if idnumber != None: # jika idnumber ditemukan
                (attractions[idnumber]).newSale(int(x[3])) # masukkan attraksi pada idnumber sebanyak data pembelian

    # Lakukan yang sama dengan refund hanya dibuat minus
    # karena pengurangan pembelian
    refunddata = rfndmanager.get()
    if panjangArray(refunddata) > 0:
        for x in refunddata:
            idnumber = cariArray(x[2], attractionids) # mencari idwahana yang terdaftar di pembelian pada array id wahana
            if idnumber != None: # jika idnumber ditemukan
                (attractions[idnumber]).newSale((-1)*int(x[3])) # masukkan attraksi pada idnumber sebanyak data pembelian