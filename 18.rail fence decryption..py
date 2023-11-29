def sequence(n):
    return list(range(n)) + list(range(n - 1, 0, -1))

def railfence(cipher_text, n):
    cipher_text = cipher_text.lower()
    L = sequence(n)
    L = L[:len(cipher_text)]
    print("The raw sequence of indices: ", L)
    temp1 = sorted(L)
    print("The row indices of the characters in the cipher string: ", L)
    print("The row indices of the characters in the plain string: ", temp1)
    print("Transformed message for decryption: ", cipher_text)
    plain_text = ""
    for i in L:
        k = temp1.index(i)
        temp1[k] = n
        plain_text += cipher_text[k]
    print("The cipher text is: ", plain_text)

cipher_text = "horel ollwd"
n = 3
railfence(cipher_text, n)
