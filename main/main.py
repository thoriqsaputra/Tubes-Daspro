import spesifikasi, argparse, time

logged = ["",""] # Array user logged [username, role]


parser = argparse.ArgumentParser()
parser.add_argument("path", nargs='?', type=str) #menerima input bertipe string & bersifat positional (parameter spesifik) -
args = parser.parse_args()                       # dan hanya menerima input 0 s/d 1 argument
spesifikasi.cekPath(args.path)

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
message2 = "Permainan dimulai! gunakan command 'help' untuk melihat daftar command yang ada.\n"

for i in range(len(message1)):
    print(message1[i], end='', flush=True)
    time.sleep(0.0000000000001)
for i in range(len(message2)):
    print(message2[i], end='', flush=True )
    time.sleep(0.03)
print()

while True:
    
    cmd = input(">>> ")

    if logged[1] == "" and cmd!= "logout" and cmd != "login" and cmd != "help" and cmd != "exit":
        print('\nInput anda salah, gunakan command "help" untuk menampilkan daftar command.\n')
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
        spesifikasi.ayamberkokok()
    elif cmd == "save":
        spesifikasi.save()
    elif cmd == "help":
        spesifikasi.helps(logged)
    elif cmd == "exit":
        spesifikasi.exit_game()
    else:
        print('Input anda salah, gunakan command "help" untuk menampilkan daftar command.')

