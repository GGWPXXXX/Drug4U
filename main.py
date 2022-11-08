def read_external_file(file_name):                                        #This fucntion read user's username and password text file
    file = open(file_name, 'r', encoding='utf-8').read().splitlines()     #then reteturn them as dict.
    user_list = []
    for each_line in file:
        user_list.append(each_line.split(' '))
    lldict = dict(user_list)
    return lldict


def create_an_account(filename):
    print('===============================')
    print('Hi this is registration form :)')
    print('===============================')
    username = input('What should we call you?: ')
    print('===============================')
    print(f'Hi {username} Nice to meet ya :)')
    print('===============================')
    password = input('And what will  your password be?: ')
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(username)
        file.write(' ')
        file.write(password)


def check_y_n(choice):
    choice_list = ['n', 'N', 'y', 'Y']
    while choice not in choice_list:
        print('Please type (y/n)')
        choice = input('(y/n): ')
        if choice in choice_list:
            return choice
    return choice


def login(data):
    print('========================')
    print('Hi welcome to login page')
    print('Please type in your username and password :)')
    print('========================')
    username = input('Your username?: ')
    password = input('And password?: ')
    while True:
        if username in data.keys() and password == data[username]:
            return username, password
        print('Sorry your username or pass must be wrong please try again :o')
        username = input('Your username?: ')
        password = input('And password?: ')


class User:
    def __init__(self, username):
        self.username = username

    def welcome_user(self):
        print(f'Hi {self.username} welcome to my shop :)')


user_file = '../Drug4U/User_file/username_pass.txt'
customer_data = (read_external_file(user_file))
print('''
===========================
Welcome to My DRUG4U Shop!
===========================
''')
print('Are you a customer?')
check_wheter_customer = input('(y/n): ')
check_wheter_customer = check_y_n(check_wheter_customer)

if check_wheter_customer == 'n' or check_wheter_customer == 'N':
    print("Then you must be an admin :)")
    print("Please login")

if check_wheter_customer == 'y' or check_wheter_customer == 'Y':
    print('Do you have an account?')
    check_account = input('(y/n): ')
    check_account = check_y_n(check_account)
    if check_account == 'n' or check_account == 'N':
        create_an_account(user_file)
    if check_account == 'y' or check_account == 'Y':
        username, password = login(customer_data)
        User = User(username)
