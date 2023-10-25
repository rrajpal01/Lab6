def encode(password):
    encoded_pass= ''
    for i in range(len(password)):
        encoded_pass += str((int(password[i])+3))
    return encoded_pass

def decode(encoded_password):
    decoded_pass = ''
    for i in range(len(encoded_password)):
        decoded_pass += str((int(encoded_password[i]) - 3))
    return decoded_pass

if __name__ == '__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode \n2. Decode \n3. Quit')
        option = int(input('Please enter an option:'))
        if option == 1:
            code = input('Please enter you password to encode:')
            print('Your password has been encoded and stored!')
            encoded_code = (encode(code))
        if option == 2:
            decoded_code = decode(encoded_code)
            print(f"The encoded password is {encoded_code}, and the original password is {decoded_code}")


        if option == 3:
            break