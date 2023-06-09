# Import module yang dibutuhkan
import function, time, os
from typing import List

# Deklarasi array/matrix untuk menyimpan data permainan.
userpassrole = [["","",""] for i in range(102)] # matrix berisi [username, password, role]
id = ["" for i in range(1000)] # array file csv candi kolom id
pembuat = ["" for i in range(1000)] # array file csv candi kolom pembuat
pasir = ["" for i in range(1000)] # array file csv candi kolom pasir
batu = ["" for i in range(1000)] # array file csv candi kolom batu
air = ["" for i in range(1000)] # array file csv candi kolom air
bahan_bangunan = [["", "", 0] for i in range(3)] # matrix bahan bangunan [nama, deskripsi, jumlah]

# Varibael yang dibutuhkan dalam game
arr_jin_pembangun = function.arr_target("jin_pembangun", userpassrole, 0, 2) # Membuat array berisi jin pembangun
jumlah_jin_pengumpul = 0 # jumlah jin pengumpul
jumlah_jin_pembangun = 0 # jumlah jin pembangun
jumlah_jin = 0 # jumlah jin pembangun
jumlah_pembuat = 0 # jumlah jin yang sudah membangun candi
jumlah_id = 0 # jumlah id
# Untuk ngerandom angka yang didapatkan
seed_value = int(time.time()* 1000000) 
rng_05 = function.lcg_05(seed_value)
rng_15 = function.lcg_15(seed_value)

