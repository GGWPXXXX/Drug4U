
import json
from time import sleep
import textwrap


class Customer:
    def __init__(self, username):
        self.__username = username
        self.__list_for_total_price = []
        self.__total_price_list = []

    # getter for username
    @property
    def username(self):
        return self.__username

    # welcome customer text
    def welcome_user(self):
        print('============================')
        print(f'Hi {self.__username} welcome to my shop :)')
        print('============================')

    def take_to_menu_animation(self):
        for time in range(5, 0, -1):
            print(f"We'll take you back in main menu in {time}")
            sleep(1)

    # Show all menu
    def menu(self):
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as med:
            med_data = json.load(med)
        print('---> Please select Menu :) <---')
        print('==========================')
        count = 1
        for each_category in med_data.keys():
            print(f'{count}.{each_category}')
            count += 1
        print('==========================')
        print(f'{count}.Setting')
        print(f'{count+1}.Checkout')
        print(f'{count+2}.Exit')
        count += 3
        print('==========================')
        menu_choice = input('Please input number:) ')
        print('==========================')
        print()
        # Check if user input is the correct menu number or not.
        num_of_menu = [str(x) for x in range(1, count+1)]
        while menu_choice not in num_of_menu:
            print("Wrong category :(")
            menu_choice = input('Please input the correct number :( ')
        while menu_choice == "" and menu_choice == " ":
            print("Type in something bruh.")
            menu_choice = input('Please input the correct number :( ')
        return int(menu_choice)

    # Setting method for the customer.

    def setting(self):
        while True:
            menu_dict_num = {'1': "password", '2': "address", '3': "tel"}
            print('==============================')
            print('What would you like to change?')
            print('==============================')
            print('1.Password')
            print('2.Address')
            print('3.Telephone number')
            choice = input('Please type in menu number :) ')

            # Check if user type in the wrong choice.
            while choice not in menu_dict_num.keys():
                print('Wrong choice!!')
                choice = input('Please type in menu number :) ')

            change_to = input('Change it to? : ')
            while change_to == '' or change_to == ' ':
                print('Wrong choice!!')
                change_to = input('Change it to? :( ')
            with open('../Drug4U/User_file/User_data.json', 'r')as old_data_file:
                old_data = json.load(old_data_file)

                # Use this code if user want to change password.
                if choice == '1':
                    new_information = {
                        self.__username: {
                            menu_dict_num[choice]: change_to,
                            "address": old_data[self.__username]["address"],
                            "tel": old_data[self.__username]["tel"]
                        }
                    }

                # Use this code if user want to change Address.
                elif choice == '2':
                    new_information = {
                        self.__username: {
                            "password": old_data[self.__username]["password"],
                            menu_dict_num[choice]: change_to,
                            "tel": old_data[self.__username]["tel"]

                        }
                    }

                # Use this code if user want to change Telephone number.
                elif choice == '3':
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
                self.take_to_menu_animation()
                break

            elif ask_final_choice == 'y'.lower():
                continue

    # Add new item into the cart.json
    def add_to_cart(self, med_name, price, med_amount):

        with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
            cart = json.load(cart_data)

            new_order_for_account_not_in_sys = {
                self.__username: {
                    1: [med_name, price, med_amount]
                }
            }

            # if account already in cart database use the following code.
            try:
                new_order_for_account_in_sys = {
                    int(max(cart[self.__username])) + 1: [med_name, price, med_amount]

                }
                cart[self.__username].update(new_order_for_account_in_sys)

            # if not use this following code
            except KeyError:
                cart.update(new_order_for_account_not_in_sys)

        with open('../Drug4U/Medicine/Cart.json', 'w') as new_cart:
            json.dump(cart, new_cart, indent=4)
        print(f'{med_name[2:]} was added to your cart :)')


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
                    print(f'{int(num_of_item)}. {data_from_cart[self.__username][num_of_item][0][2:]}. x '
                          f'{data_from_cart[self.__username][num_of_item][2]}')

                    print(f'---> {data_from_cart[self.__username][num_of_item][1]} Baht. <---')
                    self.__list_for_total_price.append([int(data_from_cart[self.__username][num_of_item][1]),
                                                        int(data_from_cart[self.__username][num_of_item][2])])
                print('-------------')

                # This is list for compute price of each item from the customer.
                # each_item[0] mean price per one product.
                # each_item[1] mean how many product customer want to buy.
                self.__total_price_list = [each_item[0] * each_item[1] for each_item in self.__list_for_total_price]
                print(f"Your total is {sum(self.__total_price_list)} Baht.")
                print('-------------')

                # Clear both list for next customer.
                self.__total_price_list.clear()
                self.__list_for_total_price.clear()

                with open('../Drug4U/Admin_file/Orders.json', 'r') as order:
                    order_file = json.load(order)

                # If account already in orders.json
                try:
                    order = {
                        int(max(order_file[self.__username].keys()))+1: data_from_cart[self.__username]
                    }
                    order_file[self.__username].update(order)
                    with open('../Drug4U/Admin_file/Orders.json', 'w') as new_order:
                        json.dump(order_file, new_order, indent=4)


                #If not program will run this code.
                except KeyError:
                    with open('../Drug4U/User_file/User_data.json', 'r') as data:
                        customer_data = json.load(data)
                    order = {
                        self.__username:{
                            0: [customer_data[self.__username]["address"], customer_data[self.__username]["tel"]],
                            1: data_from_cart[self.__username]

                        }
                    }
                    order_file.update(order)
                    with open('../Drug4U/Admin_file/Orders.json', 'w') as new_order:
                        json.dump(order_file, new_order, indent=4)

            # Delete order that ordered from the cart database.
                data_from_cart.pop(self.__username)
                data_from_cart.update()
            with open('../Drug4U/Medicine/Cart.json', 'w') as cart_data:
                json.dump(data_from_cart, cart_data, indent=4)



        # If there's an error the program will execute this code.
        except KeyError:
            print("===============================")
            print("There's nothing in your cart :)")
            print("===============================")
            self.take_to_menu_animation()

        exit()



#
#
# c = Customer('a123')
# c.checkout()
