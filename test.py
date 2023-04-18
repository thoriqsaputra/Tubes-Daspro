# import os
# userpassrole = ["" for i in range(102)]
# candi = ["" for i in range(100)]
# bahan_bagunan = ["" for i in range(3)]
# userpassrole[0] = "Bondowoso;cintaroro;bandung_bondowoso"
# userpassrole[1] = "Roro;gasukabondo;roro_jonggrang"
# userpassrole[5] = "Roro;gasukabondo;roro_jonggrang"
# folder_name = "batman"

# if not os.path.exists(f"my_folder/{folder_name}"):
#     if not os.path.exists("save"):
#         os.mkdir("my_folder")
#         os.mkdir(f"my_folder/{folder_name}")
#     print(f"Folder '{folder_name}' created successfully.")
# else:
#     print(f"Folder '{folder_name}' already exists.")

# file = open(f"my_folder/{folder_name}/user.cv","w")

# for i in range(102):
#     file.write(f"{userpassrole[i]}\n")
# for i in range(100):
#     file.write(f"{candi[i]}\n")

def LCG(seed, n):
    if n == 0:
        return seed
    else:
        new_seed = (1664525 * LCG(seed, n-1) + 1013904223) % (2**32)
        return new_seed

for i in range(10):
    random_number = (LCG(seed=1234, n=i) % 5) + 1
    print(random_number)
