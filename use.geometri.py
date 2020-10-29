#import geometri.segitiga
#print(f'luas segitiga cara #1: {geometri.segitiga.hitung_luas_segitiga(10, 5)}')
#import geometri.segitiga as gs
#print(f'luas segitiga cara #2: {gs.hitung_luas_segitiga(10, 5)}')
from geometri.persegipanjang import hitung_luas_persegipanjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
print(f'luas segitiga cara#3 : {hitung_luas_segitiga(10, 5)}')
print(info_persegipanjang())
print(f'luas persegi panjang : {hitung_luas_persegipanjang(10, 5)}')
