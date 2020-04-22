class MhsTIF (object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = MhsTif("Jainal", 10, "Sukoharjo", "informatika", 240000)
c1 = MhsTif("Fandit", 51, "Sragen", "informatika", 230000)
c2 = MhsTif("Diko", 2, "Surakarta", "informatika", 250000)
c3 = MhsTif("Ijul", 18, "Surakarta", "informatika", 235000)
c4 = MhsTif("Ghani", 4, "Boyolali", "informatika", 240000)
c5 = MhsTif("Rizki", 31, "Salatiga", "informatika", 250000)
c6 = MhsTif("Bagus", 13, "Klaten", "informatika", 245000)
c7 = MhsTif("Iqbal", 5, "Wonogiri", "informatika", 245000)
c8 = MhsTif("Khalid", 23, "Klaten", "informatika", 245000)
c9 = MhsTif("Azka", 64, "Karanganyar", "informatika", 270000)
c10 = MhsTif("Bima", 29, "Purwodadi", "informatika", 265000)

Daftar = [c0.NIM, c1.NIM, c2.NIM, c3.NIM, c4.NIM, c5.NIM, c6.NIM, c7.NIM, c8.NIM, c9.NIM, c10.NIM]

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i += 1
            else:
                A[k] = separuhKanan[j]
                j += 1
            k += 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i += 1
            k += 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j += 1
            k += 1

        return A

print(daftar)
mergeSort(daftar)
print(daftar)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)
    return A

print('\n')
print(daftar)
quickSort(daftar)
print(daftar)
