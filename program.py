from fungsi import musa
from fungsi import panjang
from fungsi import login

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
        logged = []
        masuk = False