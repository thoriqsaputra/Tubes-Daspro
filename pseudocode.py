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
        print("\nLogout gagal!\n\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout\n")
        return logged
    else:
        logged = ["",""] # Array of logged information
        print("\nLogout berhasil!\n")
        return logged

# F03 Summon Jin
def summonjin(logged: List[str]) -> List[str]: # Summon jin oleh Bondowoso
    if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini.
        
        jumlah_jin = function.jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)
        print(jumlah_jin)
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
                        print(f"Username “{userjin}” sudah diambil!")
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
                            print(f"\n{userjin} berhasil dipanggil!")
                            return
                    
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")

# F04 Hilangkan Jin
def hapusjin(logged: List[str]) -> List[str]: # Menghilangkan Jin.
    if logged[1] == "bandung_bondowoso":  # Hanya Bondowoso yang dapat melakukan command ini.

        jinhapus = input("\nMasukkan username jin : ") # Input username jin.

        for i in range(2, 102): # loop jumlah index data
            if jinhapus == userpassrole[i][0]: # jika user baru ada maka return True
                while True: 
                    # User disuruh input antara Y atau N dalam penghapusan jin.
                    yesno = input(f"Apakah anda yakin ingin menghapus jin dengan username {jinhapus} (Y/N)? ")
                    if yesno == "Y": #jika iya maka akan di hapus
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
                    
                    elif yesno == "N": # Jika tidak, maka akan keluar dari bagian ini.
                        return("\nJin tidak jadi dihapus.\n")                        
                    else:
                        print("\nPilih antara Y atau N.\n")
        else:
            print("\nTidak ada jin dengan username tersebut.\n")
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")

def summonjinplus(logged: List[str]):

    if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini. 
         # input jumlah jin yang ingin disummon
        banyakjin = int(input("Banyak jin yang ingin disummon: "))
        jumlah_jin = function.jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)
        if jumlah_jin + banyakjin > 100: # tidak boleh melebihi jumlah maks jin
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
            print(f"\n{banyakjin} jin berhasil dipanggil!\n")
            return
    else:
        print("Hanya Bondowoso yang dapat mengakses command ini.")