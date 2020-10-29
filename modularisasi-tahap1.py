"""
Menghitung luas segitiga
"""

alas = 10
tinggi = 5
luas_segitiga = alas * tinggi / 2
print(f'luas segitiga dengan alas = {alas}, dan tinggi = {tinggi} sehingga luasnya = {luas_segitiga}')

print('\nMembuat dengan fungsi')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


print(f'luas segitiga yaitu {hitung_luas_segitiga(10, 6)}')
