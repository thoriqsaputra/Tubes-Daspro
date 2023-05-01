def login(logged: List[str]) -> List[str]:
    
    if (logged[0] ≠ "") then
        output(f"Login gagal!\nAnda telah login dengan username {logged[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        return (logged)
    else    

        while True do 
            
            input(user) 
            input(pa55)
            if (user == "" or user == "") then
                output("\nInput salah!\n")
                continue
            i traversal [0..102]
                if (user == userpassrole[i][0] & pa55 == userpassrole[i][1]) then
                    output(f"\nSelamat datang, {user} \nMasukkan command “help” untuk daftar command yang dapat kamu panggil")
                    logged ← [userpassrole[i][0],userpassrole[i][2]]
                    return (logged)
                
                else if (user == userpassrole[i][0] & pa55 ≠ userpassrole[i][1]) do 
                    output("\nPassword salah!")
                    return (logged)
            else
                output("\nUsername tidak terdaftar!") 
                return (logged)

# F02 Logout
def logout(logged: List[str]) -> List[str]: # log out dari akun
    if (logged[1] == "") then
        output("\nLogout gagal!\n\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout\n")
        return (logged)
    else
        logged ← ["",""] # Array of logged information
        output("\nLogout berhasil!\n")
        return (logged)

# F03 Summon Jin
def summonjin(logged: List[str]) -> List[str]: # Summon jin oleh Bondowoso
    if (logged[1] == "bandung_bondowoso") do
        
        jumlah_jin ← jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)
        if (jumlah_jin ≥ 100) then
            output("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            return
        else
            output("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")

            while True do

                input(jin)
                
                if (jin == "1") then
                    rolejin ← "jin_pengumpul" 
                    output("\nMemilih jin “Pengumpul”.\n")
                    break
                else if (jin == "2") do
                    rolejin ← "jin_pembangun" 
                    output("\nMemilih jin “Pembangun”.\n")
                    break
                else
                    output(f"\nTidak ada jenis jin bernomor “{jin}”!\n")

            while True do 
                input(userjin)
                if (userjin == "") then
                    output("\nTry again.\n")
                    continue
                i traversal [0..102]
                    if (userjin == userpassrole[i][0]) then
                        output(f"Username “{userjin}” sudah diambil!")
                        break

                else # username belum ada
                    while True do # Loop 3 Menentukan password jin.
                        input(passjin) # Input password jin.
                        if not(5 ≤ len(passjin) ≤ 25) then # Password harus sepanjang 5-25 kata.
                            output("\nPassword panjangnya harus 5-25 karakter!\n")
                            continue
                        else 
                            addlistmatrix(userpassrole, 102, 3, [userjin,passjin,rolejin])
                            output("\nMengumpulkan sesajen", end="")
                            i traversal [0..3] 
                                output(".", end="", flush=True)
                                sleep(0.4)
                            output("\nMenyerahkan sesajen", end="")
                            i traversal [0..3] 
                                output(".", end="", flush=True)
                                sleep(0.4)
                            output("\nMembacakan mantra", end="")
                            i traversal [0..3] 
                                output(".", end="", flush=True)
                                sleep(0.4)
                            output(f"\n{userjin} berhasil dipanggil!")
                            return
                    
    else
        output("Hanya Bondowoso yang dapat mengakses command ini.")

# F04 Hilangkan Jin
def hapusjin(logged: List[str]) -> List[str]: # Menghilangkan Jin.
    if logged[1] == "bandung_bondowoso":  # Hanya Bondowoso yang dapat melakukan command ini.

        input(jinhapus) # Input username jin.

        i traversal [2..102] # loop jumlah index data
            if (jinhapus == userpassrole[i][0]) then # jika user baru ada maka return True
                while True do
                    # User disuruh input antara Y atau N dalam penghapusan jin.
                    input(yesno)
                    if (yesno == "Y") then #jika iya maka akan di hapus
                        i traversal [0..102] 
                            if (jinhapus == userpassrole[i][0]) then
                                userpassrole[i] ← ["","",""] # diubah jadi ""
                                output("\nJin telah berhasil dihapus dari alam gaib.")
                        i traversal [0..1000] # menghapuskan candi yang telah di bangun.
                            if (jinhapus == pembuat[i]) then
                                id[i] ← ""
                                pembuat[i] ← ""
                                pasir[i] ← ""
                                batu[i] ← ""
                                air[i] ← ""
                        return
                    
                    else if (yesno == "N") then # Jika tidak, maka akan keluar dari bagian ini.
                        return("\nJin tidak jadi dihapus.\n")                        
                    else
                        output("\nPilih antara Y atau N.\n")
        else
            output("\nTidak ada jin dengan username tersebut.\n")
    else
        output("Hanya Bondowoso yang dapat mengakses command ini.")

def summonjinplus(logged: List[str]):

    if logged[1] == "bandung_bondowoso": # Hanya Bondowoso yang dapat melakukan command ini. 
         # input jumlah jin yang ingin disummon
        input(banyakjin)
        jumlah_jin ← jumlah_targetList (["jin_pembangun","jin_pengumpul"], userpassrole, 2)
        if (jumlah_jin + banyakjin > 100) then # tidak boleh melebihi jumlah maks jin
            output("Summon gagal! Anda melebihi batas maks summonjin.")
            return
        
        else
            output("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi\n")

            while True do  # Loop 1 menentukan role jin.

                input(jin) # Input jin yang mau dihapuskan.
                
                if (jin == "1") do # Memilih jin pengumpul. 
                    rolejin ← "jin_pengumpul" # Menyimpan dalam sebuah variabel.
                    output("\nMemilih jin “Pengumpul”.\n")
                    break
                else if (jin == "2") do # Memilih jin pembangun.
                    rolejin ← "jin_pembangun" # Menyimpan dalam sebuah variabel.
                    output("\nMemilih jin “Pembangun”.\n")
                    break
                else # Selain dari jin pengumpul dan jin pembangun.
                    output(f"\nTidak ada jenis jin bernomor “{jin}”!\n")
            
            i traversal [banyakjin] # dalam loop jumlah banyak jin 
                numba ← 1 # proses pembuatan username dan password jin
                j traversal [102]
                    if (f"userjin{numba}" ≠  userpassrole[j][0]) do
                        numba ← numba
                    else
                        numba ← numba + 1
                userjin ← f"userjin{numba}"
                passjin ← f"passjin{numba}"
                output(f"Jin ke-{i+1}:\nUsername: {userjin}\nPassword: {passjin}")
                addlistmatrix(userpassrole, 102, 3, [userjin,passjin,rolejin])
            # Print teks 
            output("\nMengumpulkan sesajens", end="")
            i traversal [3]
                output(".", end="", flush=True)
                sleep(0.4)
            output("\nMenyerahkan sesajens", end="")
            i traversal [3]
                output(".", end="", flush=True)
                sleep(0.4)
            output("\nMembacakan mantras", end="")
            i traversal [3]
                output(".", end="", flush=True)
                sleep(0.4)
            output(f"\n{banyakjin} jin berhasil dipanggil!\n")
            return
    else
        output("Hanya Bondowoso yang dapat mengakses command ini.")