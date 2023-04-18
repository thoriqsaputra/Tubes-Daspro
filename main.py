
from spesifikasi import login, logout


logged = ""
masuk = False
while True:
    x = input(">>> ")
    if masuk == False and x != "login" and x != "help":
        print("You must login in order to continue or type Help for list of commands.")
    elif x == "login":
        logged = login(logged)
        masuk = True
    elif x == "logout":
        logged = logout(logged)
        masuk = False