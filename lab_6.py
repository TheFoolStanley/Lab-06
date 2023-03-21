def encoder(var):
    encode_password = ""
    for char in var:
        char = int(char)
        char += 3
        encode_password += str(char)
    return encode_password


def decode(password):
    decoded_password = ""
    for i in password:
        i = int(i)
        i -= 3
        decoded_password += str(i)
    return decoded_password


if __name__ == "__main__":
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            var = input("Please enter your password to encode: ")
            password = encoder(var)
            print("Your password has been encoded and stored!")
            print()
        elif choice == 2:
            decoded_password = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded_password}")
        elif choice == 3:
            break