# F01 Login
def login(logged: List[str]) -> List[str]: # login ke akun yang sudah dibuat.
    if logged[0] != "": # Apabila sudah ada yang login maka harus logout terlebih dahulu.
        print(f"Login gagal!\nAnda telah login dengan username {logged[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        return logged
    else: # User belum login

        while True: # Dalam loop agar dapat diulang jika terjadi kesalahan.
            
            user = input("Username: ") # User disuruh input username dan password yang sudah dibuat.
            pa55 = input("Password: ")
            if user == "" or user == "":
                print("\nInput salah!\n")
                continue
            for i in range(102): # Cek apakah ada username dan password dalama array of user data.
                
                if user == userpassrole[i][0] and pa55 == userpassrole[i][1]: # Jika username dan password ada maka akan log in.
                    print(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                    logged = [userpassrole[i][0],userpassrole[i][2]] # Array of logged information
                    return logged
                
                elif user == userpassrole[i][0] and pa55 != userpassrole[i][1]: #jika pasword salah
                    print("\nPassword salah!")
                    return logged
            else:
                print("\nUsername tidak terdaftar!") #jika username tidak ada 
                return logged

# F02 Logout
def logout(logged: List[str]) -> List[str]: # log out dari akun
    if logged[1] == "": # Jika belum ada yang login
        print("\nLogout gagal!\n\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return logged
    else:
        logged = ["",""] # Array of logged information
        print("\nLogout berhasil!")
        return logged

# F03 Summon Jin
def summonjin(logged: List[str]) -> List[str]: # Summon jin oleh Bondowoso
    if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini.
        
        jumlah_jin = function.jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)

        if jumlah_jin >= 100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
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

            while True: # Loop 2 menentukan username dan password jin.
                userjin = input("Masukkan username jin: ") # Input username jin.
                if userjin == "":
                    print("\nTry again.\n")
                    continue
                for i in range(102): # loop jumlah index data
                    if userjin == userpassrole[i][0]: # jika user baru ada maka return True
                        print(f"\nUsername “{userjin}” sudah diambil!")
                        break

                else: # username belum ada
                    while True: # Loop 3 Menentukan password jin.
                        passjin = input("Masukkan password jin: ") # Input password jin.
                        if not(5 <= len(passjin) <= 25): # Password harus sepanjang 5-25 kata.
                            print("\nPassword panjangnya harus 5-25 karakter!\n")
                            continue
                        else:
                            function.addlistmatrix(userpassrole, 102, 3, [userjin,passjin,rolejin])
                            print("\nMengumpulkan sesajen", end="")
                            for i in range(3):
                                print(".", end="", flush=True)
                                time.sleep(0.4)
                            print("\nMenyerahkan sesajen", end="")
                            for i in range(3):
                                print(".", end="", flush=True)
                                time.sleep(0.4)
                            print("\nMembacakan mantra", end="")
                            for i in range(3):
                                print(".", end="", flush=True)
                                time.sleep(0.4)
                            print(f"\n\nJin {userjin} berhasil dipanggil!")
                            return
                    
    else:
        print("\nHanya Bandung Bondowoso yang dapat mengakses command ini.")

# F04 Hilangkan Jin
def hapusjin(logged: List[str]) -> List[str]: # Menghilangkan Jin.  
    if logged[1] == "bandung_bondowoso":  # Hanya Bondowoso yang dapat melakukan command ini.

        jinhapus = input("\nMasukkan username jin : ") # Input username jin.

        for i in range(2, 102): # loop jumlah index data
            if jinhapus == userpassrole[i][0]: # jika user baru ada maka return True
                while True: 
                    # User disuruh input antara Y atau N dalam penghapusan jin.
                    yesno = input(f"Apakah anda yakin ingin menghapus jin dengan username {jinhapus} (Y/N)? ")
                    if yesno == "Y" or yesno == "y": #jika iya maka akan di hapus
                        for i in range(102):
                            if jinhapus == userpassrole[i][0]:
                                userpassrole[i] = ["","",""] # diubah jadi ""
                                print("\nJin telah berhasil dihapus dari alam gaib.")
                        for i in range(1000): # menghapuskan candi yang telah di bangun.
                            if jinhapus == pembuat[i]:
                                id[i] = ""
                                pembuat[i] = ""
                                pasir[i] = ""
                                batu[i] = ""
                                air[i] = ""
                        return
                    
                    elif yesno == "N" or yesno == "n": # Jika tidak, maka akan keluar dari bagian ini.
                        print("\nJin tidak jadi dihapus.")                        
                        return
                    else:
                        print("\nPilih antara Y atau N.\n")
        else:
            print("\nTidak ada jin dengan username tersebut.")
    else:
        print("\nHanya Bandung Bondowoso yang dapat mengakses command ini.")

# F05 Ubah Tipe Jin
def ubahjin(logged: List[str]) -> List[str]:
    if logged[1] == "bandung_bondowoso": #pengecekan login user, jika user adalah bandung bondowoso, fitur ubahjin dapat diakses.
        namajin = input("\nMasukkan username jin: ")
        status = False
        for i in range (2, 102): #looping sesuai jumlah index data
            if userpassrole[i][0] == namajin: #jika userpassrole[i][0] sama dengan masukan pada variable namajin, maka dipastikan username ada
                status = True #batasan pun berubah menjadi nilai True, dan akan lanjut ke command berikutnya
                index = i
                break
        if status == False: #jika batasan tetap bernilai False, maka dipastikan namajin != userlogin[0] atau jin tidak ada.
            print("\nTidak ada jin dengan username tersebut.\n")
        else:
            if userpassrole[index][2] == "jin_pengumpul": # pengecekan role jin yang di-input
                opsi = input("\nJin ini bertipe Pengumpul. Yakin ingin mnengubah tipe jin? (Y/ N?): ")
                if opsi == "Y": #user memutuskan untuk mengganti tipe jin dari pengumpul menjadi pembangun
                    userpassrole[index][2] = "jin_pembangun"  #data pada file user.csv di-update 
                    print("\nJin telah berhasil diubah.")
                elif opsi == "N":
                    print("\nJin tidak jadi diubah.")
                else:
                    print("\nPilih antara Y atau N.\n")
            else: #kondisional 2, jika jin yang dimasukkan bukan ga dateng blablabla
                opsi = input("Jin ini bertipe Pembangun. Yakin ingin mengubah tipe jin? (Y/N): ")
                if opsi == "Y":
                    userpassrole[index][2] = "jin_pengumpul"     
                    print("\nJin telah berhasil diubah.")
                elif opsi == "N":
                    print("\nJin tidak jadi diubah.")
                else:
                    print("\nPilih antara Y atau N.\n")
    else:
        print("\nHanya Bandung Bondowoso yang dapat mengakses command ini.")  #kondisi dimana user yang login bukan merupakan bandung bondowoso

# F06 Jin Pembangun
def bangun(logged: List[str]):
    if logged[1] == "jin_pembangun": # Hanya role Jin Pembangun yang dapat menggunakan command ini 

        butuh_pasir = next(rng_15) # Untuk menentukan berapa banyak pasir yang dibutuhkan untuk membangun satu candi
        butuh_batu = next(rng_15) # Untuk menentukan berapa banyak batu yang dibutuhkan untuk membangun satu candi
        butuh_air = next(rng_15) # Untuk menentukan berapa banyak air yang dibutuhkan untuk membangun satu candi
       
        if butuh_pasir > bahan_bangunan[0][2] or butuh_batu > bahan_bangunan[1][2] or butuh_air > bahan_bangunan[2][2]: # Apabila salah satu dari pasir, batu, dan air yang dibutuhkan lebih banyak dari yang dimiliki, maka candi tidak bisa dibangun
            print("\nBahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")

        else:
            candii = """
         ▄▄
         ██
        ,██;
      ,█▄▄▄▄█,
      █"⌐-]'╓█
     ▄█▄▄▄▄▄▄█▄
  ╒▄█▌▄▄▄▄▄▄▄▄▄█▄⌐
  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
 """
            for i in range (len(candii)):
                print(candii[i], end="", flush=True)
                time.sleep(0.02)

            # Mengurangi bahan yang telah tergunakan untuk membangun candi
            bahan_bangunan[0][2] -= butuh_pasir 
            bahan_bangunan[1][2] -= butuh_batu
            bahan_bangunan[2][2] -= butuh_air

            idx = 0
            for i in range (1000):
                if id[i] == "": # Untuk mengecek array id yang kosong
                    idx = i # Untuk menyimpan indeksnya
                    break

            # Menambahkan kedalam array
            id[idx] = idx
            pembuat[idx] = logged[0]
            pasir[idx] = butuh_pasir
            batu[idx] = butuh_batu
            air[idx] = butuh_air

            jumlah_pembuat = function.jumlah_column(pembuat) # menghitung jumlah candi yang sudah dibangun.
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-jumlah_pembuat}.")
    else:
        print("\nHanya Jin Pembangun yang dapat menggunakan command tersebut.")

# F07 Jin Pengumpul
def kumpul(logged: List[str]):

    if logged[1] == "jin_pengumpul": # Hanya role Jin Pengumpul yang dapat menggunakan command ini

        kumpul_pasir = next(rng_05) # Untuk mengumpulkan pasir
        kumpul_batu = next(rng_05) # Untuk mengumpulkan batu
        kumpul_air = next(rng_05) # Untuk mengumpulkan air
        bahan_bangunan[0][2] += kumpul_pasir # Untuk memasukkan pasir yang telah dikumpulkan kedalam array
        bahan_bangunan[1][2] += kumpul_batu # Untuk memasukkan batu yang telah dikumpulkan kedalam array
        bahan_bangunan[2][2] += kumpul_air # Untuk memasukkan air yang telah dikumpulkan kedalam array
        print(f"\nJin menemukan {kumpul_pasir} pasir, {kumpul_batu} batu, dan {kumpul_air} air.")

    else:
        print("\nHanya Jin Pengumpul yang dapat menggunakan command tersebut.")

# F08 Batch Bangun
def batchbangun(logged: List[str]) -> List[str]:
    jumlah_pembuat1 = function.jumlah_column(pembuat) # menghitung jumlah candi yang sudah dibangun.

    arr_jin_pembangun = function.arr_target("jin_pembangun", userpassrole, 0, 2) 
    jumlah_jin_pembangun = function.jumlah_target ("jin_pembangun", userpassrole, 2)
    
    if logged[1] == "bandung_bondowoso":

        if jumlah_jin_pembangun == 0: # kondisi kalo tidak ada jin pembangun
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

        else: # kondisi kalo ada jin pembangun
            # deklarasi awal jumlah pasir batu air yang dibutuhkan untuk membangun candi
            total_pasir_bangun = 0
            total_batu_bangun = 0
            total_air_bangun = 0

        
            for i in range(jumlah_jin_pembangun): # looping untuk jumlah candi yang akan dibangun untuk 1 candi per jin pembangun
                for j in range(1000): # looping untuk melakukan cek data apakah id candi tertentu sudah dibuat (pake patokan pembuat karena kalo id masih ada kemungkinan id 0)
                    if pembuat[j] == "": # kalo pembuatnya masih none berarti itu belum ada candi yang dibangun untuk id tersebut
                        break
                    
                id[j] = j # id nya tercetak
                pembuat[j] = arr_jin_pembangun[i]
                # randomize jumlah pasir batu air yang dipake untuk ngebangun
                pasir[j] = next(rng_15)
                batu[j] = next(rng_15)
                air[j] = next(rng_15)
                # total pasir batu air yang dibutuhin ditambahin sama yang udh di randomize
                total_pasir_bangun += pasir[j]
                total_batu_bangun += batu[j]
                total_air_bangun += air[j]

            print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {bahan_bangunan[0][2]} pasir, {bahan_bangunan[0][2]} batu, dan {bahan_bangunan[2][2]} air.")
            
            if total_pasir_bangun > bahan_bangunan[0][2] or total_batu_bangun > bahan_bangunan[1][2] or total_air_bangun > bahan_bangunan[2][2]: # kondisi kalo ada salah satu bahan bangunan yang kurang
                kurang_pasir = total_pasir_bangun - bahan_bangunan[0][2]
                kurang_batu = total_batu_bangun - bahan_bangunan[1][2]
                kurang_air = total_air_bangun - bahan_bangunan[2][2]

                if kurang_pasir <= 0 and kurang_batu <= 0: # kondisi kalo yang kurang itu air doang
                    print(f"Bangun gagal. Kurang {kurang_air} air.")

                elif kurang_batu <= 0 and kurang_air <= 0: # kondisi kalo yang kurang itu pasir doang
                        print(f"Bangun gagal. Kurang {kurang_pasir} pasir.") 

                elif kurang_pasir <= 0 and kurang_air <= 0: # kondisi kalo yang kurang itu batu doang
                    print(f"Bangun gagal. Kurang {kurang_batu} batu.")

                elif kurang_pasir <= 0: # kondisi kalo yang kurang itu batu dan air
                    print(f"Bangun gagal. Kurang {kurang_batu} batu dan {kurang_air} air.")

                elif kurang_batu <= 0: # kondisi kalo yang kurang itu pasir dan air
                    print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_air} air.")

                elif kurang_air <= 0: # kondisi kalo yang kurang itu pasir dan batu
                    print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_batu} batu.")

                else: # kondisi kalo yang kurang itu pasir batu air
                    print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")

                print(f"Bahan bangunan yang tersedia hanya sebanyak {bahan_bangunan[0][2]} pasir, {bahan_bangunan[1][2]} batu, dan {bahan_bangunan[2][2]} air.")

                for i in range(j, (j-jumlah_jin_pembangun), -1): # looping kalo misal ada bahan yang kurang, candi gajadi dibangun, balikin filenya jadi kosong sama 0
                    id[i] = ""
                    pembuat[i] = ""
                    pasir[i] = ""
                    batu[i] = ""
                    air[i] = ""

            else: # kondisi gaada bahan bangunan yang kurnag
                bahan_bangunan[0][2] -= total_pasir_bangun
                bahan_bangunan[1][2] -= total_batu_bangun
                bahan_bangunan[2][2] -= total_air_bangun
                # Display candi dibangun.
                candii = """
         ▄▄
         ██
        ,██;
      ,█▄▄▄▄█,
      █"⌐-]'╓█
     ▄█▄▄▄▄▄▄█▄
  ╒▄█▌▄▄▄▄▄▄▄▄▄█▄⌐
  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
 """
                for i in range (len(candii)):
                    print(candii[i], end="", flush=True)
                    time.sleep(0.02)
                # Perhitungan candi yang telah dibangun.
                jumlah_candi = 0
                jumlah_pembuat2 = function.jumlah_column(pembuat) # menghitung jumlah candi yang sudah dibangun.
                if jumlah_pembuat1 > jumlah_pembuat2:
                    jumlah_candi = jumlah_pembuat1 - jumlah_pembuat2
                else:
                    jumlah_candi = jumlah_pembuat2 - jumlah_pembuat1

                print(f"Jin berhasil membangun total {jumlah_candi} candi.")
                print(f"Sisa bahan bangunan sebanyak {bahan_bangunan[0][2]} pasir, {bahan_bangunan[1][2]} batu, dan {bahan_bangunan[2][2]} air.") # kreativitas

    else:
        print("Hanya Bandung Bondowoso yang dapat mengakses command ini.")

