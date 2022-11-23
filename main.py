import json


def read_external_file(file_name):
    with open(file_name, 'r') as file:
        data_file = json.load(file)
        return data_file


def create_an_account(file_path):
    print('===============================')
    print('Hi this is registration form :)')
    print('===============================')
    username = input('What should we call you?: ')

    # Check if the username has been used.
    with open(file_path, 'r') as file:
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
    # read an old data then save it in data_file variable
    with open(file_path, 'r') as file:
        data_file = json.load(file)
        data_file.update(new_data)

    # write down new data
    with open(file_path, 'w') as file:
        json.dump(data_file, file, indent=4)


def check_y_n(choice):
    choice_list = ['n', 'N', 'y', 'Y']
    while choice not in choice_list:
        print('Please type (y/n)')
        choice = input('(y/n): ')
        if choice in choice_list:
            return choice
    return choice


def login(file_path):
    print('========================')
    print('Hi welcome to login page')
    print('Please type in your username and password :)')
    print('========================')
    username = input('Your username?: ')

    # check username that if it's in database or not.
    with open(file_path, 'r') as file:
        data_file = json.load(file)
        while username not in data_file:
            print(f'Sorry, Username:{username} not found on the system.')
            username = input('Your username?: ')
    password = input('And password?: ')

    # check the given password that if it's match with the username or not.
    with open(file_path, 'r') as file:
        data_file = json.load(file)
        while password != data_file[username]['password']:
            print(f'Sorry, your given password does not match with the username, Please try again.')
            password = input('And password?: ')
    return username


class Customer:
    def __init__(self, username):
        self.__username = username

    # getter for username
    @property
    def username(self):
        return self.__username

    # setter for username
    @username.setter
    def username(self, new_value):
        self.__username = new_value

    # welcome customer text
    def welcome_user(self):
        print('============================')
        print(f'Hi {self.__username} welcome to my shop :)')
        print('============================')

    # Show menu
    def menu(self):
        print('Please select Menu :)')
        print('1.Medicine Store')
        print('2.Setting')
        menu_choice = int(input('Please input number:) '))

        # Check if user input is the correct menu number or not.
        while True:
            if menu_choice == 1 or menu_choice == 2:
                return menu_choice
            menu_choice = int(input('Please input the correct number :( '))

    # Show medine menu
    def show_medicine(self):



user_file_path = '../Drug4U/User_file/User_data.json'
customer_data = (read_external_file(user_file_path))
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
    username = login(admin_data)

if check_wheter_customer.lower() == 'y':
    print('Do you have an account?')
    check_account = input('(y/n): ')
    check_account = check_y_n(check_account)
    if check_account.lower() == 'n':
        create_an_account(user_file_path)
        customer_data = (read_external_file(user_file_path))
    print('============================')
    print("Please login")
    username = login(user_file_path)
    customer = Customer(username)
    customer.welcome_user()
    customer_choice = customer.menu()
