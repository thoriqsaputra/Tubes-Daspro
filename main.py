
from spesifikasi import login
from spesifikasi import logout

logged = []
masuk = False
while True:
    x = input(">>> ")
    if masuk == False:
        if x == "login":
            login(logged)
            masuk = True
            continue
    elif x == "logout":
        logout()