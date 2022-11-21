import json


def read_external_file(file_name):
    with open(file_name, 'r') as file:
        data_file = json.load(file)
        return data_file


def create_an_account(filename):
    print('===============================')
    print('Hi this is registration form :)')
    print('===============================')
    username = input('What should we call you?: ')
    # Check if the username has been used.
    with open(filename, 'r') as file:
        data_file = json.load(file)
        while username in data_file:
            print('Sorry, this username has already been used.')
            username = input('What should we call you?: ')

    print('===============================')
    print(f'Hi {username} Nice to meet ya :)')
    print('===============================')
    password = input('And what will your password be?: ')
    print('PETFECTOOOO!!')
    address = input('Now the address for your shipping: ')
    tel = input('Your telephone number please:) ')
    new_data = {
        username: {
            "password": password,
            "address": address,
            "telephone": tel
        }
    }
    with open(filename, 'r') as file:
        data_file = json.load(file)
        data_file.update(new_data)
    with open(filename, 'w') as file:
        json.dump(data_file, file, indent=4)


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


# def update_customer_data(data, username, password, address, telephone):
#     with open(data) as file:
#         data_file = csv.DictReader(file)
#         for each_file in data_file:
#             if each_file['username'] == username:
#                 each_file['username'] = username
#                 each_file['password'] = password
#                 each_file['address'] = address
#                 each_file['telephone'] = telephone


class Customer:
    def __init__(self, username, password, address, telephone_number):
        self.__username = username

    def welcome_user(self):
        print(f'Hi {self.__username} welcome to my shop :)')


user_file = '../Drug4U/User_file/User_data.json'
customer_data = (read_external_file(user_file))
admin_data = read_external_file('../Drug4U/Admin_file/Admin_data.json')
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

if check_wheter_customer.lower() == 'y':
    print('Do you have an account?')
    check_account = input('(y/n): ')
    check_account = check_y_n(check_account)
    if check_account.lower() == 'n':
        create_an_account(user_file)
        customer_data = (read_external_file(user_file))

username, password = login(customer_data)
