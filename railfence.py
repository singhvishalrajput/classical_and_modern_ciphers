
def encrypt(text):
    rail1, rail2 = "", ""
    for i, char in enumerate(text):
        if i%2 == 0:
            rail1 += char
        else:
            rail2 += char
    return rail1+rail2

def decrypt(cipher):
    mid = (len(cipher) + 1) // 2
    rail1, rail2 = cipher[:mid], cipher[mid:]
    result = ""
    for i in range(len(rail1)):
        result += rail1[i]
        if i < len(rail2):
            result += rail2[i]
    return result

message = "Hello world"
cipher = encrypt(message)
print("Encrypted :", cipher)

decipher = decrypt(cipher)
print("decrypted :", decipher)
        