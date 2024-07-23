def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str(((int(char)+10)-3) % 10)

    return decoded_password

def encode(password):
    new_password = ''

    for char in password:
        new_password += (str((int(char)+ 3) % 10))

    return new_password

def main():
    encoded_value = 0
    decoded_value = 0
    while(True):    
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        option = int(input('Please enter an option: '))
        
        if option == 1:
            pw = input('Please enter the password to encode: ')
            encoded_value = encode(pw)
            print('Your password has been encoded and stored!\n')
        
        elif option == 2:
            decoded_value = decode(str(encoded_value))
            print('The encoded password is', str(encoded_value) + ', and the original password is', str(decoded_value) + '.')
            print()

        elif option == 3:
            break

if __name__ == '__main__':
    main()

