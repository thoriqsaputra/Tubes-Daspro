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

# def LCG(seed, n):
#     if n == 0:
#         return seed
#     else:
#         new_seed = (1664525 * LCG(seed, n-1) + 1013904223) % (2**32)
#         return new_seed

# for i in range(10):
#     random_number = (LCG(seed=1234, n=i) % 5) + 1
#     print(random_number)

# indeksundo = 0
# arr_undo = ["" for i in range(100)]
# def arrs_undo(jin_kehapus):
#     global arr_undo, indeksjin
#     arr_undo[indeksjin] = jin_kehapus
#     indeksundo += 1

# while True:
#     b = input()
#     arrs_undo(b)
#     print(arr_undo)
#     print(indeksjin)
#     if indeksjin == 4:
#         break

# print(arr_undo[0])

# # Initialize an empty array of length 15
# arr = [""] * 15

# # Fill some of its elements
# arr[0] = "apple"
# arr[1] = "banana"
# arr[2] = "orange"
# arr[3] = "pear"
# arr[4] = "grape"

# # Set the 3rd element (index 2) to an empty string
# arr[0] = ""

# # Loop through the array starting from the 4th element (index 3)
# for i in range(1, len(arr)):
#     # Move the current element to the previous index
#     arr[i-1] = arr[i]

# print(arr)

undo_jin = ["" for i in range(100)]

for i in range(3):
    undo_jin[i][0] = input()

print(undo_jin)
# jinhapus = "batman"

# for i in range(5):
#        undo_jin[i] = input()
# indeksjin = 0
# for i in range(100):
#     if undo_jin[i] == jinhapus:
#         undo_jin[i] = ""
#         indeksjin = i
#         break
# for i in range(indeksjin+1,100):
#     undo_jin[i-1] = undo_jin[i]

# print(undo_jin)
