def encode(password):
    new_password = ''

    for char in password:
        new_password += (str((int(char)+ 3) % 10))

    return new_password

<<<<<<< HEAD
def main():
    while(True):
        encoded_value = 0
        decoded_value = 0

        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        option = int(input('Please enter an option: '))
        
        if option == 1:
            pw = input('Please enter the password to encode: ')
            encoded_value = encode(pw)
            print('Your password has been encoded and stored!')
        
        elif option == 2:
            decoded_value = decode(encoded_value)
            print('The encoded password is', str(encoded_value) + ', and the original password is', str(decoded_value) + '.')

        elif option == 3:
            break

if __name__ == '__main__':
    main()
=======
def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str(((int(char)+10)-3) % 10)

    return decoded_password
>>>>>>> a716275726afa39eb8d1f39ee44a2d0bb0822bc4
