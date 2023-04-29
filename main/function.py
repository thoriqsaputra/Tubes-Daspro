from typing import List
from spesifikasi import *

def jumlah_target (target, array, index) -> int: # menghitung jumlah variabel dari 1 kolom seperti "jin_pembangun" dari kolom role
    jumlah_variabel = 0
    for i in range(100):
        if array[i][index] == target:
            jumlah_variabel += 1
    return jumlah_variabel

def jumlah_column (column) -> int: # menghitung jumlah kolom yang terisi, selain None dan 0
    jumlah_data = 0
    for i in range(100):
        if column[i] != None and column[i] != 0:
            jumlah_data += 1
    return jumlah_data

def arr_target (target, array, column1, column2) -> list: # membuat suatu array yang berisi target dari 2 kolom,
    # contoh seperti array baru dari kolom role sebagain "jin_pembangun" yang berupa nama namanya dari kolom "username"
    arr_target = [None for i in range(jumlah_target (target, array, column2))]
    j = 0
    for i in range(100):
        if array[i][column2] == target:
            arr_target[j] = array[i][column1]
            j += 1
    return arr_target

def lcg_05(seed): # rng untuk 0 - 5
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a * x + c) % m
        yield x % 6  # menghasilkan nilai dari 0 sampai 5

def lcg_15(seed): # rng untuk 1 - 5
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a * x + c) % m
        yield (x % 5) + 1

def addlist(lis: List[str], kata: str,lenght: int) -> List[str]:
    for i in range(lenght):
        if lis[i] == "":
            lis[i] = kata
            break
    return lis

def addlistmatrix(lis: List[str], lenght: int, kolom: int, lisword: List[str]) -> List[str]:
    idx = 0
    for i in range(lenght):
        if lis[i][0] == "":
            idx = i
        for i in range(kolom):
            lis[idx][i] = lisword[i]
        return lis
    return("Sudah penuh")        

def makeshift_split(kata: str,lenght: int) -> List[str]:
    temp = "" #tempat sementara kata
    listbaru = ["" for i in range(lenght)] #list baru untuk string yang di split
    x = 0
    for i in range(len(kata)) : #dalam loop jika ada ",", "\n", atau ";" maka akan dimasukan ke indeks pertama dst
        if kata[i] == "," or kata[i] == ";" or kata[i] == "\n":
            listbaru[x] = temp
            x +=1
            temp = ""
        elif i == len(kata) - 1 : #khusus untuk huruf terakhir 
            temp += str(kata[i])
            listbaru[x] = temp
        else: #jika tidak yang lain maka akan dimasukan ke variabel temporary
            temp += str(kata[i])
    return listbaru

