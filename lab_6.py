def encoder(var):
    encode_password = ""
    for char in var:
        char = int(char)
        char += 5
        encode_password += str(char)
    return encode_password
if __name__ == "__main__":
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option:")
        if choice == 1:
            char = input("Please enter your password to encode:")
            password = encoder(var)
            print("Your password has been encoded and stored")
        elif choice == 2:
            pass
        elif choice == 3:
            exit()