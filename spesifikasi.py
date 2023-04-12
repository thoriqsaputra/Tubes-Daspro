from function import musa
from function import masukinae
from typing import List

userdata = ["" for i in range(103)]
user_data = open("csv files/user.csv","r")
for baris in user_data:
    masukinae(userdata, baris)

def isuser(newuser: str) -> bool:
    for i in range(102):
        userlogin = musa(userdata[i], 3)
        if newuser == userlogin[0]:
            return True
    return False

def login(t: List[str]) -> List[str]:
    while True:
        user_data = open("csv files/user.csv","r")
        user = input("Username: ")
        pa55 = input("Password: ")

        for baris in user_data:
            userlogin = musa(baris,3)
            if user == userlogin[0] and pa55 == userlogin[1]:
                print(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                t = userlogin[0]
                return t
            elif user == userlogin[0] and pa55 != userlogin[1]:
                print("\nPassword salah!")
                break
        else:
            print("Username tidak terdaftar!")

def logout(l: str) -> str:
    l = ""
    return l

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
                if not(5 <= len(passjin) <= 25):
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
                        userlogin = musa(userdata[i], 3)
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

def ubahjin():
    namajin = input("Masukkan username jin: ")
    status = False 
    for i in range (102):
        userlogin = musa(userdata[i], 3)
        if userlogin[0] == namajin:
            status = True
            index = i
            break
    if status == False:
        print("Tidak ada jin dengan username tersebut.")
    else:
        if userlogin[2] == "Pengumpul":
            opsi = input("Jin ini bertipe Pengumpul. Yakin ingin mnengubah tipe jin? (Y/ N?): ")
            if opsi == "Y":
                userdata[index] = f"{userlogin[0]};{userlogin[1]};jin_pembangun\n"      
                print("Jin telah berhasil diubah.")
        else:
            opsi = input("Jin ini bertipe Pembangun. Yakin ingin mengubah tipe jin? (Y/N): ")
            if opsi == "Y":
                userdata[index] = f"{userlogin[0]};{userlogin[1]};jin_pengumpul\n"     
                print("Jin telah berhasil diubah.")
                