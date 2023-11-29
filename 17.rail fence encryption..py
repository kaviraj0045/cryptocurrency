def sequence(n):
    return list(range(n)) + list(range(n-1,0,-1))

def railfence(s, n):
    s = s.lower()
    L = sequence(n)
    L = L[:len(s)]
    print("The raw sequence of indices: ", L)
    print("The row indices of the characters in the given string: ", L)
    print("Transformed message for encryption: ", s)
    num = 0
    cipher_text = ""
    while num < n:
        for i in range(L.count(num)):
            cipher_text = cipher_text + s[L.index(num)]
            L[L.index(num)] = n
        num += 1
    print("The cipher text is: ", cipher_text)

plain_text = input("Enter the string to be encrypted: ")
n = int(input("Enter the number of rails: "))
railfence(plain_text, n)
