def panjang(a):
    e = 0
    for i in a:
        e += 1  
    return e  

def masukinae(lis, word):
    for i in range(101):
        if lis[i] == "":
            lis[i] = word
            break
    return lis

def musa(a):
    temp = "" #tempat sementara kata
    listbaru = ["a" for i in range(3)] #list baru untuk string yang di split
    x = 0
    for i in range(len(a)) : #dalam loop jika ada ",", " ", atau ";" maka akan dimasukan ke indeks pertama dst
        if a[i] == " " or a[i] == "," or a[i] == ";" or a[i] == "\n":
            listbaru[x] = temp
            x +=1
            temp = ""
        elif i == len(a) - 1 : #khusus untuk huruf terakhir 
            temp += str(a[i])
            listbaru[x] = temp
        else: #jika tidak yang lain maka akan dimasukan ke variabel temporary
            temp += str(a[i])
    return listbaru
