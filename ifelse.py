
registredPassword = 'M1234'

username = input("Username: ")
password = input("Password: ")


if password == registredPassword:
    print('Wellcome ' + username)
else:
    print('Wrong password')