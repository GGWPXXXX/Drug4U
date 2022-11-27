
import json
from Medicine import Medicine


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

    def setting(self):
        print('What would you like to change?')
        print('''
        1.password
        2.address
        3.telephone number''')
        choice = int(input('Please type in menu number :) '))
        new_information = {
            self.__username: {
                "password"
            }
        }
        with open('../Drug4U/User_file/User_data.json', 'r')as data_file:
            data = json.load(data_file)

        data[self.__username].update()

    # Add new item into the cart.json
    def add_to_cart(self, med_name, price):
        with open('../Drug4U/Medicine/Cart.json', 'r') as cart_data:
            cart = json.load(cart_data)
            new_order_for_account_not_in_sys = {
                    self.__username: {
                        med_name: price
                    }
                }
            new_order_for_account_already_in_system = {
                med_name: price
            }
            new_order_for_same_product = {
                med_name: cart[self.__username][med_name] + price
            }

            # Check if account in the cart database or not.
            if self.__username in cart:

                # Check if med already in user's cart (meaning buy same product more than one)
                if med_name in cart[self.__username]:
                    cart[self.__username].update(new_order_for_same_product)
                else:
                    cart[self.__username].update(new_order_for_account_already_in_system)
            else:
                cart.update(new_order_for_account_not_in_sys)
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
            self.add_to_cart(chosen_med, price)


c = Customer('GG_WPX')
c.setting()
