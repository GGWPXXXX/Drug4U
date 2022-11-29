
import json
from Medicine import Medicine
import textwrap


class Customer:
    def __init__(self, username):
        self.__username = username

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
        print('==========================')
        menu_choice = input('Please input number:) ')

        # Check if user input is the correct menu number or not.
        menu_num_list = {'1': "Digestive system", '2': "Pain", '3': "Infections and infestations",
                         '4': "Allergic disorders", '5': "Nutrition", '6': "Setting"}
        while True:
            if menu_choice not in menu_num_list.keys() or menu_choice == '':
                print('---> Are you blind? <---')
                menu_choice = input('Please input the correct number :( ')
            else:
                return int(menu_choice)

    # Setting method for the customer.

    def setting(self):
        while True:
            menu_dict_num = {1: "password", 2: "address", 3: "tel"}
            print('==============================')
            print('What would you like to change?')
            print('==============================')
            print('1.password')
            print('2.address')
            print('3.telephone number')
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
                            "tel": old_data[self.__username]["tel"]
                        }
                    }
                elif choice == 2:
                    new_information = {
                        self.__username: {
                            "password": old_data[self.__username]["password"],
                            menu_dict_num[choice]: change_to,
                            "tel": old_data[self.__username]["tel"]
                        }
                    }
                else:
                    new_information = {
                        self.__username: {
                            "password": old_data[self.__username]["password"],
                            "address": old_data[self.__username]["address"],
                            menu_dict_num[choice]: change_to
                        }
                    }

            with open('../Drug4U/User_file/User_data.json', 'r')as data_file:
                data = json.load(data_file)
                data.update(new_information)
            with open('../Drug4U/User_file/User_data.json', 'w')as data_file:
                json.dump(data, data_file, indent=4)

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
                print(f'Your {menu_dict_num[choice]} is now changed to {change_to}')
                break

            elif ask_final_choice == 'y'.lower():
                print(f'Your {menu_dict_num[choice]} is now changed to {change_to}')
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

    # def checkout(self):
        # print('=================================')
        # print("You're order(s) are the following :)")
        # print('=================================')
        # with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
        #     data_from_cart = json.load(cart_data)
        #     print(f'---> Price {data_from_cart[self.__username][item]} <---')


# c = Customer('GG_WPX')
# c.add_to_cart("1.Nature's Bounty Activated Charcoal 260 mg, 100 Capsules", 700)
# c.add_to_cart("3.Tagamet Acid Reducer, 200mg, 30-count Tablets, 30 Count", 300)
# c.add_to_cart("1.Amazon Elements Vitamin C 1000mg 300 Tablets", 1000 )
# c.add_to_cart("2.Now Foods, Vitamin A, 10,000 IU, 100 Softgels", 500 )
# c = Customer('a123')
# c.add_to_cart("2.Now Foods, Vitamin A, 10,000 IU, 100 Softgels", 500 )
