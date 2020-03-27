class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')
        
Daftar = [MhsTif("Jainal", 10, "Sukoharjo", 240000),
MhsTif("Fandit", 51, "Sragen", 230000),
MhsTif("Diko", 2, "Surakarta", 250000),
MhsTif("Ijul", 18, "Surakarta", 235000),
MhsTif("Ghani", 4, "Boyolali", 240000),
MhsTif("Rizki", 31, "Salatiga", 250000),
MhsTif("Bagus", 13, "Klaten", 245000),
MhsTif("Iqbal", 5, "Wonogiri", 245000),
MhsTif("Khalid", 23, "Klaten", 245000),
MhsTif("Azka", 64, "Karanganyar", 270000),
MhsTif("Bima", 29, "Purwodadi", 265000)]

#NOMER 1
def ceknim (d):
    for i in d :
        print (i.NIM)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urutnim(d):
    n = len(d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k].NIM > d[k+1].NIM :
                swap(d,k,k+1)
##cara menampilkan
##urutnim(Daftar)
##ceknim(Daftar)
                



