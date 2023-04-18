from function import musa, masukinae
from typing import List
import os

userpassrole = ["" for i in range(102)]
candi = ["" for i in range(100)]
bahan_bagunan = ["" for i in range(3)]
userpassrole[0] = "Bondowoso;cintaroro;bandung_bondowoso"
userpassrole[1] = "Roro;gasukabondo;roro_jonggrang"

def isuser(newuser: str) -> bool:
    for i in range(101):
        userlogin = musa(userpassrole[i], 3)
        if newuser == userlogin[0]:
            return True
    return False

def login(t: List[str]) -> List[str]:
    while True:

        user = input("Username: ")
        pa55 = input("Password: ")

        for i in range(102):

            userlogin = musa(userpassrole[i],3)

            if user == userlogin[0] and pa55 == userlogin[1]:
                print(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                t = userlogin[2]
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
                    masukinae(userpassrole, f"{userjin};{passjin};{rolejin}")            
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
                        userlogin = musa(userpassrole[i], 3)
                        if jinhapus == userlogin[0]:
                            userpassrole[i] = ""
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
        userlogin = musa(userpassrole[i], 3)
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
                userpassrole[index] = f"{userlogin[0]};{userlogin[1]};jin_pembangun"      
                print("Jin telah berhasil diubah.")
        else:
            opsi = input("Jin ini bertipe Pembangun. Yakin ingin mengubah tipe jin? (Y/N): ")
            if opsi == "Y":
                userpassrole[index] = f"{userlogin[0]};{userlogin[1]};jin_pengumpul"     
                print("Jin telah berhasil diubah.")
                
def save():
    folder_name = input("Masukkan Nama folder: ")
    
    if not os.path.exists(f"save/{folder_name}"):
        
        if not os.path.exists("save"):
            os.mkdir("save")
            os.mkdir(f"save/{folder_name}")
            print("\nSaving...\n")
        else:
            print(f"\nSaving...\n\nMembuat folder save/{folder_name}...\n\nBerhasil menyimpan data di folder save/{folder_name}!")
            os.mkdir(f"save/{folder_name}")

    else:
        print(f"\nSaving...\n\nBerhasil menyimpan data di folder save/{folder_name}!")

    file = open(f"save/{folder_name}/user.csv","w")
    
    for i in range(102):
        file.write(f"{userpassrole[i]}\n")
    for i in range(100):
        file.write(f"{candi[i]}\n")
    for i in range(3):
        file.write(f"{bahan_bagunan[i]}\n")
    
    file.close()
