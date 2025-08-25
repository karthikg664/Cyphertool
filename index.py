# program starts with greeting function
def greeting():
    print("Welcome! This is a cyphertool")
    print(
        """
          !!!Rules!!!
          >Original alphabet:- a b c d e f g h i j k l m n o p q r s t u v w x y z
          >Substitution alphabet:- Define your's or same as original
          """
    )
    main()


# main menu function
def main():
    print(
        """
          1. Encrypt a message
          2. Decrypt a message
          3. Exit
          """
    )
    choice = int(input("What you want to do: "))
    if choice == 1 or choice == 2:
        enter(choice)
    elif choice == 3:
        exit()
    else:
        print("!!!Invalid Input!!!")
        main()


# input function
def enter(choice):
    original = input("Enter original alphabet (e.g., abcdefghijklmnopqrstuvwxyz): ")
    sub = input("Enter substitution alphabet (e.g., shuffled letters for substitution): ")
    if len(original) == len(sub) and (
        len(set(original)) == len(original) and len(set(sub)) == len(sub)
    ):
        message = input("Enter the message to process: ")
        if choice == 1:
            mapped = {original[i]: sub[i] for i in range(len(original))}
            print("Mapping created! You may now encrypt your message.")
            encrypt(mapped, message)
        else:
            mapped = {original[i]: sub[i] for i in range(len(original))}
            print("Reverse mapping created! You may now decrypt your message.")
            decrypt(mapped, message)
    else:
        print("!!!Invalid Input!!!")
        main()
        return


# encrypt function
def encrypt(mapped, message):
    encrypted_message = ""
    for char in message:
        if char.lower() in mapped:
            mapped_char=mapped[char.lower()]
            if char.isupper():
                mapped_char=mapped_char.upper()
            encrypted_message += mapped_char
        else:
            encrypted_message += char
    print("Encrypted message:", encrypted_message)

# decrypt function
def decrypt(mapped, message):
    decrypted_message = ""
    for char in message:
        if char.lower() in mapped:
            mapped_char=mapped[char.lower()]
            if char.isupper():
                mapped_char=mapped_char.upper()
            decrypted_message += mapped_char
        else:
            decrypted_message += char
    print("Decrypted message:", decrypted_message)

greeting()


# original    = a s d q w e g h j t y u i o
# substitution= z x e f c v u k b n m p h t
# message  = hello my name is karthik and i am 23 years old!!!
# expected encrypted output= kvllt mm nzmv hx kzrnkhk zne h zm 23 mvzrx tle!!!