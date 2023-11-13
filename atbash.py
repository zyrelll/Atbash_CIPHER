def decrypt(message, matrix):
    decrypted_message = ""
    for char in message:
        if char == " ": 
            decrypted_message += " "
        else:
            index = matrix[2 if char.islower() else 3].index(char)
            decrypted_message += matrix[0 if char.islower() else 1][index]
    return decrypted_message

def input_message():
    while(True):
        encrypted_message = input("Enter encrypted message: ")
        if encrypted_message.isalpha(): 
            break
        else:
            print("Invalid input. Please enter a string without digits or symbols.")
    return encrypted_message

alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
reversed_ua = ''.join(reversed(upper_alphabet))
reversed_alphabet = ''.join(reversed(alphabet))
matrix = [list(alphabet), list(upper_alphabet), list(reversed_alphabet), list(reversed_ua)]

encrypted_message = input_message()
decrypted_message = decrypt(encrypted_message, matrix)

print("Decrypted message: ", decrypted_message)
