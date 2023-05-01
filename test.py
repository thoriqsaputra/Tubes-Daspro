
# def addlistmatrix(lis: List[str], kata: str,lenght: int) -> List[str]:
#     for i in range(lenght):
#         if lis[i][0] == "":
#             lis[i] = kata
#             break
#     return lis

# def makeshift_split(kata: str,lenght: int) -> List[str]:
#     temp = "" #tempat sementara kata
#     listbaru = ["" for i in range(lenght)] #list baru untuk string yang di split
#     x = 0
#     for i in range(len(kata)) : #dalam loop jika ada ",", " ", atau ";" maka akan dimasukan ke indeks pertama dst
#         if kata[i] == " " or kata[i] == "," or kata[i] == ";" or kata[i] == "\n":
#             listbaru[x] = temp
#             x +=1
#             temp = ""
#         elif i == len(kata) - 1 : #khusus untuk huruf terakhir 
#             temp += str(kata[i])
#             listbaru[x] = temp
#         else: #jika tidak yang lain maka akan dimasukan ke variabel temporary
#             temp += str(kata[i])
#     return listbaru

# # c = [["","",""] for i in range(10)]

# # # addlistmatrix(c, makeshift_split("batman is da best",4), 10)
# # # print(c)
# # userpassrole = [["","",""] for i in range(102)] # matrix berisi username, password, role  
# # userpassrole[0][0], userpassrole[0][1], userpassrole[0][2] = "Bondowoso", "cintaroro", "bandung_bondowoso"
# # userpassrole[1][0], userpassrole[1][1], userpassrole[1][2] = "Roro", "gasukabondo", "roro_jonggrang" 
# # logged = ["Bondowoso","bandung_bondowoso"]


# # def isuser(newuser: str) -> bool: # Cek apakah user baru ada atau tidak dalam data user.
# #     for i in range(102): # loop jumlah index data
# #         if newuser == userpassrole[i][0]: # jika user baru ada maka return True
# #             return True
# #     return False # tidak terdapat maka False

# # def summonjin(logged: List[str]) -> List[str]: # Summon jin oleh Bondowoso
# #     if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini.
    
# #         print("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")

# #         while True:  # Loop 1 menentukan role jin.

# #             jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ")) # Input jin yang mau dihapuskan.
            
# #             if jin == 1: # Memilih jin pengumpul. 
# #                 rolejin = "jin_pengumpul" # Menyimpan dalam sebuah variabel.
# #                 print("\nMemilih jin “Pengumpul”.\n")
# #                 break
# #             elif jin == 2: # Memilih jin pembangun.
# #                 rolejin = "jin_pembangun" # Menyimpan dalam sebuah variabel.
# #                 print("\nMemilih jin “Pembangun”.\n")
# #                 break
# #             else: # Selain dari jin pengumpul dan jin pembangun.
# #                 print(f"\nTidak ada jenis jin bernomor “{jin}”!\n")

# #         while True: # Loop 2 menentukan username dan password jin.

# #             userjin = input("Masukkan username jin: ") # Input username jin.

# #             if isuser(userjin): # Cek apakah username jin sudah ada atau belum.
# #                 print(f"Username “{userjin}” sudah diambil!")
# #                 continue
# #             else:
# #                 while True: # Loop 3 Menentukan password jin.
# #                     passjin = input("Masukkan password jin: ") # Input password jin.
# #                     print("\nPassword panjangnya harus 5-25 karakter!\n")
# #                     if not(5 <= len(passjin) <= 25): # Password harus sepanjang 5-25 kata.
# #                         continue
# #                     else:
# #                         index = function.indexMatrixKosong(userpassrole, 102, 1)
# #                         userpassrole[index][0], userpassrole[index][1], userpassrole[index][2] = userjin, passjin, rolejin
# #                         print(f"Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n\n{userjin} berhasil dipanggil!")
# #                         return
                    
# #     else:
# #         print("Hanya Bondowoso yang dapat mengakses command ini.")

# # def ubahjin(logged: List[str]) -> List[str]:

