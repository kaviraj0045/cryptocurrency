def decrypt():
    encrypted_message = input("Enter the message to be decrypted: ").strip()
    k = int(input("Enter the key to decrypt: "))
    letters = "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ''.join([letters[(letters.find(ch) - k) % 26] if ch in letters else ch for ch in encrypted_message])
    print("Your decrypted message is:\n", decrypted_message)
decrypt()
