
from spesifikasi import login, logout, summonjin, hapusjin, ubahjin, save

logged = ["","",False]

while True:

    x = input(">>> ")

    if logged[2] == False and x != "login" and x != "help":
        print("You must login in order to continue or type Help for list of commands.")
    elif x == "login":
        logged = login(logged)
    elif x == "logout":
        logged = logout(logged)
    elif x == "summonjin":
        summonjin(logged)
    elif x == "hapusjin":
        hapusjin(logged)
    elif x == "ubahjin":
        ubahjin(logged)    
    elif x == "save":
        save()
    elif x == "help":
        print("bbb")

