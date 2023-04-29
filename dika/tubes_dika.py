import time

def lcg_05(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a * x + c) % m # Algoritma LCG
        yield x % 6  # Random Number Generator yang dapat menghasilkan nilai dari 0 sampai 5

def lcg_15(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a * x + c) % m # Algoritma LCG
        yield (x % 5) + 1 # Random Number Generator yang dapat menghasilkan nilai dari 1 sampai 5

def bangun(logged):
    if logged[1] == "jin_pembangun": # Hanya role Jin Pembangun yang dapat menggunakan command ini 
        seed_value = int(time.time() * 1000000)  # Menggunakan waktu dalam mikrosekon agar nilai dapat lebih bervariasi
        rng = lcg_15(seed_value) # Mendapatkan nilai dari 1 sampai 5 secara acak
        butuh_pasir = next(rng) # Untuk menentukan berapa banyak pasir yang dibutuhkan untuk membangun satu candi
        butuh_batu = next(rng) # Untuk menentukan berapa banyak batu yang dibutuhkan untuk membangun satu candi
        butuh_air = next(rng) # Untuk menentukan berapa banyak air yang dibutuhkan untuk membangun satu candi
        if butuh_pasir > jumlah[0] or butuh_batu > jumlah[1] or butuh_air > jumlah[2]: # Apabila salah satu dari pasir, batu, dan air yang dibutuhkan lebih banyak dari yang dimiliki, maka candi tidak bisa dibangun
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else:
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-jumlah_pembuat}.")
            # Mengurangi bahan yang telah tergunakan untuk membangun candi
            jumlah[0] -= butuh_pasir 
            jumlah[1] -= butuh_batu
            jumlah[2] -= butuh_air
            for i in range (100):
                if id[i] == None: # Untuk mengecek array id yang kosong
                    idx = i # Untuk menyimpan indeksnya
                    break
            # Menambahkan kedalam array
            id[idx] = idx
            pembuat[i] = logged[0]
            pasir[i] = butuh_pasir
            batu[i] = butuh_batu
            air[i] = butuh_air
    else:
        print("Hanya Jin Pembangun yang dapat menggunakan command tersebut.")

def kumpul(logged):
    if logged[1] == "jin_pengumpul": # Hanya role Jin Pengumpul yang dapat menggunakan command ini
        seed_value = int(time.time() * 1000000)  # Menggunakan waktu dalam mikrosekon agar nilai dapat lebih bervariasi
        rng = lcg_05(seed_value) # Mendapatkan nilai dari 0 sampai 5 secara acak
        kumpul_pasir = next(rng) # Untuk mengumpulkan pasir
        kumpul_batu = next(rng) # Untuk mengumpulkan batu
        kumpul_air = next(rng) # Untuk mengumpulkan air
        jumlah[0] += kumpul_pasir # Untuk memasukkan pasir yang telah dikumpulkan kedalam array
        jumlah[1] += kumpul_batu # Untuk memasukkan batu yang telah dikumpulkan kedalam array
        jumlah[2] += kumpul_air # Untuk memasukkan air yang telah dikumpulkan kedalam array
        print(f"Jin menemukan {kumpul_pasir} pasir, {kumpul_batu} batu, dan {kumpul_air} air.")
    else:
        print("Hanya Jin Pengumpul yang dapat menggunakan command tersebut.")
        return jumlah
    
def ayamberkokok(logged):
    if logged[1] == "roro_jonggrang": # Hanya role Roro Jonggrang yang dapat menggunakan command ini
        if jumlah_pembuat == 100: # Apabila jumlah candi mencapai 100 maka Bandung Bondowoso akan memenangkan permainan
            print("Kukuruyuk.. Kukuruyuk..\n")
            print("Jumlah Candi: 100\n")
            print("Yah, Bandung Bondowoso memenangkan permainan!")
        else: # Apabila jumlah candi dibawah 100 maka Roro Jonggrang akan memenangkan permainan
            print("Kukuruyuk.. Kukuruyuk..")
            print(f"Jumlah Candi: {jumlah_pembuat}\n")
            print(f"Selamat, Roro Jonggrang memenangkan permainan!\n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Hanya Roro Jonggrang yang dapat menggunakan command tersebut.")

def helps(logged):
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
    elif logged[1] == "roro_jonggrang": # Output untuk role Roro Jonggrang
        print("=========== HELP ===========")
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi \nUntuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok \nUntuk menyelesaikan permainan dengan memalsukan pagi hari")
    elif logged[1] == "jin_pembangun": # Output untuk role Jin Pembangun
        print("=========== HELP ===========")
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. bangun \nUntuk membangun candi")
    elif logged[1] == "jin_pengumpul":
        print("=========== HELP ===========") # Output untuk role Jin Pengumpul
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul \nUntuk mengumpulkan resource candi") 