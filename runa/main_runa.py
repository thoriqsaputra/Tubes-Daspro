import os, argparse
from typing import List
# import module 

logged = ["", "", False] #deklarasi variable logged

#F05 Ubah Tipe Jin

def ubahjin(logged: List[str]) -> List[str]:
    if logged[1] == "bandung_bondowoso": #pengecekan login user, jika user adalah bandung bondowoso, fitur ubahjin dapat diakses.
        namajin = input("Masukkan username jin: ")

        status = False

        for i in range (102): #looping sesuai jumlah index data
            userlogin = makeshift_split(userpassrole[i], 3) #user data displit ke dalam array baru menggunakan fungsi bentukan sendiri
            if userlogin[0] == namajin: #setelah displit, jika userlogin[0] sama dengan masukan pada variable namajin, maka dipastikan username ada
                status = True #batasan pun berubah menjadi nilai True, dan akan lanjut ke command berikutnya
                index = i
                break

        if status == False: #jika batasan tetap bernilai False, maka dipastikan namajin != userlogin[0] atau jin tidak ada.
            print("Tidak ada jin dengan username tersebut.")
        else:
            if userlogin[2] == "Pengumpul": # pengecekan role jin yang di-input
                opsi = input("Jin ini bertipe Pengumpul. Yakin ingin mnengubah tipe jin? (Y/ N?): ")
                if opsi == "Y": #user memutuskan untuk mengganti tipe jin dari pengumpul menjadi pembangun
                    userpassrole[index] = f"{userlogin[0]};{userlogin[1]};jin_pembangun" #data pada file user.csv di-update 
                    print("Jin telah berhasil diubah.")
            else: #kondisional 2, jika jin yang dimasukkan bukan ga dateng blablabla
                opsi = input("Jin ini bertipe Pembangun. Yakin ingin mengubah tipe jin? (Y/N): ")
                if opsi == "Y":
                    userpassrole[index] = f"{userlogin[0]};{userlogin[1]};jin_pengumpul"     
                    print("Jin telah berhasil diubah.")
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")  #kondisi dimana user yang login bukan merupakan bandung bondowoso
        
        
#F05 Ubah Tipe Jin

#deklarasi argumen yang akan di-parsing
parser = argparse.ArgumentParser(description="Masukka Nama Folder")
parser.add_argument("path", nargs='?', type=str) #menerima input bertipe string & bersifat positional (parameter spesifik) -
args = parser.parse_args()                      # dan hanya menerima input 0 s/d 1 argument
dir = args.path

def cekPath(path): #pemanggilan prosedur untuk memvalidasi keberadaan folder yang di-input tersebut benar atau bukan
    pathtodata = f"save/{path}" #direktori tempat file disimpan dalam laptop 

    if args.path: #kondisional untuk mengecek apakah user memasukkan parameter seperti yang diminta atau tidak (kosong / no input)
        if not os.path.exists(os.path.join(pathtodata, path)): #menggabungkan parent directory dengan input user (variable path) dgn os.join
    
            if os.path.exists(args.path): #jika path yang diinput valid/exists dalam komputer maka menjalankan command berikutnya
                print(f"\nLoading...\n\nSelamat datang di program Manajerial Candi")
                print("Silakan masukkan username Anda")
                test = input(">>> ")
                while True: #loop dalam kondisi True agar user bisa login
                    List = [""]
                    if test.lower() != "": #menggunakan fungsi str.lower() agar input pengguna selalu valid tanpa peduli kapital
                        List = [""] #List kosong untuk menyimpan data setelah pemanggilan precedure login
                        login(List) #setelah user login, ada opsi untuk langsung exit atau mengecek command yg tersedia dengan "help"
                        exit() #keluar program jika user tidak memutuskan apapun
                    exit() 
                                   
            else: #kondisi jika input path berupa nama folder yang tidak tersedia
                print(f"Folder '{path}' tidak ditemukan.")
                exit()  # program keluar 
    else: 
        print("Tidak ada nama folder yang diberikan!\nUsage: python main.py <nama_folder>") #jika tidak menginput file apapun
        exit() #program keluar
           

#F16 Exit

def exit(): 
    check1 = True #batas awal untuk pengecekan apakah command berjalan sesuai / tidak
    while (check1 == True): #memasuki looping selama kondisi batas (check1 masih bernilai True)
        masukan = input(">>> ") #input command user
        check2 = True #penempatan batas untuk pengecekan kedua
        while check2 == True: #memasuki kondisi looping kedua selama nilai check2 masih True
            if (masukan.lower() == "exit"): #kondisi 1, apabila input user merupakan command "exit"
                validasi = str(input("""Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)
    """)) #input untuk memvalidasi pilihan pengguna, apakah mau men-save file yang sudah diupdate atau tidak
                if (validasi.lower()== "n" or validasi.lower()== "y"): #kondisi ke-2 untuk memastikan user hanya menginput nilai y dan n
                    if (validasi.lower()=="y"): #kondisi 3, jika user setuju untuk save sebelum melakukan exit
                        save() #memanggil procedure save
                        exit() #secara otomatis keluar program jika save berhasil
                    else:
                        check2 = False #batasan berubah nilai karena ada command yang tidak terpenuhi
                        exit() 
                elif not (validasi.lower()== "n" or validasi.lower()== "y"): #kondisional 
                    check2 = True #jika input pada saat validasi tidak sesuai, maka program akan terus looping 
                