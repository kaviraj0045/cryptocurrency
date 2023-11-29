import string

key = input("Enter key").upper().replace(" ", "")
key = key.replace("J", "I")
other_chars = "".join(c for c in string.ascii_uppercase if c not in key and c != "J")
key += other_chars

matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(25):
    matrix[i // 5][i % 5] = key[i]

def locindex(c):
    if c == "J":
        c = "I"
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if c == char:
                return [i, j]

def encrypt():
    msg = input("ENTER MSG:").upper().replace(" ", "")
    for i in range(0, len(msg) + 1, 2):
        if i < len(msg) - 1 and msg[i] == msg[i + 1]:
            msg = msg[:i + 1] + "X" + msg[i + 1:]
    if len(msg) % 2 != 0:
        msg += "X"

    print("CIPHER TEXT:", end=" ")
    for i in range(0, len(msg), 2):
        loc1 = locindex(msg[i])
        loc2 = locindex(msg[i + 1])

        if loc1[1] == loc2[1]:
            print(matrix[(loc1[0] + 1) % 5][loc1[1]], matrix[(loc2[0] + 1) % 5][loc2[1]], end=" ")
        elif loc1[0] == loc2[0]:
            print(matrix[loc1[0]][(loc1[1] + 1) % 5], matrix[loc2[0]][(loc2[1] + 1) % 5], end=" ")
        else:
            print(matrix[loc1[0]][loc2[1]], matrix[loc2[0]][loc1[1]], end=" ")

def decrypt():
    msg = input("ENTER CIPHER TEXT:").upper().replace(" ", "")
    print("PLAIN TEXT:", end=" ")

    for i in range(0, len(msg), 2):
        loc1 = locindex(msg[i])
        loc2 = locindex(msg[i + 1])

        if loc1[1] == loc2[1]:
            print(matrix[(loc1[0] - 1) % 5][loc1[1]], matrix[(loc2[0] - 1) % 5][loc2[1]], end=" ")
        elif loc1[0] == loc2[0]:
            print(matrix[loc1[0]][(loc1[1] - 1) % 5], matrix[loc2[0]][(loc2[1] - 1) % 5], end=" ")
        else:
            print(matrix[loc1[0]][loc2[1]], matrix[loc2[0]][loc1[1]], end=" ")

while True:
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))

    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        exit()
    else:
        print("Choose correct choice")
