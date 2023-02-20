import re
import validate_email
def signUp(name_user = input('Enter your name>>> '),
           email = input('Enter your email>>> '),
           password = input('Enter your password>>> ')):
    gmail = validate_email.validate_email(email)
    data_user = {
        'name_user':'Morison',
        'email':'secret@gmail.com',
        'password':'qwerty123'
    }
    print()
    if len(name_user) < 5 or len(name_user) > 12 :
        print('Not less than 5 and not more than 12 lines')
    if re.search(r'[^a-zA-Z]', name_user):
        print("Enter name in latin")
    if gmail:
        print('Email address exists')
    else:
        print('Email address is not correct')
    if len(password) < 8:
        print('At least 8 characters')
    if name_user == data_user['name_user'] and email == data_user['email'] and password == data_user['password']:
        x = data_user
        print(x)
    if name_user != data_user['name_user'] :
        print('You entered the wrong name!!!')
    if email != data_user['email'] :
        print('You entered the wrong email!!!')
    if password != data_user['password']:
        print('You entered the wrong password!!!')
signUp()

