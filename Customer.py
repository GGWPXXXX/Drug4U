
import json
from Medicine import Medicine
import textwrap


class Customer:
    def __init__(self, username):
        self.__username = username
        self.__cart_med_name_list = []

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
    def add_to_cart(self, med_name, price, med_type):

        with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
            cart = json.load(cart_data)

            new_order_for_account_not_in_sys = {
                self.__username: {
                    0: {med_name: price}
                }
            }

            if self.__username in cart:
                new_order_for_account_in_sys = {
                    len(max(cart[self.__username]))+1: {med_name: price}

                }
                cart[self.__username].update(new_order_for_account_in_sys)
            else:
                cart.update(new_order_for_account_not_in_sys)

            # new_order_for_med_type_not_in_account = {
            #     self.__username: {
            #         med_type: [med_name, price]
            #     }
            # }
            #
            # new_order_for_med_type_already_in_system = {
            #     med_type: [[med_name, price]]
            # }
            #
            # if self.__username in cart:
            #     if med_type in cart[self.__username]:
            #         new_order_for_same_medtype = {
            #             med_type: cart[self.__username][med_type].append([med_name, price])
            #         }
            #         cart[self.__username].update(new_order_for_same_medtype)
            #     cart[self.__username].update(new_order_for_med_type_already_in_system)
            #
            # else:
            #     cart.update(new_order_for_med_type_not_in_account)

            # new_order_for_account_not_in_sys = {
            #         self.__username: {
            #             med_name: price
            #         }
            #     }
            # new_order_for_account_already_in_system = {
            #     med_name: price
            # }
            # new_order_for_same_product = {
            #     med_name: cart[self.__username][med_name] + price
            # }
            # Check if account in the cart database or not.
            # if self.__username in cart:
            #
            #     # Check if med already in user's cart (meaning buy same product more than one)
            #     if med_name in cart[self.__username]:
            #         cart[self.__username].update(new_order_for_same_product)
            #     else:
            #         cart[self.__username].update(new_order_for_account_already_in_system)
            # else:
            #     cart.update(new_order_for_account_not_in_sys)
        with open('../Drug4U/Medicine/Cart.json', 'w') as new_cart:
            json.dump(cart, new_cart, indent=4)
        print(f'{med_name} was added to your cart :)')

    # The main method for customer class.
    def main(self):
        menu_num_list = {1: "Digestive system", 2: "Pain", 3: "Infections and infestations", 4: "Allergic disorders",
                         5: "Nutrition", 6: "Setting"}

        # show all categories then return chosen choice.
        menu_num = self.menu()

        # This method allow user to choose each medicine from the chosen categories.
        chose_medicine_num = Medicine.show_medicine_from_user_choice(self.__username, menu_num)

        # Show information about the very specific medicine that user chose from categories.
        chosen_med, price = Medicine.show_detail_of_medicine(self.__username, menu_num_list[menu_num],
                                                             chose_medicine_num)
        put_to_cart_or_not = Medicine.ask_user_they_like_products(self.__username)
        if put_to_cart_or_not == 0:
            self.add_to_cart(chosen_med, price, menu_num_list[menu_num])

    def checkout(self):
        print('=================================')
        print("You're order(s) are the following :)")
        print('=================================')
        with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
            data_from_cart = json.load(cart_data)
            count = 0
            count += 1
            for item in self.__cart_med_name_list:
                print(item.replace(item[:2], ''))
                print(f'---> Price {data_from_cart[self.__username][item]} <---')


c = Customer('GG_WPX')
c.add_to_cart("1.Nature's Bounty Activated Charcoal 260 mg, 100 Capsules", 700, "Digestive system")
c.add_to_cart("3.Tagamet Acid Reducer, 200mg, 30-count Tablets, 30 Count", 300, "Pain")
c.add_to_cart("1.Amazon Elements Vitamin C 1000mg 300 Tablets", 1000, "Nutrition")
c.add_to_cart("2.Now Foods, Vitamin A, 10,000 IU, 100 Softgels", 500, "Nutrition")
