def decrypt(message, matrix):
    decrypted_message = ""
    for char in message:
        if char == " ":
            decrypted_message += " "
        else:
            index = matrix[1].index(char)
            decrypted_message += matrix[0][index]
    return decrypted_message

alphabet = 'abcdefghijklmnopqrstuvwxyz'
reversed_alphabet = ''.join(reversed(alphabet))
matrix = [list(alphabet), list(reversed_alphabet)]

encrypted_message = "ovdrh xsvhhnvm"  # insert encrypted message here
decrypted_message = decrypt(encrypted_message, matrix)

print("Decrypted message: ", decrypted_message)
