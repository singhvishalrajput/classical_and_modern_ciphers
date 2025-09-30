def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
        
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)


message = "password"
shift = 3

encrypted = encrypt(message, shift)
print("encrypted message :", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted message :", decrypted)