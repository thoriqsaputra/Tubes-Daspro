# Import module yang dibutuhkan
import spesifikasi, argparse, time
# Array user logged [username, role]
logged = ["",""] 

# Memulai permainan dengan input python main.py <nama folder>, input melalui teriminal
parser = argparse.ArgumentParser()
# Menerima input bertipe string & bersifat positional (parameter spesifik) dan hanya menerima input 0 s/d 1 argument
parser.add_argument("path", nargs='?', type=str) 
args = parser.parse_args()                       
spesifikasi.cekPath(args.path)

# Print welcoming sign
message1 = """
                    ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                    ───█▒▒░░░░░░░░░▒▒█───
                    ────█░░█░░░░░█░░█────
                    ─▄▄──█░░░▀█▀░░░█──▄▄─
                    █░░█─▀▄░░░░░░░▄▀─█░░█
                    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
                    █░░║║║╠─║─║─║║║║║╠─░░█
                    █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
"""
message2 = "Permainan dimulai! Gunakan command 'help' untuk melihat daftar command yang ada.\n"

for i in range(len(message1)):
    print(message1[i], end='', flush=True)
    if message1[i] != " ":
        time.sleep(0.001)
for i in range(len(message2)):
    print(message2[i], end='', flush=True )
    time.sleep(0.03)
print()

# Loop permainan 
while True:
    cmd = input(">>> ")

    if logged[1] == "" and cmd != "logout" and cmd != "login" and cmd != "help" and cmd != "exit":
        print('\nAnda belom Login atau salah input, gunakan command "help" untuk menampilkan daftar command.\n')
    elif cmd == "login":
        logged = spesifikasi.login(logged)
    elif cmd == "logout":
        logged = spesifikasi.logout(logged)
    elif cmd == "summonjin":
        spesifikasi.summonjin(logged)
    elif cmd == "hapusjin":
        spesifikasi.hapusjin(logged)
    elif cmd == "ubahjin":
        spesifikasi.ubahjin(logged)    
    elif cmd == "bangun":
        spesifikasi.bangun(logged)
    elif cmd == "kumpul":
        spesifikasi.kumpul(logged)
    elif cmd == "batchbangun":
        spesifikasi.batchbangun(logged)
    elif cmd == "batchkumpul":
        spesifikasi.batchkumpul(logged)
    elif cmd == "laporanjin":
        spesifikasi.laporanjin(logged)
    elif cmd == "laporancandi":
        spesifikasi.laporancandi(logged)
    elif cmd == "hancurkancandi":
        spesifikasi.hancurkancandi(logged)
    elif cmd == "ayamberkokok":
        spesifikasi.ayamberkokok(logged)
    elif cmd == "save":
        spesifikasi.save()
    elif cmd == "help":
        spesifikasi.helps(logged)
    elif cmd == "exit":
        spesifikasi.exit_game()
    elif cmd == "summonjinplus":
        spesifikasi.summonjinplus(logged)
    else:
        print('Input anda salah, gunakan command "help" untuk menampilkan daftar command.')

