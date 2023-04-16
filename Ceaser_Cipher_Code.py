alphabets = "abcdefghijklmnopqrstuvwxyz"
numberofletters = len(alphabets)
print("*******CEASER CIPHER*******")
def Encrypt(Plain_Text ,Key):
        Cipher_Text = ''
        for letter in Plain_Text :
            letter  = letter.lower()
            if not letter == ' ':
                Index = alphabets.find(letter)
                if Index == -1:
                    Cipher_Text += letter
                else:
                    New_Index =Index + key
                    if New_Index >= numberofletters:
                        New_Index -= numberofletters
                    Cipher_Text += alphabets[New_Index]
        return Cipher_Text


def Decrypt(Cipher_Text ,Key):
        Plain_Text = ''
        for letter in Cipher_Text :
            letter  = letter.lower()
            if not letter == ' ':
                Index = alphabets.find(letter)
                if Index == -1:
                    Plain_Text += letter
                else:
                    New_Index =Index + key
                    if New_Index < 0: 
                        New_Index += numberofletters
                    Plain_Text += alphabets[New_Index]
        return Plain_Text


while True:
    user_input = input('''What Do You Want To Do ?
    1.Perform Encryption
    2.Perform Decryption
    3.Press 0 To Exit ''').upper()

    if user_input == "1":
        print("\n----You've Selected The Option To Encrypt The Plain Text Into Cipher Text----\n")
        key = int(input("Enter The Key Between 1 To 26: "))
        text = input("Enter The Plain Text That You Want To Encrypt: ")
        Cipher_Text = Encrypt(text,key)
        print(f'Your Encrypted Cipher Text  is: {Cipher_Text}')

    elif user_input == "2":
        print("\n----You've Selected The Option To Decrypt The Cipher Text Into Original Plain Text----\n")
        key = int(input("Enter The Key Between 1 To 26: "))
        text = input("Enter The Plain Text That You Want To Decrypt: ")
        Plain_Text = Decrypt(text,key)
        print(f'Your Decrypted Plain Text  is: {Plain_Text}')
    else:
        print("Exiting.....")
        break
        
