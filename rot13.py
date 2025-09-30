
def rot13(text):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result

message = "Hello world"

encoded = rot13(message)
print("encoded :", encoded)

decoded = rot13(encoded)
print("decoded :", decoded)