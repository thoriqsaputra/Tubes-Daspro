from main_bry import *
import random

"""
Kamus:
jumlah_jin_pengumpul: int -> jumlah jin pengumpul yang ada
jumlah_jin_pembangun: int -> jumlah jin pembangun yang ada
total_pasir_kumpul: int -> total pasir yang dikumpulkan jin pengumpul dalam satu command
total_batu_kumpul: int -> total batu yang dikumpulkan jin pengumpul dalam satu command
total_air_kumpul: int -> total air yang dikumpulkan jin pengumpul dalam satu command
total_pasir_bangun: int -> total pasir yang digunakan untuk membangun semua candi dalam satu command
total_batu_bangun: int -> total batu yang digunakan untuk membangun semua candi dalam satu command
total_air_bangun: int -> total air yang digunakan untuk membangun semua candi dalam satu command
kurang_pasir: int -> jumlah pasir yang kurang untuk membangun semua candi dalam satu command
kurang_batu: int -> jumlah batu yang kurang untuk membangun semua candi dalam satu command
kurang_air: int -> jumlah air yang kurang untuk membangun semua candi dalam satu command
total_pasir_candi: int -> jumlah pasir yang digunakan untuk membangun semua candi
total_batu_candi: int -> jumlah batu yang digunakan untuk membangun semua candi
total_air_candi: int -> jumlah air yang digunakan untuk membangun semua candi
jin_termalas: str -> username jin yang membangun candi paling sedikit
jin_terajin: str -> username jin yang membangun candi paling banyak
candi_termurah: int -> harga candi yang dibangun termurah
candi_termahal: int -> harga candi yang dibangun termahal
id_hancur: int -> id candi yang akan dihancurkan
YN: str -> yes atau no untuk menghancurkan candi
"""

# F08 batchkumpul
def batchkumpul(jumlah):

    if jumlah_jin_pengumpul == 0: # kondisi kalo tidak ada jin pengumpul
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu")

    else: # kondisi kalo ada jin pengumpul
        # deklarasi jumlah pasir batu air yang dikumpulkan dalam satu sesi command
        total_pasir_kumpul = 0
        total_batu_kumpul = 0
        total_air_kumpul = 0

        for i in range(jumlah_jin_pengumpul): # looping untuk randomize jumlah pasir batu air yang dikumpulkan per jin pengumpul
            total_pasir_kumpul  += rng_05
            total_batu_kumpul += rng_05
            total_air_kumpul += rng_05

        # hasil pasir batu air yang dikumpulkan ditambahin ke array jumlah bahan bangunan pasir batu air
        jumlah[0] += total_pasir_kumpul
        jumlah[1] += total_batu_kumpul
        jumlah[2] += total_air_kumpul

        # output 
        print("Mengerahkan %d jin untuk mengumpulkan bahan." %jumlah_jin_pengumpul)
        print(f"Jin menemukan total {total_pasir_kumpul} pasir, {total_batu_kumpul} batu, dan {total_air_kumpul} air")

    return jumlah

# F08 batchbangun
def batchbangun(jumlah, id, pembuat, pasir, batu, air):
    
    if jumlah_jin_pembangun == 0: # kondisi kalo tidak ada jin pembangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

    else: # kondisi kalo ada jin pembangun
        # deklarasi awal jumlah pasir batu air yang dibutuhkan untuk membangun candi
        total_pasir_bangun = 0
        total_batu_bangun = 0
        total_air_bangun = 0

    
        for i in range(jumlah_jin_pembangun): # looping untuk jumlah candi yang akan dibangun untuk 1 candi per jin pembangun
            for j in range(100): # looping untuk melakukan cek data apakah id candi tertentu sudah dibuat (pake patokan pembuat karena kalo id masih ada kemungkinan id 0)
                if pembuat[j] == None: # kalo pembuatnya masih none berarti itu belum ada candi yang dibangun untuk id tersebut
                    break
                
            id[j] = j # id nya tercetak
            pembuat[j] = arr_jin_pembangun[i]
            # randomize jumlah pasir batu air yang dipake untuk ngebangun
            pasir[j] = rng_15 
            batu[j] = rng_15
            air[j] = rng_15
            # total pasir batu air yang dibutuhin ditambahin sama yang udh di randomize
            total_pasir_bangun += pasir[j]
            total_batu_bangun += batu[j]
            total_air_bangun += air[j]

        print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {jumlah[0]} pasir, {jumlah[1]} batu, dan {jumlah[2]} air.")
        
        if total_pasir_bangun > jumlah[0] or total_batu_bangun > jumlah[1] or total_air_bangun > jumlah[2]: # kondisi kalo ada salah satu bahan bangunan yang kurang
            kurang_pasir = total_pasir_bangun - jumlah[0]
            kurang_batu = total_batu_bangun - jumlah[1]
            kurang_air = total_air_bangun - jumlah[2]

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

            print(f"Sisa bahan bangunan sebanyak {jumlah[0]} pasir, {jumlah[1]} batu, dan {jumlah[2]} air.")

            for i in range(j, (j-jumlah_jin_pembangun), -1): # looping kalo misal ada bahan yang kurang, candi gajadi dibangun, balikin filenya jadi None sama 0
                id[i] = None
                pembuat[i] = None
                pasir[i] = 0
                batu[i] = 0
                air[i] = 0

        else: # kondisi gaada bahan bangunan yang kurnag
            jumlah[0] -= total_pasir_bangun
            jumlah[1] -= total_batu_bangun
            jumlah[2] -= total_air_bangun

            print(f"Jin berhasil membangun total {jumlah_jin_pembangun} candi.")
            print(f"Sisa bahan bangunan sebanyak {jumlah[0]} pasir, {jumlah[1]} batu, dan {jumlah[2]} air.") # kreativitas

    return (jumlah, id, pembuat, pasir, batu, air)

