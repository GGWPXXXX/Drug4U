import csv


def read_external_file(file_name):
    data_list = []
    with open(file_name) as temp_var:
        file = csv.DictReader(temp_var)
        for each_line in file:
            data_list.append(each_line)
    return data_list


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
        for each_dict in data:
            if username in each_dict['username'] and password in each_dict['password']:
                return username, password
        print('Sorry your username or pass must be wrong please try again :o')
        username = input('Your username?: ')
        password = input('And password?: ')


def update_customer_data(data, username, password, address, telephone):
    with open(data) as file:
        data_file = csv.DictReader(file)
        for each_file in data_file:
            if each_file['username'] == username:
                each_file['username'] = username
                each_file['password'] = password
                each_file['address'] = address
                each_file['telephone'] = telephone


class Customer:
    def __init__(self, username, password, address, telephone_number):
        self.__username = username

    def welcome_user(self):
        print(f'Hi {self.__username} welcome to my shop :)')


user_file = '../Drug4U/User_file/User_data.csv'
customer_data = (read_external_file(user_file))
admin_data = read_external_file('../Drug4U/Admin_file/Admin_data.csv')
print('''
===========================
Welcome to My DRUG4U Shop!
===========================
''')
print('Are you a customer?')
check_wheter_customer = input('(y/n): ')
check_wheter_customer = check_y_n(check_wheter_customer)

if check_wheter_customer == 'n' or check_wheter_customer == 'N':
    print('============================')
    print("Then you must be an admin :)")
    print("Please login")
    print('============================')
    username, password = login(admin_data)

if check_wheter_customer == 'y' or check_wheter_customer == 'Y':
    print('Do you have an account?')
    check_account = input('(y/n): ')
    check_account = check_y_n(check_account)
    if check_account == 'n' or check_account == 'N':
        create_an_account(user_file)
        customer_data = (read_external_file(user_file))

username, password = login(customer_data)
