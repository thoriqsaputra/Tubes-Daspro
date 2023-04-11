from function import musa
from function import masukinae

userdata = ["" for i in range(103)]

user_data = open("csv files/user.csv","r")
for baris in user_data:
    masukinae(userdata, baris)

def isuser(newuser):
    for i in range(102):
        userlogin = musa(userdata[i])
        if newuser == userlogin[0]:
            return True
    return False

def login():
    while True:
        user_data = open("csv files/user.csv","r")
        user = input("Username: ")
        pa55 = input("Password: ")

        for baris in user_data:
            userlogin = musa(baris)
            if user == userlogin[0] and pa55 == userlogin[1]:
                print(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                return
            elif user == userlogin[0] and pa55 != userlogin[1]:
                print("\nPassword salah!")
                break
        else:
            print("Username tidak terdaftar!")

def logout():
    logged = ""
    masuk = False
    return masuk, logged

def summonjin():
    print("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")
    while True:
        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        if jin == 1:
            rolejin = "jin_pengumpul"
            print("\nMemilih jin “Pengumpul”.\n")
            break
        elif jin == 2: 
            rolejin = "jin_pembangun"
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
                    masukinae(userdata, f"{userjin};{passjin};{rolejin}\n")            
                    print(f"Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n\n{userjin} berhasil dipanggil!")
                    return

def hapusjin():
    while True:
        jinhapus = input("Masukkan username jin : ")
        if isuser(jinhapus):
            while True: 
                yesno = input(f"Apakah anda yakin ingin menghapus jin dengan username {jinhapus} (Y/N)? ")
                if yesno == "Y":
                    for i in range(101):
                        userlogin = musa(userdata[i])
                        if jinhapus == userlogin[0]:
                            userdata[i] = ""
                            print("\nJin telah berhasil dihapus dari alam gaib.")
                    return
                elif yesno == "N":
                    break
                else:
                    print("Choose between Y or N for the following command.")

        else:
            print("Tidak ada jin dengan username tersebut.")
