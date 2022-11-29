import json
from Customer import Customer
from Medicine import Medicine
import os
from time import sleep


def read_external_file(file_name):
    with open(file_name, 'r') as file:
        data_file = json.load(file)
        return data_file


def clear():
    print('\n'*40)


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
    print('PERFECTOOOO!!')
    address = input('Now the address for your shipping: ')
    tel = input('Your telephone number please:) ')
    email = input('And your email please :) ')

    # Check if input email are correct or not by check @ in input.
    while True:
        if '@' not in email:
            print('Ehhh Wrong! Please check your email and type again ( ˘︹˘ )')
            email = input('Your email please! :( ')
        else:
            break
    new_data = {
        username: {
            "password": password,
            "address": address,
            "tel": tel,
            "email": email
        }
    }
    # Read an old data then save it in data_file variable
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
    print('============================')
    print('Hi welcome to login page')
    print('Please type in your username and password :)')
    print('============================')
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
clear()

# Animation for loading data
print("Retrieving data please wait ", end='')
for time in range(0, 10):
    print('.', end='')
    sleep(0.5)
clear()
# Declare customer class from Customer.py
customer = Customer(username)
customer.welcome_user()
# show all categories then return chosen choice.
chose_menu = customer.menu()
if chose_menu == 6:
    customer.setting()
menu_num_list = {1: "Digestive system", 2: "Pain", 3: "Infections and infestations", 4: "Allergic disorders",
                 5: "Nutrition", 6: "Setting"}
# Declare Medicine class from Medicine.py
medicine = Medicine(username)
# This method allow user to choose each medicine from the chosen categories.
chose_medicine_num = medicine.show_medicine_from_user_choice(chose_menu)
# Show information about the very specific medicine that user chose from categories.
chosen_med, price = medicine.show_detail_of_medicine(menu_num_list[chose_menu], chose_medicine_num)
put_to_cart_or_not = medicine.ask_user_they_like_products()
if put_to_cart_or_not == 0:
    customer.add_to_cart(chosen_med, price)
