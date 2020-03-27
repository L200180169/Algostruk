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

#NOMER 3
def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
    
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini + 1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubblesort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                
def selectionsort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)

def insertionsort(A):
    n = len(A)
    for i in range(1 ,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1 ,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak=detak();print('Buble      : %g detik' %(ak-aw));
aw = detak();selectionsort(u_sel);ak=detak();print('Selection  : %g detik' %(ak-aw));
aw = detak();insertionsort(u_ins);ak=detak();print('Insertion  : %g detik' %(ak-aw));
