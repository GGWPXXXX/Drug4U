import json
from time import sleep
from Customer import Customer
from Medicine import Medicine
import Admin



def read_external_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data_file = json.load(file)
        return data_file


def clear():
    print('\n'*40)


def load_animation(time):
    print("Retrieving data please wait ", end='')
    for count_time in range(0, time):
        print('.', end='')
        sleep(0.5)


def create_an_account(file_path):
    print('===============================')
    print('Hi this is registration form :)')
    print('===============================')
    user_name = input('What should we call you?: ')

    # Check if the username has been used.
    with open(file_path, 'r') as file:
        data_file = json.load(file)
        while username in data_file:
            print('Sorry, this username has already been used.')
            user_name = input('What should we call you?: ')

    print('===============================')
    print(f'Hi {user_name} Nice to meet ya :)')
    print('===============================')
    password = input('And what will your password be?: ')
    print('PERFECTOOOO!!')
    address = input('Now the address for your shipping: ')
    tel = input('Your telephone number please:) ')

    new_data = {
        user_name: {
            "password": password,
            "address": address,
            "tel": tel,
        }
    }
    # Read an old data then save it in data_file variable
    with open(file_path, 'r', encoding='utf-8') as file:
        data_file = json.load(file)
        data_file.update(new_data)

    # write down new data
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data_file, file, indent=4)

    print("Account Created !!!")
    load_animation(3)


def login(file_path):
    """This function is a login page for the program."""

    print('============================')
    print('Hi welcome to login page')
    print('Please type in your username and password :)')
    print('============================')
    user_name = input('Your username?: ')

    # check username that if it's in database or not.
    with open(file_path, 'r', encoding='utf-8') as file:
        data_file = json.load(file)
        while user_name not in data_file:
            print(f'Sorry, Username:{user_name} not found on the system.')
            user_name = input('Your username?: ')
    password = input('And password?: ')

    # check the given password that if it's match with the username or not.
    with open(file_path, 'r', encoding='utf-8') as file:
        data_file = json.load(file)
        while password != data_file[user_name]['password']:
            print(f'Sorry, your given password does not match with the username, Please try again.')
            password = input('And password?: ')
    return user_name


user_file_path = '../Drug4U/User_file/User_data.json'
customer_data = (read_external_file(user_file_path))
print('''
===========================
Welcome to My DRUG4U Shop!
===========================
''')
print('Are you a customer?')
check_wheter_customer = input('(y/n): ')
while check_wheter_customer.lower() != 'y' and check_wheter_customer.lower() != 'n':
    print('Please type (y/n)')
    check_wheter_customer = input('(y/n): ')

# This part is for admin only
if check_wheter_customer.lower() == 'n':
    print('============================')
    print("Then you must be an admin :)")
    print("Please login")
    print('============================')
    admin_name = login('../Drug4U/Admin_file/Admin_data.json')
    with open('../Drug4U/Admin_file/Admin_data.json', 'r', encoding='utf-8') as data:
        admin_data = json.load(data)
    if admin_data[admin_name]["role"] == "Supreme-Admin":
        admin = Admin.Supreme_Admin(admin_name)
        admin.operate()
    elif admin_data[admin_name]["role"] == "Stock_Manager":
        admin = Admin.Stock_Manager(admin_name)
        admin.operate()
    else:
        admin = Admin.Sender(admin_name)
        admin.operate()


if check_wheter_customer.lower() == 'y':
    print('Do you have an account?')
    check_account = input('(y/n): ')
    while check_account.lower() != 'y' and check_account.lower() != 'n':
        print('Please type (y/n)')
        check_account = input('(y/n): ')
    if check_account.lower() == 'n':
        create_an_account(user_file_path)
        customer_data = (read_external_file(user_file_path))

print('============================')
print("Please login")
username = login(user_file_path)
clear()
load_animation(5)
# Animation for loading data
clear()
# Declare customer class from Customer.py
customer = Customer(username)
customer.welcome_user()
# show all categories then return chosen choice.

menu_num_dict = {}
with open('../Drug4U/Medicine/Medicine_Data.json', 'r' ,encoding='utf-8') as medicine_data:
    med_data = json.load(medicine_data)
    count = 1
    for each_categories in med_data.keys():
        menu_num_dict[count] = each_categories
        count += 1

while True:
    chose_menu = customer.menu()
    while chose_menu in (count, count + 1, count + 2):
        if chose_menu == count:
            clear()
            customer.setting()
            clear()
        elif chose_menu == count+1:
            clear()
            customer.checkout()
            clear()
        elif chose_menu == count+2:
            exit()
        chose_menu = customer.menu()

    # Declare Medicine class from Medicine.py
    medicine = Medicine(username)
    # This method allow user to choose each medicine from the chosen categories.
    clear()
    chose_med_name = medicine.show_medicine_from_user_choice(chose_menu)
    clear()
    # Show information about the very specific medicine that user chose from categories.
    chosen_med, price = medicine.show_detail_of_medicine(menu_num_dict[chose_menu], chose_med_name)
    put_to_cart_or_not = medicine.ask_user_customer_like_products()

    if put_to_cart_or_not == 0:
        customer_amount = medicine.ask_customer_want_buy_how_many\
            (menu_num_dict[chose_menu], chose_med_name)
        customer.add_to_cart(chosen_med, price, customer_amount)

    clear()