# F08 Batch Kumpul
def batchkumpul(logged: List[str]) -> List[str]:
    
    jumlah_jin_pengumpul = function.jumlah_target ("jin_pengumpul", userpassrole, 2) 
    if logged[1] == "bandung_bondowoso":
        if jumlah_jin_pengumpul == 0: # kondisi kalo tidak ada jin pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu")

        else: # kondisi kalo ada jin pengumpul
            # deklarasi jumlah pasir batu air yang dikumpulkan dalam satu sesi command
            total_pasir_kumpul = 0
            total_batu_kumpul = 0
            total_air_kumpul = 0

            for i in range(jumlah_jin_pengumpul): # looping untuk randomize jumlah pasir batu air yang dikumpulkan per jin pengumpul
                total_pasir_kumpul  += next(rng_05)
                total_batu_kumpul += next(rng_05)
                total_air_kumpul += next(rng_05)

            # hasil pasir batu air yang dikumpulkan ditambahin ke array jumlah bahan bangunan pasir batu air
            bahan_bangunan[0][2] += total_pasir_kumpul
            bahan_bangunan[1][2] += total_batu_kumpul
            bahan_bangunan[2][2] += total_air_kumpul

            # output 
            print("Mengerahkan %d jin untuk mengumpulkan bahan." %jumlah_jin_pengumpul)
            print(f"Jin menemukan total {total_pasir_kumpul} pasir, {total_batu_kumpul} batu, dan {total_air_kumpul} air")
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")

