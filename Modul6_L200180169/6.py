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

def quickSort(L, ascending = True): 
    quicksorthelp(L, 0, len(L), ascending)
    
def quicksorthelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += quicksorthelp(L, low, pivot_location, ascending)  
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low] 
    return i - 1, result

def median_of_three(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

print(daftar)
quickSort(daftar)
print(daftar)
