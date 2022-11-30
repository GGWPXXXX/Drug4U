
import json
from time import sleep
from Medicine import Medicine
import textwrap


class Customer:
    def __init__(self, username):
        self.__username = username
        self.__list_for_total_price = []

    # getter for username
    @property
    def username(self):
        return self.__username

    # welcome customer text
    def welcome_user(self):
        print('============================')
        print(f'Hi {self.__username} welcome to my shop :)')
        print('============================')

    # Show all menu
    def menu(self):
        print('---> Please select Menu :) <---')
        print('==========================')
        print('1.Digestive system')
        print('2.Pain')
        print('3.Infections and infestations')
        print('4.Allergic disorders')
        print('5.Nutrition')
        print('6.Setting')
        print('7.Checkout')
        print('8.Exit')
        print('==========================')
        menu_choice = input('Please input number:) ')
        print('==========================')
        print()
        # Check if user input is the correct menu number or not.
        menu_num_list = {'1': "Digestive system", '2': "Pain", '3': "Infections and infestations",
                         '4': "Allergic disorders", '5': "Nutrition", '6': "Setting", '7': "Checkout", '8': "Exit"}
        while True:
            if menu_choice not in menu_num_list.keys() or menu_choice == '':
                print('---> Are you blind? <---')
                menu_choice = input('Please input the correct number :( ')
            else:
                return int(menu_choice)

    # Setting method for the customer.

    def setting(self):
        while True:
            menu_dict_num = {1: "password", 2: "address", 3: "tel", 4: "email"}
            print('==============================')
            print('What would you like to change?')
            print('==============================')
            print('1.Password')
            print('2.Address')
            print('3.Telephone number')
            print('4.Email')
            choice = int(input('Please type in menu number :) '))

            # Check if user type in the wrong choice.
            while choice not in menu_dict_num.keys():
                print('Wrong choice!!')
                choice = int(input('Please type in menu number :) '))
            change_to = input('Change it to? : ')
            with open('../Drug4U/User_file/User_data.json', 'r')as old_data_file:
                old_data = json.load(old_data_file)
                if choice == 1:
                    new_information = {
                        self.__username: {
                            menu_dict_num[choice]: change_to,
                            "address": old_data[self.__username]["address"],
                            "tel": old_data[self.__username]["tel"],
                            "email": old_data[self.__username]["email"]
                        }
                    }
                elif choice == 2:
                    new_information = {
                        self.__username: {
                            "password": old_data[self.__username]["password"],
                            menu_dict_num[choice]: change_to,
                            "tel": old_data[self.__username]["tel"],
                            "email": old_data[self.__username]["email"]

                        }
                    }
                elif choice == 3:
                    new_information = {
                        self.__username: {
                            "password": old_data[self.__username]["password"],
                            "address": old_data[self.__username]["address"],
                            menu_dict_num[choice]: change_to,
                            "email": old_data[self.__username]["email"]
                        }
                    }
                else:
                    while True:
                        if '@' not in change_to:
                            print('Ehhh Wrong! Please check your email and type again ( ˘︹˘ )')
                            change_to = input('Your email please! :( ')
                        else:
                            break
                    new_information = {
                        self.__username: {
                            "password": old_data[self.__username]["password"],
                            "address": old_data[self.__username]["address"],
                            "tel": old_data[self.__username]["tel"],
                            menu_dict_num[choice]: change_to
                        }
                    }
            with open('../Drug4U/User_file/User_data.json', 'r')as data_file:
                data = json.load(data_file)
                data.update(new_information)
            with open('../Drug4U/User_file/User_data.json', 'w')as data_file:
                json.dump(data, data_file, indent=4)
            print(f'Your {menu_dict_num[choice]} is now changed to {change_to}')
            # Check if user want to change anything else.
            print('Do you want to change anything else?')
            ask_final_choice = input('(y/n): ')
            check_list = ['y', 'n']

            # Check if user type in the wrong choice.
            while True:
                if ask_final_choice not in check_list:
                    print('Wrong Choice!!!!')
                    ask_final_choice = input('Please type y/n!: ')
                else:
                    break
            if ask_final_choice == 'n'.lower():
                break

            elif ask_final_choice == 'y'.lower():
                continue

    # Add new item into the cart.json
    def add_to_cart(self, med_name, price):

        with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
            cart = json.load(cart_data)

            new_order_for_account_not_in_sys = {
                self.__username: {
                    0: [med_name, price]
                }
            }

            # if account already in cart database use the following code.
            try:
                new_order_for_account_in_sys = {
                    int(max(cart[self.__username]))+1: [med_name, price]

                }
                cart[self.__username].update(new_order_for_account_in_sys)

            # if not use this following code
            except KeyError:
                cart.update(new_order_for_account_not_in_sys)

        with open('../Drug4U/Medicine/Cart.json', 'w') as new_cart:
            json.dump(cart, new_cart, indent=4)
        print(f'{med_name} was added to your cart :)')

    # This method allow user to check out of the store.
    def checkout(self):
        # Try this and check if there's any error.
        try:
            with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
                data_from_cart = json.load(cart_data)

                # This variable trigger_error made to trigger key error i.e.check if this user have any
                # product in cart.json
                trigger_error = data_from_cart[self.__username]
                print('=================================')
                print("You're order(s) are the following :)")
                print('=================================')
                for num_of_item in data_from_cart[self.__username].keys():
                    print(f'{int(num_of_item)+1}. {data_from_cart[self.__username][num_of_item][0][2:]}.')
                    print(f'---> {data_from_cart[self.__username][num_of_item][1]} Baht. <---')
                    self.__list_for_total_price.append(int(data_from_cart[self.__username][num_of_item][1]))
                print('-------------')
                print(f"Your total is {sum(self.__list_for_total_price)} Baht.")
                print('-------------')
                self.__list_for_total_price.clear()
            with open('../Drug4U/Medicine/Cart.json', 'w') as cart_data:
                data_from_cart.pop(self.__username)
                data_from_cart.update()
                json.dump(data_from_cart, cart_data, indent=4)
                exit()
        # If there's an error the program will execute this code.
        except KeyError:
            print("===============================")
            print("There's nothing in your cart :)")
            print("===============================")
            for time in range(5, 0, -1):
                print(f"We'll take you back in main menu in {time}")
                sleep(1)


# c = Customer('GG_WPX')
# c.checkout()