# F09 laporanjin
def laporanjin (pembuat, jumlah):

    # deklarasi cek jin terajin termalas
    check_terajin = 0
    check_termalas = 0
    jin_terajin = ""
    jin_termalas = ""

    for i in range(jumlah_jin_pembangun):
        x = 0
        y = 0
        

        for j in range(jumlah_pembuat):
            if arr_jin_pembangun[i] == pembuat[j]: # kondisi kalo nama jin pembangun sama dengan nama pembuat candi
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
    print("Jumlah Pasir: %d unit" %jumlah[0])
    print("Jumlah Air: %d unit" %jumlah[1])
    print("Jumlah Batu: %d unit" %jumlah[2])

    return (jin_termalas, jin_terajin)

# F10 laporancandi
def laporancandi (pasir, batu, air):

    # deklarasi awal jumlah pasir batu air yang dipake di semua candi
    total_pasir_candi = 0
    total_batu_candi = 0
    total_air_candi = 0

    for i in range(jumlah_pembuat): # looping jumlah pasir batu air yang dipake
        total_pasir_candi += pasir[i]
        total_batu_candi += batu[i]
        total_air_candi += air[i]

    harga_candi = [0 for i in range(100)] # deklarasi array awal harga candi
    for i in range (100): # looping input harga candi ke array
        harga_candi[i] = (10000 * pasir[i]) + (15000 * batu[i]) + (7500 * air[i])
    
    # deklarasi awal harga candi termahal dan termurah
    candi_termurah = harga_candi[0]
    candi_termahal = harga_candi[0]

    for i in range(jumlah_pembuat): # looping ngecek harga candi
        if harga_candi[i] >= candi_termahal:
            candi_termahal = harga_candi[i]
            id_candi_termahal = i
        elif harga_candi[i] <= candi_termurah:
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

# F11 hancurkancandi
def hancurkancandi (id, jumlah_pembuat):

    id_hancur = int(input("Masukkan ID candi: ")) # input id candi yang mau dihancurin
    check_hancur = 0

    for i in range(jumlah_pembuat): # looping untuk ngecek ada ga id candi yang mau diancurin sama dengan yang di array id
        if id_hancur == id[i]:
            check_hancur += 1
        break

    if check_hancur > 0: # kondisi kalo cek hancurnya lebih dari 0 (1) tandanya ada yg sama di array id
        YN = input("Apakh anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %id_hancur)

        while YN != "Y" and "N": # kondisi kalo pilihan yang ditulis bukan Y atau N
            print("\nTidak ada pilihan tersebut.")
            YN = input("Apakh anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %id_hancur)

        if YN == "Y": # kondisi kalo udh inputnya Y
            if i == jumlah_id - 1: # kondisi kalo candi yang mau diancurin itu adalah data terakhir yang terisi
                id[i] = None

            else: # kondisi kalo candi yang mau diancurin itu ada di tengah tengah data
                for j in range((i+1), jumlah_id):
                    id[j-1] = id[j]
                id[jumlah_id - 1] = None
                print("\nCandi telah berhasil dihancurkan.")

        else: # kondisi kalo dia jawabnya N
            print("\nCandi tidak jadi dihancurkan.")

    else: # kondisi kalo gaada id yang mau diancurin sama dengan array id
        print("\nTidak ada candi dengan ID tersebut.")
        hancurkancandi (id, jumlah_pembuat)

    return (id)