# F09 Ambil Laporan Jin
def laporanjin(logged: List[str]) -> List[str]:
    arr_jin_pembangun = function.arr_target("jin_pembangun", userpassrole, 0, 2) 
    jumlah_jin_pembangun = function.jumlah_target ("jin_pembangun", userpassrole, 2)
    jumlah_pembuat = function.jumlah_column(pembuat) # jumlah jin yang sudah membangun candi
    jumlah_jin_pengumpul = function.jumlah_target ("jin_pengumpul", userpassrole, 2) 


    if logged[1] == "bandung_bondowoso":

        # deklarasi cek jin terajin termalas
        check_terajin = 0
        check_termalas = 0
        jin_terajin = "-"
        jin_termalas = "-"

        for i in range(jumlah_jin_pembangun):
            x = 0
            y = 0
            
            for j in range(jumlah_pembuat):
                if pembuat[j] == "":
                    continue
                if arr_jin_pembangun[i] == pembuat[j]: # pembuat candi
                    x += 1
                else: # kondisi kalo beda
                    y += 1

            if x > check_terajin: # kalo dia nama jin samanya lebih banyak dibanding nama jin sama sebelumnya
                check_terajin = x
                jin_terajin = arr_jin_pembangun[i]

            elif x == check_terajin: # kalo dia nama jin samanya sama jumlahnya dengan nama jin sama sebelumnya
                if jin_terajin > arr_jin_pembangun[i]: # leksikografis
                    jin_terajin = arr_jin_pembangun[i]

            elif y > check_termalas: # kalo dia nama jin bedanya sama jumlahnya dengan nama jin beda sebelumnya
                check_termalas = y
                jin_termalas = arr_jin_pembangun[i]

            elif y == check_termalas: # kalo dia nama jin bedanya sama jumlahnya dengan nama jin beda sebelumnya
                if jin_termalas < arr_jin_pembangun[i]: # leksikografis
                    jin_termalas = arr_jin_pembangun[i]
            
        print("Total Jin: %d" %(jumlah_jin_pengumpul + jumlah_jin_pembangun))
        print("Total Jin Pengumpul: %d" %jumlah_jin_pengumpul)
        print("Total Jin Pembangun: %d" %jumlah_jin_pembangun)
        print("Jin Terajin: %s" %jin_terajin)
        print("Jin Termalas: %s" %jin_termalas)
        print("Jumlah Pasir: %d unit" %bahan_bangunan[0][2])
        print("Jumlah Air: %d unit" %bahan_bangunan[1][2])
        print("Jumlah Batu: %d unit" %bahan_bangunan[2][2])

        return (jin_termalas, jin_terajin)
    
    else:
        print("Hanya Bandung Bondowoso yang dapat mengakses command ini.")

