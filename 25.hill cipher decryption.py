import string
import numpy as np

main = string.ascii_lowercase

def generate_key(n, s):
    s = s.replace(" ", "").lower()
    key_matrix = ['' for _ in range(n)]
    i, j = 0, 0
    for c in s:
        if c in main:
            key_matrix[i] += c
            j += 1
            if j > n - 1:
                i += 1
                j = 0
    print("The key matrix (" + str(n) + 'x' + str(n) + ") is:")
    for row in key_matrix:
        print(row)

    key_num_matrix = [[ord(c) - ord('a') for c in row] for row in key_matrix]
    return key_num_matrix

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

def method(a, m):
    if a > 0:
        return a % m
    else:
        k = (abs(a) // m) + 1
        return method(a + k * m, m)

def message_matrix(s, n):
    s = s.replace(" ", "").lower()
    final_matrix = []

    if len(s) % n != 0:
        for _ in range(abs(len(s) % n)):
            s += 'z'

    print("Converted cipher_text for decryption:", s)

    for k in range(len(s) // n):
        message_matrix = []
        for i in range(n):
            sub = [[ord(s[i + (n * k)]) - ord('a')]]
            message_matrix.append(sub)
        final_matrix.append(message_matrix)

    print("The column matrices of plain text in numbers are:")
    for i in final_matrix:
        print(i)

    return final_matrix

def multiply_and_convert(key, message):
    res_num = [[0 for _ in range(len(message[0]))] for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message[0])):
            for k in range(len(message)):
                res_num[i][j] += key[i][k] * message[k][j]

    res_alpha = [[chr((res_num[i][j] % 26) + 97) for j in range(len(message))] for i in range(len(key))]
    return res_alpha

n = int(input("What will be the order of square matrix: "))
s = input("Enter the key: ")
key_matrix = generate_key(n, s)
A = np.array(key_matrix)
det = np.linalg.det(A)
adjoint = det * np.linalg.inv(A)

if det != 0:
    convert_det = modInverse(int(det), 26)
    adjoint = adjoint.tolist()

    for i in adjoint:
        for j in i:
            j = round(j)
            j = method(j, 26)

    adjoint = np.array(adjoint)
    inverse = convert_det * adjoint
    inverse = inverse.tolist()

    for i in inverse:
        for j in i:
            j %= 26

    cipher_text = input("Enter the cipher text: ")
    message = message_matrix(cipher_text, n)
    plain_text = ''

    for i in message:
        sub = multiply_and_convert(inverse, i)
        for j in sub:
            for k in j:
                plain_text += k

    print("plain message:", plain_text)
else:
    print("Matrix cannot be inverted")
