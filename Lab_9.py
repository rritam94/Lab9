def encode(password):
    new_password = ''

    for char in password:
        new_password += (str((int(char)+ 3) % 10))

    return new_password
