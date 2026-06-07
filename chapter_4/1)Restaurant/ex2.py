USERS = {'alice': '1234', 'bob': 'abcd', 'sara': 'pass1'}

def login_system():
    username = input('Username: ').strip()
    password = input('Password: ').strip()

    if username in USERS and USERS[username] == password:
        print('Login successful')
    else:
        print('Access denied')

login_system()