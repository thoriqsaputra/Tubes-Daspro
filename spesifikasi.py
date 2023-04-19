from function import addlist, makeshift_split, addlistmatrix
from typing import List
import os

userpassrole = ["" for i in range(102)] #deklarasi array of user data sesuai dengan template.
candi = ["" for i in range(100)] #deklarasi array of candi sesuai dengan template.
bahan_bagunan = ["" for i in range(3)] #deklarasi array of bahan bagunan sesuai dengan template.
undo_jin = [["",""] for i in range(100)] #deklarasi array of jin yang telah dihapus.

#masukin user data yang sudah ada ke array of user data.
userpassrole[0] = "Bondowoso;cintaroro;bandung_bondowoso"
userpassrole[1] = "Roro;gasukabondo;roro_jonggrang"


# def jin_in_undo(jinhapus):
#     indeksjin = 0
#     for i in range(100):
#         if undo_jin[i] == jinhapus:
#             undo_jin[i] = ""
#             indeksjin = i
#             break
#     for i in range(indeksjin+1,100):
#         undo_jin[i-1] = undo_jin[i]
        
def isuser(newuser: str) -> bool: # Cek apakah user baru ada atau tidak dalam data user.
    for i in range(102): # loop jumlah index data
        userlogin = makeshift_split(userpassrole[i], 3) # user data displit ke dalam array baru
        if newuser == userlogin[0]: # jika user baru ada maka return True
            return True
    return False # tidak terdapat maka False

def login(logged: List[str]) -> List[str]: # log in ke akun yang sudah dibuat.
    
    if logged[0] != "": # Apabila sudah ada yang login maka harus logout terlebih dahulu.
        print(f"Login gagal!\nAnda telah login dengan username {logged[0]}, silahkan lakukan “logout”\nsebelum melakukan login kembali.")
    
    else: # User belum login

        while True: # Dalam loop agar dapat diulang jika terjadi kesalahan.
            
            user = input("Username: ") # User disuruh input username dan password yang sudah dibuat.
            pa55 = input("Password: ")

            for i in range(102): # Cek apakah ada username dan password dalama array of user data.

                userlogin = makeshift_split(userpassrole[i],3) # Split user data dari template

                if user == userlogin[0] and pa55 == userlogin[1]: # Jika username dan password ada maka akan log in.
                    print(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                    logged = [userlogin[0],userlogin[2], True] # Array of logged information
                    return logged
                
                elif user == userlogin[0] and pa55 != userlogin[1]: #jika pasword salah
                    print("\nPassword salah!")
                    break
            else:
                print("Username tidak terdaftar!") #jika username tidak ada 

def logout(logged: List[str]) -> List[str]: # log out dari akun
    logged = ["","",False] # Array of logged information
    return logged

def summonjin(logged: List[str]) -> List[str]: # Summon jin oleh Bondowoso
    if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini.
    
        print("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")

        while True:  # Loop 1 menentukan role jin.

            jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ")) # Input jin yang mau dihapuskan.
            
            if jin == 1: # Memilih jin pengumpul. 
                rolejin = "jin_pengumpul" # Menyimpan dalam sebuah variabel.
                print("\nMemilih jin “Pengumpul”.\n")
                break
            elif jin == 2: # Memilih jin pembangun.
                rolejin = "jin_pembangun" # Menyimpan dalam sebuah variabel.
                print("\nMemilih jin “Pembangun”.\n")
                break
            else: # Selain dari jin pengumpul dan jin pembangun.
                print(f"\nTidak ada jenis jin bernomor “{jin}”!\n")

        while True: # Loop 2 menentukan username dan password jin.

            userjin = input("Masukkan username jin: ") # Input username jin.

            if isuser(userjin): # Cek apakah username jin sudah ada atau belum.
                print(f"Username “{userjin}” sudah diambil!")
                continue
            else:
                while True: # Loop 3 Menentukan password jin.
                    passjin = input("Masukkan password jin: ") # Input password jin.
                    print("\nPassword panjangnya harus 5-25 karakter!\n")
                    if not(5 <= len(passjin) <= 25): # Password harus sepanjang 5-25 kata.
                        continue
                    else:
                        for i in range(1000):
                            undojin = makeshift_split(undo_jin[i][0])
                            if undo_jin[i] == jin:
                                yesorno = input("Anda telah melakukan hapusjin dengan jin yang sama apakah mau ")

                         
                        addlist(userpassrole, f"{userjin};{passjin};{rolejin}",102) # Append data jin ke dalam array of user data.           
                        print(f"Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n\n{userjin} berhasil dipanggil!")
                        return
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")

def hapusjin(logged: List[str]) -> List[str]: # Menghilangkan Jin.

    if logged[1] == "bandung_bondowoso":  # Hanya Bondowoso yang dapat melakukan command ini.
        while True:

            jinhapus = input("Masukkan username jin : ")

            if isuser(jinhapus):
                while True: 
                    yesno = input(f"Apakah anda yakin ingin menghapus jin dengan username {jinhapus} (Y/N)? ")
                    if yesno == "Y":
                        for i in range(101):
                            userlogin = makeshift_split(userpassrole[i], 3)
                            if jinhapus == userlogin[0]:
                                addlistmatrix(undo_jin, jinhapus, 1000, 0)
                                userpassrole[i] = ""
                                print("\nJin telah berhasil dihapus dari alam gaib.")
                        return
                    elif yesno == "N":
                        break
                    else:
                        print("Pilih antara Y atau N.")

            else:
                print("Tidak ada jin dengan username tersebut.")
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")

def ubahjin(logged: List[str]) -> List[str]:
    if logged[1] == "bandung_bondowoso":
        namajin = input("Masukkan username jin: ")

        status = False 

        for i in range (102):
            userlogin = makeshift_split(userpassrole[i], 3)
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
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")   
         
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

    file_user = open(f"save/{folder_name}/user.csv","w")
    file_candi = open(f"save/{folder_name}/candi.csv","w")
    file_bahan_bangunan = open(f"save/{folder_name}/bahan_bangunan.csv","w")

    for i in range(102):
        file_user.write(f"{userpassrole[i]}\n")
    for i in range(100):
        file_candi.write(f"{candi[i]}\n")
    for i in range(3):
        file_bahan_bangunan.write(f"{bahan_bagunan[i]}\n")
    
    file_user.close()
    file_candi.close()
    file_bahan_bangunan.close()

# def undo():