# #     if logged[1] == "bandung_bondowoso": #pengecekan login user, jika user adalah bandung bondowoso, fitur ubahjin dapat diakses.
        
# #         namajin = input("Masukkan username jin: ")
# #         status = False
# #         for i in range (102): #looping sesuai jumlah index data
# #             if userpassrole[i][0] == namajin: #setelah displit, jika userlogin[0] sama dengan masukan pada variable namajin, maka dipastikan username ada
# #                 status = True #batasan pun berubah menjadi nilai True, dan akan lanjut ke command berikutnya
# #                 index = i
# #                 break

# #         if status == False: #jika batasan tetap bernilai False, maka dipastikan namajin != userlogin[0] atau jin tidak ada.
# #             print("Tidak ada jin dengan username tersebut.")
# #         else:
# #             if userpassrole[index][2] == "jin_pengumpul": # pengecekan role jin yang di-input
# #                 opsi = input("Jin ini bertipe Pengumpul. Yakin ingin mnengubah tipe jin? (Y/ N?): ")
# #                 if opsi == "Y": #user memutuskan untuk mengganti tipe jin dari pengumpul menjadi pembangun
# #                     userpassrole[index][2] = "jin_pembangun"  #data pada file user.csv di-update 
# #                     print("Jin telah berhasil diubah.")
# #             else: #kondisional 2, jika jin yang dimasukkan bukan ga dateng blablabla
# #                 opsi = input("Jin ini bertipe Pembangun. Yakin ingin mengubah tipe jin? (Y/N): ")
# #                 if opsi == "Y":
# #                     userpassrole[index][2] = "jin_pengumpul"     
# #                     print("Jin telah berhasil diubah.")
# #     else:
# #         print("Hanya Bondowoso yang dapat mengakses command ini.")  #kondisi dimana user yang login bukan merupakan bandung bondowoso

# # summonjin(logged)
# # ubahjin(logged)
# import time
# # print(userpassrole)
# # rng_05 = next(function.lcg_05(int(time.time() * 1000000)))
# # rng_15 = next(function.lcg_15(int(time.time() * 1000000)))

# # print(rng_05)
# # print(rng_05)
# # print(rng_05)
# # print(rng_05)

# candii = """
#          ▄▄
#          ██
#         ,██;
#       ,█▄▄▄▄█,
#       █"⌐-]'╓█
#      ▄█▄▄▄▄▄▄█▄
#   ╒▄█▌▄▄▄▄▄▄▄▄▄█▄⌐
#   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
#  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# """
# for i in range (len(candii)):
#     print(candii[i], end="", flush=True)
#     time.sleep(0.02)
# print("B")
# import time
# message1 = """
#                     ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
#                     ───█▒▒░░░░░░░░░▒▒█───
#                     ────█░░█░░░░░█░░█────
#                     ─▄▄──█░░░▀█▀░░░█──▄▄─
#                     █░░█─▀▄░░░░░░░▄▀─█░░█
#                     █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
#                     █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
#                     █░░║║║╠─║─║─║║║║║╠─░░█
#                     █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
# """
# message2 = "Permainan dimulai! gunakan command 'help' untuk melihat daftar command yang ada.\n"

# for i in range(len(message1)):
#     print(message1[i], end='', flush=True)
#     if message1[i] != " ":
#         time.sleep(0.009)
# for i in range(len(message2)):
#     print(message2[i], end='', flush=True )
#     time.sleep(0.03)

# from typing import List
# o = [["","",""] for i in range(2)]
# o[0][0] = "23"
# def addlistmatrix(lis: List[str], lenght: int, kolom: int, lisword: List[str]) -> List[str]:
#     idx = 0
#     for i in range(lenght):
#         if lis[i][0] == "":
#             idx = i
#             break
#         else:
#             return("Sudah penuh")   
#     for i in range(kolom):
#         lis[idx][i] = lisword[i]
#     return lis
# print(o)
# addlistmatrix(o, 2, 3, ["2","3","5"])
# from typing import List
# # print(o)
# userpassrole = [["2","2","2"] for i in range(102)] # matrix berisi [username, password, role]

