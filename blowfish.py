
key = "MYSECRET"
key_val = sum(bytearray(key.encode()))  


def F(x, key_val):
    return (x ^ key_val) % 256  


def blowfish_encrypt(text, key_val):
    print("Encryption:")
    if len(text) % 2 != 0:
        text += "X"

    encrypted = []
    for i in range(0, len(text), 2):  
        left, right = ord(text[i]), ord(text[i+1])
        for r in range(1, 17):  # 16 rounds
            left, right = right, left ^ F(right, key_val)
        encrypted.append((left, right))
    return encrypted


def blowfish_decrypt(pairs, key_val):
    print("Decryption:")
    decrypted = ""
    for left, right in pairs:
        for r in range(16, 0, -1):  # reverse rounds
            left, right = right ^ F(left, key_val), left
        decrypted += chr(left) + chr(right)
    return decrypted

# --- Run Demo ---
data = "iamvishalsingh"
cipher = blowfish_encrypt(data, key_val)
print("Encrypted (conceptual):", cipher)

plain = blowfish_decrypt(cipher, key_val)
print("Decrypted:", plain)
