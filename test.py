import os
userpassrole = ["" for i in range(102)]
candi = ["" for i in range(100)]
bahan_bagunan = ["" for i in range(3)]
userpassrole[0] = "Bondowoso;cintaroro;bandung_bondowoso"
userpassrole[1] = "Roro;gasukabondo;roro_jonggrang"
userpassrole[5] = "Roro;gasukabondo;roro_jonggrang"
folder_name = "batman"

if not os.path.exists(f"my_folder/{folder_name}"):
    if not os.path.exists("save"):
        os.mkdir("my_folder")
        os.mkdir(f"my_folder/{folder_name}")
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

file = open(f"my_folder/{folder_name}/user.cv","w")

for i in range(102):
    file.write(f"{userpassrole[i]}\n")