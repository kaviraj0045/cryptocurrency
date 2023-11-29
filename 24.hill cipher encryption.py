import string

def generate_key(n, s):
    s = s.replace(" ", "").lower()
    key_matrix = [['' for _ in range(n)] for _ in range(n)]
    i, j = 0, 0
    for c in s:
        if c in string.ascii_lowercase:
            key_matrix[i][j] = c
            j += 1
            if j >= n:
                i += 1
                j = 0
    print("The key matrix (" + str(n) + 'x' + str(n) + ") is:")
    for row in key_matrix:
        print(row)

    key_num_matrix = [[ord(c) - ord('a') for c in row] for row in key_matrix]
    return key_num_matrix

def message_matrix(s, n):
    s = s.replace(" ", "").lower()
    final_matrix = []

    if len(s) % n != 0:
        s += 'z' * (n - len(s) % n)

    print("Converted plain_text for encryption:", s)

    for k in range(0, len(s), n):
        message_matrix = []
        for i in range(n):
            sub = [[ord(s[k + i]) - ord('a')]]
            message_matrix.append(sub)
        final_matrix.append(message_matrix)

    print("The column matrices of plain text in numbers are:")
    for i in final_matrix:
        print(i)

    return final_matrix

def determinant(mat, n):
    if n == 1:
        return mat[0][0]

    D = 0
    temp = [[0 for _ in range(n)] for _ in range(n)]
    sign = 1

    for f in range(n):
        getCofactor(mat, temp, 0, f, n)
        D += (sign * mat[0][f] * determinant(temp, n - 1))
        sign = -sign

    return D

def isInvertible(mat, n):
    return determinant(mat, n) != 0

def multiply_and_convert(key, message):
    res_num = [[0 for _ in range(len(message))] for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message)):
            for k in range(len(message[0])):
                res_num[i][j] += key[i][k] * message[k][j]

    res_alpha = [[chr((res_num[i][j] % 26) + 97) for j in range(len(message))] for i in range(len(key))]
    return res_alpha

n = int(input("What will be the order of square matrix: "))
s = input("Enter the key: ")
key = generate_key(n, s)

if isInvertible(key, len(key)):
    print("Yes it is invertable and can be decrypted")
else:
    print("No it is not invertable and cannot be decrypted")

plain_text = input("Enter the message: ")
message = message_matrix(plain_text, n)
final_message = ''

for i in message:
    sub = multiply_and_convert(key, i)
    for j in sub:
        final_message += ''.join(j)

print("plain message:", plain_text)
print("final encrypted message:", final_message)
