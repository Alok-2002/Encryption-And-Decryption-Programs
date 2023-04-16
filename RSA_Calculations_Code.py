import random
import math

def generate_p_and_q():
    
    p = int(input("Enter The Value Of P: "))
    q = int(input("Enter The Value OF Q: "))

    return p, q

p,q =  generate_p_and_q()

n = p * q
P = p -1
Q = q -1

phi = (P*Q)
print("Value Of N is = ",n,"\nAnd Value Of Φ(N) = ",phi)

def generate_e(phi):
    possible_e_values = []

    for i in range(2,phi):
        if math.gcd(i,phi) == 1: 
            e=i
            possible_e_values.append(e)

#     print("The All Possible Values Are : ",possible_e_values)

    return random.choice(possible_e_values)

e = generate_e(phi)

print("Value Of E is = ",e)


def generate_d(e,phi): 

    # d_list = [] 

    for i in range(2,phi):

        if (i*e) % phi == 1:
            d = i
            # d_list.append(d)
            break

    # print(d_list)
    return d

d = generate_d(e,phi)

print("Value of D is = ",d)

message = random.randint(1,n)

print("Random Generated Message is : ",message)

def encrypt(message,e,n): 
    c = pow(message,e,n)
    return c

Encrypted_Message = encrypt(message,e,n)

print("Encrypted message is : ",Encrypted_Message)

def decrypt(message,d,n): 
    p = pow(message,d,n)
    return p

Decrypted_message = decrypt(Encrypted_Message,d,n)
print("Decrypted Message is : ",Decrypted_message)