# F10 Ambil Laporan Candi
def laporancandi(logged: List[str]) -> List[str]:
    
    jumlah_pembuat = function.jumlah_column(pembuat) # jumlah jin yang sudah membangun candi

    if logged[1] == "bandung_bondowoso":

        # deklarasi awal jumlah pasir batu air yang dipake di semua candi
        total_pasir_candi = 0
        total_batu_candi = 0
        total_air_candi = 0

        for i in range(1000): # looping jumlah pasir batu air yang dipake
            if pasir[i] == "":
                continue
            total_pasir_candi += int(pasir[i])
            total_batu_candi += int(batu[i])
            total_air_candi += int(air[i])

        harga_candi = [0 for i in range(1000)] # deklarasi array awal harga candi
        for i in range (1000): # looping input harga candi ke array
            if pasir[i] == "":
                continue
            harga_candi[i] = (10000 * int(pasir[i])) + (15000 * int(batu[i])) + (7500 * int(air[i]))
        
        # deklarasi awal harga candi termahal dan termurah
        candi_termurah = harga_candi[0]
        candi_termahal = harga_candi[0]

        if jumlah_pembuat == 0:
            id_candi_termahal = " - "
            id_candi_termurah = " - "
        else:
            for i in range(jumlah_pembuat): # looping ngecek harga candi
                if harga_candi[i] >= candi_termahal:
                    candi_termahal = harga_candi[i]
                    id_candi_termahal = i
                else:
                    candi_termurah = harga_candi[i]
                    id_candi_termurah = i

        # output
        print("Total Candi: %d" %jumlah_pembuat)
        print("Jumlah Pasir: %d unit" %total_pasir_candi)
        print("Jumlah Batu: %d unit" %total_batu_candi)
        print("Jumlah Air: %d unit" %total_air_candi)
        print("ID Candi Termahal:", id_candi_termahal, "(%d)" %candi_termahal)
        print("ID Candi Termurah:", id_candi_termurah, "(%d)" %candi_termurah)

        return (candi_termurah, candi_termahal)
    
    else:
        print("Hanya Bandung Bondowoso yang dapat mengakses command ini.")

