import random

characters = " " +"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*!~@#$%^&()|\/<>:;"
characters = list(characters)
key = characters.copy()
random.shuffle(key)
# print(key)

#Encryption Process
def Encryption():
    plain_text = input("Enter The Message To Encrypt : ")
    cipher_text = " "

    for letter in plain_text:
        index = characters.index(letter)
        cipher_text += key[index]

    print("Original Message is :",plain_text)
    print("Encrypted Message is :",cipher_text)

    return

#Decryption Process
def Decryption():
    cipher_text = input("Enter The Message To Decrypt : ")
    plain_text = " "


    for letter in cipher_text:
        index = key.index(letter)
        plain_text += characters[index]

    print("Original Message is :",plain_text)
    return

def Substitution_Cipher():
    while True:
        user_input = input('''"What Do You Want To Do?
        1.Encryption
        2.Decryption
        3.Exit : ''')

        if user_input == "1":
            print("******YOU HAVE SELECTED ENCRYPTION PROCESS*****")
            Encryption()
        elif user_input == "2":
            print("******YOU HAVE SELECTED DECRYPTION PROCESS*****")
            Decryption()
        else:
            print("Exiting...........")
            break
            
            
Substitution_Cipher()
