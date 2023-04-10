def panjang(a):
    e = 0
    for i in a:
        e += 1  
    return e  

def masukinae(lis, word):
    for i in range(panjang(lis)):
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

user = ["" for i in range(100)]
pa55 = ["" for i in range(100)]
role = ["" for i in range(100)]
user_data = open("csv files/user.csv","r")
for baris in user_data:
        userlogin = musa(baris)
        masukinae(user, userlogin[0])
        masukinae(pa55, userlogin[1])
        masukinae(role, userlogin[2])

def isuser(newuser):
    global user
    for i in range(10):
        if newuser == user[i]:
            return True
    return False

def login(t):
    while True:
        user_data = open("csv files/user.csv","r")
        user = input("Username: ")
        pa55 = input("Password: ")

        for baris in user_data:
            userlogin = musa(baris)
            if user == userlogin[0] and pa55 == userlogin[1]:
                print(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                t.append(userlogin[2])
                return t
            elif user == userlogin[0] and pa55 != userlogin[1]:
                print("\nPassword salah!")
                break
        else:
            print("Username tidak terdaftar!")

def summonjin():
    print("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")
    while True:
        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        if jin == 1:
            x = "jin_pengumpul"
            print("\nMemilih jin “Pengumpul”.\n")
            break
        elif jin == 2: 
            x = "jin_pembangun"
            print("\nMemilih jin “Pembangun”.\n")
            break
        else:
            print(f"\nTidak ada jenis jin bernomor “{jin}”!\n")
    while True:
        userjin = input("Masukkan username jin: ")
        if isuser(userjin):
            print(f"Username “{userjin}” sudah diambil!")
            continue
        else:
            while True:
                passjin = input("Masukkan password jin: ")
                print("\nPassword panjangnya harus 5-25 karakter!\n")
                if not(5 <= panjang(passjin) <= 25):
                    continue
                else:
                    print(userjin)
                    print(passjin)
                    print(x)
                    print(f"Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n\n{userjin} berhasil dipanggil!")

def hapusjin():

summon()





