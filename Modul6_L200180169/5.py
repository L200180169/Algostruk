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

def _merge_sort(indices, the_list):
    start = indices[0]
    end = indices[1]
    half_way = (end - start) // 2 + start
    
    if start < half_way:
        _merge_sort((start, half_way), the_list)

    if half_way + 1 <= end and end - start != 1:
       _merge_sort((half_way + 1, end), the_list)

    sort_sub_list(the_list, indices[0], indices[1])
    
    return the_list
    
    
def sort_sub_list(the_list, start, end):
    orig_start = start
    initial_start_second_list = (end - start)//2 + start + 1
    list2_first_index = initial_start_second_list
    new_list = []
    
    while start < initial_start_second_list and list2_first_index <= end:
        first1 = the_list[start]
        first2 = the_list[list2_first_index]
        if first1 > first2:
            new_list.append(first2)
            list2_first_index += 1
        else:
            new_list.append(first1)
            start += 1
            
    while start < initial_start_second_list:
        new_list.append(the_list[start])
        start += 1

    while list2_first_index <= end:
        new_list.append(the_list[list2_first_index])
        list2_first_index += 1
        
    for i in new_list:
        the_list[orig_start] = i
        orig_start += 1
        
    return the_list

def mergeSort(the_list):
    return _merge_sort((0, len(the_list) - 1), the_list)

print(daftar)
mergeSort(daftar)
print(daftar)
