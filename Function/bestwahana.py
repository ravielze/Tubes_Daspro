from Core.Attraction import Attraction, AttractionManager
from Utility.Array import elAdd, maksimalArray, panjangArray

# Program Best Wahana
# Last Update: 20 April 2020

# Deskripsi:
# Program ini berisi prosedur untuk memperlihatkan wahana dengan
# data penjualan terbanyak.

def bestwahana(attrmanager):

    attractionids = (attrmanager.getAttractions())[0]
    attractions = (attrmanager.getAttractions())[1]

    def getSaleArray():
        result = []
        for attr in attractions:
            result = elAdd(result, attr.getSale())
        return result
    
    def penamaan(nama):
        if panjangArray(nama) < 8:
            return nama + "\t\t"
        else:
            return nama + "\t"

    sales = getSaleArray()

    best1 = maksimalArray(sales)
    print(best1)
    if best1 == None: # best1 tidak ada sebab tidak ada wahana sama sekali
        print("Tidak ada wahana.")
    else: # best1 ada
        best2 = maksimalArray(sales, [best1]) # mencari nilai maksimal dengan mengabaikan index best1
        if best2 != None: # best2 ada
            best3 = maksimalArray(sales, [best1, best2]) # mencari nilai maksimal dengan mengabaikan index best1 dan best2

    print("Best Wahana")
    print("  | \tID Wahana\t | \tNama Wahana\t | \tPenjualan")
    if best1 != None:
        print(f"1 | \t{attractionids[best1]}\t\t | \t{penamaan(attractions[best1].getName())} | \t{sales[best1]}")
    if best2 != None:
        print(f"2 | \t{attractionids[best2]}\t\t | \t{penamaan(attractions[best2].getName())} | \t{sales[best2]}")
    if best3 != None:
        print(f"3 | \t{attractionids[best3]}\t\t | \t{penamaan(attractions[best3].getName())} | \t{sales[best3]}")