from function import musa
from function import masukinae
from function import panjang

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



