
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    msg=input("Enter your message:")
    key=int(input("enter key(1-94):"))

    encrypted_text = ""
    for i in range(len(msg)):
        temp = (ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32

        encrypted_text+=chr(temp)
    print("Encrypted: "+encrypted_text)
    main()

def decryption():
    print("decryption")
    print("message can only be lower or upper case")
    encrp_msg = input("enter encrypted text :")
    decrp_key = int(input("enter key(1-94):"))
    decrypted_text = ""
    for i in range(len(encrp_msg)):
        temp = (ord(encrp_msg[i])-decrp_key)
        if(temp<32):
            temp=temp+127-32

        decrypted_text+=chr(temp)
    print("decrypted text: "+decrypted_text)
    main()



        
if __name__ == "__main__":
    main()
