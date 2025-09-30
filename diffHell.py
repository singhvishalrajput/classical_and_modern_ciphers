
p =  int(input("Enter the prime number: "))
g = int(input("Enter the generator: "))


print("Now lets move to getting the secret key: ") 
a = int(input("enter a's secret: "))
b = int(input("enter b's secret: "))

print("lets generate the public key for a and b")

A = (g ** a) % p
B = (g ** b) % p

print("let's generate the shared secret: ")

ka = (B ** a) % p
kb = (A ** b)%p

if ka == kb:
    print(f"The shared secret key is {ka}")