# userpassrole[0][0], userpassrole[0][1], userpassrole[0][2] = "Bondowoso", "cintaroro", "jin_pembangun"
# userpassrole[1][0], userpassrole[1][1], userpassrole[1][2] = "Bondowoso", "cintaroro", "jin_pembangun"
# userpassrole[2][0], userpassrole[2][1], userpassrole[2][2] = "Bondowoso", "cintaroro", "jin_pembangun"
# userpassrole[3][0], userpassrole[3][1], userpassrole[3][2] = "Bondowoso", "cintaroro", "jin_pembangun"

# def addlistmatrix(lis: List[str], lenght: int, kolom: int, lisword: List[str]) -> List[str]:
#     idx = 0
#     for i in range(lenght):
#         if lis[i][0] == "":
#             idx = i
#             break
#     else:
#         return("Sudah penuh")  
    
#     for i in range(kolom):
#         lis[idx][i] = lisword[i]
#     return lis
# print(addlistmatrix(userpassrole, 102, 3, [1,2,3]))
# id = [0 for i in range(1000)] # array file csv candi kolom id
# pembuat = ["" for i in range(1000)] # array file csv candi kolom pembuat
# pasir = ["" for i in range(1000)] # array file csv candi kolom pasir
# batu = ["" for i in range(1000)] # array file csv candi kolom batu
# air = ["" for i in range(1000)]

# id[0] = 0

# import spesifikasi
# logged = ["bandung_bondowoso","roro_jonggrang"]

# spesifikasi.hancurkancandi(logged)


# bahan_bangunan = [["","",0] for i in range(3)] # matrix bahan bangunan [nama, deskripsi, jumlah]
# gg = [["batman",""] for i in range(100)]
# # print(bahan_bangunan[0][2])
# a = [["",0] for i in range(100)]

# for i in range(100):
#     if i == 2:
#         break
userpassrole = [["","",""] for i in range(102)] # matrix berisi [username, password, role]
userpassrole[0][0] = "dffdf"
userpassrole[1][0] = "dffdf"
# print(i)
import function
def batchsummon():
    # if logged[1] == "bandung_bondowoso":
        banyakjin = int(input("Banyak jin yang ingin disummon: "))
        jumlah_jin = function.jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)
        print(jumlah_jin)
        if jumlah_jin + banyakjin > 100:
            print("Summon gagal! Anda melebihi batas maks summonjin.")
            return
        
        else:
            print("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")

            while True:  # Loop 1 menentukan role jin.

                jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ") # Input jin yang mau dihapuskan.
                
                if jin == "1": # Memilih jin pengumpul. 
                    rolejin = "jin_pengumpul" # Menyimpan dalam sebuah variabel.
                    print("\nMemilih jin “Pengumpul”.\n")
                    break
                elif jin == "2": # Memilih jin pembangun.
                    rolejin = "jin_pembangun" # Menyimpan dalam sebuah variabel.
                    print("\nMemilih jin “Pembangun”.\n")
                    break
                else: # Selain dari jin pengumpul dan jin pembangun.
                    print(f"\nTidak ada jenis jin bernomor “{jin}”!\n")
            
            for i in range(banyakjin):
                numba = 1
                for i in range(102):
                    if f"userjin{numba}" != userpassrole[i][0]:
                        numba = numba
                    else:
                        numba +=1
                userjin = f"userjin{numba}"
                passjin = f"passjin{numba}"
                function.addlistmatrix(userpassrole, 102, 3, [userjin,passjin,rolejin])
            print("\nMengumpulkan sesajen", end="")
            # for i in range(3):
            #     print(".", end="", flush=True)
            #     time.sleep(0.4)
            # print("\nMenyerahkan sesajen", end="")
            # for i in range(3):
            #     print(".", end="", flush=True)
            #     time.sleep(0.4)
            # print("\nMembacakan mantra", end="")
            # for i in range(3):
            #     print(".", end="", flush=True)
            #     time.sleep(0.4)
            # print(f"\n{userjin} berhasil dipanggil!")
            # return
    # else:
    #     print("Hanya Bondowoso yang dapat mengakses command ini.")
# for i in range(3):
batchsummon()
print(userpassrole)