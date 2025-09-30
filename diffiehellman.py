
p = int(input("Enter a prime number :"))
g = int(input("Enter a primitive root modulo p(g) : "))

a = int(input("Enter Alice's private key(a): "))
b = int(input("Enter Bob's private key(b) : "))

A = (g ** a) % p
B = (g ** b) % p

print(f"Alice's public key : {A}")
print(f"Bob's public key : {B}")

key_alice = (B ** a) % p
key_bob = (A ** b) % p

print(f"Alice's shared key: {key_alice}")
print(f"Bob's shared key: {key_bob}")
