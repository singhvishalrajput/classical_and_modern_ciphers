
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

n = p*q
phi  = (p-1) * (q-1)

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break

    e += 1

d = 1

while (d*e) % phi != 1:
    d += 1

print(f"Public Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")

message = int(input("Enter message(as number): "))
cipher = (message ** e) % n
print("encrypted :", cipher)

decipher = (cipher ** d) % n
print("decrypted :", decipher)