# F11 Hancurkan Candi
def hancurkancandi(logged: List[str]) -> List[str]:
    if logged[1] == "roro_jonggrang":

        id_hancur = int(input("Masukkan ID candi: ")) # input id candi yang mau dihancurin
        check_hancur = 0

        for i in range(1000): # looping untuk ngecek ada ga id candi yang mau diancurin sama dengan yang di array id
            if id[i] == "":
                continue
            if id_hancur == int(id[i]):
                check_hancur += 1
                break

        if check_hancur > 0: # kondisi kalo cek hancurnya lebih dari 0 (1) tandanya ada yg sama di array id
            YN = input("Apakah anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %int(id_hancur))

            while YN != "Y" and YN != "N": # kondisi kalo pilihan yang ditulis bukan Y atau N
                print("Tidak ada pilihan tersebut.\n")
                YN = input("Apakah anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %int(id_hancur))

            if YN == "Y": # kondisi kalo udh inputnya Y
                id[i] = ""
                pembuat[i] = ""
                pasir[i] = ""
                batu[i] = ""
                air[i] = ""
                print("Candi telah berhasil dihancurkan.")

            else: # kondisi kalo dia jawabnya N
                print("Candi tidak jadi dihancurkan.")

        else: # kondisi kalo gaada id yang mau diancurin sama dengan array id
            print("Tidak ada candi dengan ID tersebut.\n")
            hancurkancandi (logged)

        return
    
    else:
        print("Hanya Roro Jonggrang yang dapat mengakses command ini.")

# F12 Ayam Berkokok
def ayamberkokok(logged: List[str]):
    
    jumlah_pembuat = function.jumlah_column(pembuat)

    if logged[1] == "roro_jonggrang": # Hanya role Roro Jonggrang yang dapat menggunakan command ini

        if jumlah_pembuat >= 100: # Apabila jumlah candi mencapai 100 maka Bandung Bondowoso akan memenangkan permainan

            print("Kukuruyuk.. Kukuruyuk..\n")
            print("Jumlah Candi: 100\n")
            print("Yah, Bandung Bondowoso memenangkan permainan!")

        else: # Apabila jumlah candi dibawah 100 maka Roro Jonggrang akan memenangkan permainan
            print("Kukuruyuk.. Kukuruyuk..")
            print(f"Jumlah Candi: {jumlah_pembuat}\n")
            print(f"Selamat, Roro Jonggrang memenangkan permainan!\n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        exit()

    else:
        print("Hanya Roro Jonggrang yang dapat menggunakan command tersebut.")

# F13 Load
def cekPath(path: str): #pemanggilan prosedur untuk memvalidasi keberadaan folder yang di-input tersebut benar atau bukan    
    
    pathtodata = f"save/{path}" #direktori tempat file disimpan dalam laptop 

    if path: #kondisional untuk mengecek apakah user memasukkan parameter seperti yang diminta atau tidak (kosong / no input)
    
        if os.path.exists(pathtodata): #jika path yang diinput valid/exists dalam komputer maka menjalankan command berikutnya
            # print text
            print("\nLoading", end = "")
            for i in range(4):
                print(".", end='', flush= True)
                time.sleep(0.4)
            time.sleep(0.5)
            print("\n\n          [Selamat datang di program Manajerial Candi]\n")
            load(path)
                                
        else: #kondisi jika input path berupa nama folder yang tidak tersedia
            # print text 
            print("\nLoading", end = "")
            for i in range(4):
                print(".", end='', flush= True)
                time.sleep(0.5)
            time.sleep(0.7)
            print(f"\n\n[Folder '{path}' tidak ditemukan.]\n")
            exit()  # program keluar 

    else: 
        print("\nTidak ada nama folder yang diberikan!\nUsage: python main.py <nama_folder>\n") #jika tidak menginput file apapun
        exit() #program keluar

def load(foldername: str): # transfer data dari file csv ke dalam array/matrix
    # menyimpan file dalam variabel
    fileBahanBangunan = open(f"save/{foldername}/bahan_bangunan.csv","r")
    fileCandi = open(f"save/{foldername}/candi.csv","r")
    fileUser = open(f"save/{foldername}/user.csv","r")

    # melakukan transfer data dari file csv ke array/matrix 
    for i in range(102):
        userpassrole[i] = function.makeshift_split(fileUser.readline(),3)
    for i in range(3):
        bahan_bangunan[i] = function.makeshift_split(fileBahanBangunan.readline(),3)
        bahan_bangunan[i][-1] = int(bahan_bangunan[i][-1])
    for i in range(1000):
        arraycandi = function.makeshift_split(fileCandi.readline(),5)
        id[i], pembuat[i], pasir[i], batu[i], air[i] = arraycandi[0], arraycandi[1], arraycandi[2], arraycandi[3], arraycandi[4]

# F14 Save
def save():

    folder_name = input("Masukkan nama folder: ") # Input nama folder
    
    if not os.path.exists(f"save/{folder_name}"): # Jika folder tidak dapat ditemukan.
        
        if not os.path.exists("save"): # Jika tidak ada folder save, maka akan di buat folder save dan folder yang diinginkan.
            os.mkdir("save") 
            os.mkdir(f"save/{folder_name}")
            # print text saving
            print(f"\nMembuat folder save dan {folder_name}", end="")
            for i in range(4):
                print(".",end="",flush = True)
                time.sleep(0.5)
            time.sleep(0.4)
            print("\n\nSaving",end="")
            for i in range(3):
                print(".",end="",flush = True)
                time.sleep(0.5)
            time.sleep(0.4)
            print(f"\nBerhasil menyimpan data di folder save/{folder_name}!")

        else: # Folder save sudah ada.
            os.mkdir(f"save/{folder_name}")
            # print text saving
            print(f"\nMembuat folder {folder_name}", end="")
            for i in range(4):
                print(".",end="",flush = True)
                time.sleep(0.5)
            time.sleep(0.4)
            print("\n\nSaving",end="")
            for i in range(3):
                print(".",end="",flush = True)
                time.sleep(0.5)
            time.sleep(0.4)
            print(f"\nBerhasil menyimpan data di folder save/{folder_name}!")

    else: # folder yang diinginkan ada.
        print(f"\nMencari folder {folder_name}", end="")
        # print text saving
        for i in range(4):
            print(".",end="",flush = True)
            time.sleep(0.5)
        time.sleep(0.4)
        print("\n\nSaving",end="")
        for i in range(3):
            print(".",end="",flush = True)
            time.sleep(0.5)
        time.sleep(0.4)
        print(f"\nBerhasil menyimpan data di folder save/{folder_name}!")

    # Membuka file csv tempat penyimpanan data.
    file_user = open(f"save/{folder_name}/user.csv","w") 
    file_candi = open(f"save/{folder_name}/candi.csv","w")
    file_bahan_bangunan = open(f"save/{folder_name}/bahan_bangunan.csv","w")

    # Memasukkan data dalam file csv.
    for i in range(102):
        file_user.write(f"{userpassrole[i][0]};{userpassrole[i][1]};{userpassrole[i][2]}\n")
    for i in range(100):
        file_candi.write(f"{id[i]};{pembuat[i]};{pasir[i]};{batu[i]};{air[i]}\n")
    for i in range(3):
        file_bahan_bangunan.write(f"{bahan_bangunan[i][0]};{bahan_bangunan[i][1]};{bahan_bangunan[i][2]}\n")
    
    # Folder ditutup setelah diwrite.
    file_user.close()
    file_candi.close()
    file_bahan_bangunan.close()

# F15 Help
def helps(logged: List[str]):

    if logged[1] == "": # Output untuk pemain yang belum login
        print("=========== HELP ===========")
        print("1. login \nUntuk masuk menggunakan akun")
        print("2. exit \nUntuk keluar dari program dan kembali ke terminal")

    elif logged[1] == "bandung_bondowoso":  # Output untuk role Bandung Bondowoso
        print("=========== HELP ===========")
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin \nUntuk memanggil jin")
        print("3. hapusjin \nUntuk menghilangkan jin yang telah di summon")
        print("4. ubahjin \nUntuk mengubah tipe jin yang telah di summon")
        print("5. batchkumpul \nUntuk mengerahkan seluruh pasukan Jin Pengumpul untuk mengumpulkan bahan")
        print("6. batchbangun \nUntuk mengerahkan seluruh pasukan Jin Pembangun untuk membangun candi")
        print("7. laporanjin \nUntuk mengambil laporan jin untuk mengetahui kinerja dari para jin")
        print("8. laporancandi \nUntuk mengambil laporan candi untuk mengetahui progress pembangunan candi")
        print("9. save \nUntuk menjalankan prosedur menyimpan data yang berada di program")
        print("10. exit \nUntuk keluar dari program dan kembali ke terminal")
        print("11. summonjinplus \nUntuk mensummon jin lebih dari 1 kali.")


    elif logged[1] == "roro_jonggrang": # Output untuk role Roro Jonggrang
        print("=========== HELP ===========")
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi \nUntuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok \nUntuk menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. save \nUntuk menjalankan prosedur menyimpan data yang berada di program")
        print("5. exit \nUntuk keluar dari program dan kembali ke terminal")

    elif logged[1] == "jin_pembangun": # Output untuk role Jin Pembangun
        print("=========== HELP ===========")
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. bangun \nUntuk membangun candi")
        print("3. save \nUntuk menjalankan prosedur menyimpan data yang berada di program")
        print("4. exit \nUntuk keluar dari program dan kembali ke terminal")

    elif logged[1] == "jin_pengumpul":
        print("=========== HELP ===========") # Output untuk role Jin Pengumpul
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul \nUntuk mengumpulkan resource candi")
        print("3. save \nUntuk menjalankan prosedur menyimpan data yang berada di program")
        print("4. exit \nUntuk keluar dari program dan kembali ke terminal")

# F16 Exit
def exit_game():
    
    check1 = True #batas awal untuk pengecekan apakah command berjalan sesuai / tidak
    while (check1 == True): #memasuki looping selama kondisi batas (check1 masih bernilai True)
        #input untuk memvalidasi pilihan pengguna, apakah mau men-save file yang sudah diupdate atau tidak
        validasi = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")) 
        if (validasi.lower()== "n" or validasi.lower()== "y"): #kondisi ke-2 untuk memastikan user hanya menginput nilai y dan n
            if (validasi.lower()=="y"): #kondisi 3, jika user setuju untuk save sebelum melakukan exit
                save() #memanggil procedure save
                check1 = False
            else:
                check1 = False #batasan berubah nilai karena ada command yang tidak terpenuhi
        elif not (validasi.lower()== "n" or validasi.lower()== "y"): #kondisional 
            print("\nInput tidak valid, harap masukkan 'y' atau 'n'")
    # Print text exiting game
    print("\nExiting game", end='')
    for i in range(5):
        print(".", end = "", flush = True)
        time.sleep(0.5)
    exit()

# Batch summon
def summonjinplus(logged: List[str]):

    if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini. 
         # input jumlah jin yang ingin disummon

        banyakjin = int(input("Banyak jin yang ingin di summon: "))

        jumlah_jin = function.jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)
        if jumlah_jin + banyakjin > 100: # tidak boleh melebihi jumlah maks jin
            print("\nSummon gagal! Anda melebihi batas maks summonjin.")
            return
        
        else:
            print("\nJenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")

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
            
            for i in range(banyakjin): # dalam loop jumlah banyak jin 
                numba = 1 # proses pembuatan username dan password jin
                for j in range(102):
                    if f"userjin{numba}" != userpassrole[j][0]:
                        numba = numba
                    else:
                        numba += 1
                userjin = f"userjin{numba}"
                passjin = f"passjin{numba}"
                print(f"Jin ke-{i+1}:\nUsername: {userjin}\nPassword: {passjin}")
                function.addlistmatrix(userpassrole, 102, 3, [userjin,passjin,rolejin])
            # Print teks 
            print("\nMengumpulkan sesajens", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            print("\nMenyerahkan sesajens", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            print("\nMembacakan mantras", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            print(f"\n\n{banyakjin} jin berhasil dipanggil!")
            return
    else:
        print("Hanya Bandung Bondowoso yang dapat mengakses command ini.")
