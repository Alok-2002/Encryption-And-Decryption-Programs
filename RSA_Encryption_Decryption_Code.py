import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return (gcd, y, x - (a // b) * y)
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        return None
    else:
        return x % phi

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

public_key,private_key = generate_keypair(7,11)

message = input("Enter The Message: ")
print("Original Message is: ",message)

cipher = encrypt(public_key,message)
print("Encrypted Message: ",cipher)

plain = decrypt(private_key,cipher)
print("Decrypted Message: ",plain)
