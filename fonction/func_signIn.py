
def singIn( name_user = input('Enter your name>>> '),
            password = input('Enter your password>>> ')):

    users  = {
        'user1' : {
            'name_user': 'John',
            'password' : '23322332'
        },
        'user2' : {
            'name_user': 'Mary',
            'password' : '32233223'
        },
        'user3' : {
            'name_user': 'Danil',
            'password' : '22332233'
        }
    }
    if name_user == users["user1"]['name_user'] and password == users["user1"]['password']:
        a = users['user1']
        print(a)
    if name_user != users["user1"]['name_user'] and password == users["user1"]['password']:
        print('You entered the wrong name!!!')
    if name_user == users["user1"]['name_user'] and password != users["user1"]['password']:
        print('You entered the wrong password!!!')
    if name_user != users["user1"]['name_user'] and password != users["user1"]['password']:
        print('You entered the wrong name and password!!!')


    if name_user == users["user2"]['name_user'] and password == users["user2"]['password']:
        x = users['user2']
        print(x)
    if name_user != users["user2"]['name_user'] and password == users["user2"]['password']:
        print('You entered the wrong name!!!')
    if name_user == users["user2"]['name_user'] and password != users["user2"]['password']:
        print('You entered the wrong password!!!')


    if name_user == users["user3"]['name_user'] and password == users["user3"]['password']:
        y = users['user3']
        print(y)
    if name_user != users["user3"]['name_user'] and password == users["user3"]['password'] :
        print('You entered the wrong name!!!')
    if name_user == users["user3"]['name_user'] and password != users["user3"]['password']:
        print('You entered the wrong password!!!')


singIn()