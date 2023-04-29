from typing import List

def addlist(lis: List[str], kata: str,lenght: int) -> List[str]:
    for i in range(lenght):
        if lis[i][0] == "":
            lis[i] = kata
            break
    return lis

def addlistmatrix(lis: List[str], kata: str,lenght: int, index:int) -> List[str]:
    for i in range(lenght):
        if lis[i][index] == "":
            lis[i] = kata
            break
    return lis

def makeshift_split(kata: str,lenght: int) -> List[str]:
    temp = "" #tempat sementara kata
    listbaru = ["" for i in range(lenght)] #list baru untuk string yang di split
    x = 0
    for i in range(len(kata)) : #dalam loop jika ada ",", " ", atau ";" maka akan dimasukan ke indeks pertama dst
        if kata[i] == " " or kata[i] == "," or kata[i] == ";" or kata[i] == "\n":
            listbaru[x] = temp
            x +=1
            temp = ""
        elif i == len(kata) - 1 : #khusus untuk huruf terakhir 
            temp += str(kata[i])
            listbaru[x] = temp
        else: #jika tidak yang lain maka akan dimasukan ke variabel temporary
            temp += str(kata[i])
    return listbaru
