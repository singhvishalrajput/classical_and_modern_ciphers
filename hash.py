import hashlib

data = input("Enter the data: ")

sha256_first = hashlib.sha256(data.encode()).hexdigest()
md5_first  = hashlib.md5(data.encode()).hexdigest()

print("SHA-256 hash: ", sha256_first)
print("MD5 hash: ", md5_first)

check_data = input("Enter the data again: ")

sha256_second = hashlib.sha256(check_data.encode()).hexdigest()
md5_second = hashlib.md5(check_data.encode()).hexdigest()


if sha256_first == sha256_second and md5_first == md5_second:
    print("Data is intact (no change)")
else:
    print("Data is modified")