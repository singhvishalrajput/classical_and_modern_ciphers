
def atbash(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result  += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result


message = "Vishal"

encoded  = atbash(message)
print("encoded :", encoded)

decoded = atbash(encoded)
print("decoded :", decoded)