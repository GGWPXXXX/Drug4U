import json
import textwrap
from Customer import Customer

class Medicine:
    """This class is a class for medicine, all the methods about medication are in here.
    such as show detail of the specific product that customer chose etc."""

    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        """getter for username."""
        return self.__username


    def show_medicine_from_user_choice(self, user_choice):
        """# This method allow user to choose each medicine from the chosen categories."""

        with open('../Drug4U/Medicine/Medicine_Data.json', 'r',
                  encoding='utf-8') as medicine_data:
            med_data = json.load(medicine_data)
            availble_med = []
            menu_num_dict = {}
            count = 1
            for each_categories in med_data.keys():
                menu_num_dict[count] = each_categories
                count += 1
            print('====================')
            print(menu_num_dict[user_choice])
            print('====================')
            count = 1
            for each_medicine_in_data, information in \
                    med_data[menu_num_dict[user_choice]].items():

            # Check stock of each that if it's lesser or equal to 0 it will not show that medicine.
                if information["amount"] <= 0:
                    continue
                availble_med.append(each_medicine_in_data)
                print(f"{count}. {each_medicine_in_data[2:]}")
                count += 1
                print(f"---> The price is {information['price']} Baht. <---")
            print('====================')
            choice = input('Which one would you like to see the information ? ')

            # list that counting how many medicine in that specific categories.
            num_med_list = []
            count = 1
            for each_med in med_data[menu_num_dict[user_choice]].keys():
                if med_data[menu_num_dict[user_choice]][each_med]["amount"] > 0:
                    num_med_list.append(count)
                    count += 1
            # check that choice is blank or not.
            while choice in ('', ' '):
                print("Wrong Choice!!")
                choice = input('Which one would you like to see the information ? ')
            choice = int(choice)
            # check that choice is correct or not.
            while True:
                if choice not in num_med_list:
                    print('Wrong choice amigo :)')
                    choice = int(input('Which one would you like to see the information ? '))
                else:
                    # method return choice of the specific medicine.
                    return availble_med[choice-1]


    def ask_user_customer_like_products(self):
        """This method ask user that they would like to continue with this product or not."""

        print('---> Do you like this product? <---')
        print('type 0 to add to the cart')
        print('type 1 to go back to main menu')
        like_it = input(':) ')
        while True:
            if like_it in ('1', '0'):
                return int(like_it)
            print('please type 0 or 1 :( ')
            like_it = input(':( ')

    def ask_customer_want_buy_how_many(self, chose_categories, chose_med_name):
        """Ask customer how many do they want to buy the product and calculate the rest of the stock."""

        print("===============================")
        customer_amount = input('How many do you want to buy? ')
        print("===============================")

        # Check that choice is blank or not.
        while customer_amount in ('', ' '):
            print("You have to type in something !")
            customer_amount = input('How many do you want to buy? ')

        # Check that choice is zero or not.
        customer_amount = int(customer_amount)
        while customer_amount <= 0:
            print("Can't be zero or less than that !")
            customer_amount = int(input("How many do you want to buy? "))

        with open('../Drug4U/Medicine/Medicine_Data.json', 'r', encoding='utf-8') as medicine_data:
            med_data = json.load(medicine_data)

            # Notify customers if that medicines are not enough for the customer.
            while med_data[chose_categories][chose_med_name]["amount"] < customer_amount:
                print("Sorry Insufficient supplies.")
                print(f"For {chose_med_name} there are "
                      f"{med_data[chose_categories][chose_med_name]['amount']} in stock.")
                customer_amount = int(input('How many do you want to buy? '))

        new_data_for_used_information = {
            chose_med_name: {
                "uses": med_data[chose_categories][chose_med_name]["uses"],
                "side-effects": med_data[chose_categories][chose_med_name]["side-effects"],
                "precautions": med_data[chose_categories][chose_med_name]["precautions"],
                "price": med_data[chose_categories][chose_med_name]["price"],
                "amount": med_data[chose_categories][chose_med_name]['amount'] - customer_amount
            }
        }

        med_data[chose_categories].update(new_data_for_used_information)
        with open('../Drug4U/Medicine/Medicine_Data.json', 'w', encoding='utf-8') as new_med_data:
            json.dump(med_data, new_med_data, indent=4)

        # Import class customer to use take_to_menu_animation method.
        customer = Customer(self.__username)
        customer.take_to_menu_animation()
        return customer_amount


    def show_detail_of_medicine(self, chose_categories, chose_med_name):
        """Show information about the very specific medicine that user chose from categories."""

        with open('../Drug4U/Medicine/Medicine_Data.json', 'r', encoding='utf-8') as medicine_data:
            med_data = json.load(medicine_data)
            for medicine in med_data[chose_categories]:
                if medicine == chose_med_name:
                    print('===========================================')
                    print('---> Please read the prescription very carefully!. <---')
                    print('===========================================')
                    print()
                    print('---> What When and How to use this medication. <---')
                    print('===========================================')
                    print(textwrap.fill(med_data[chose_categories][medicine]['uses'])), 100
                    print()
                    print('---> This is side-effect of this medication. <---')
                    print('===========================================')
                    print(textwrap.fill(med_data[chose_categories][medicine]['side-effects'])), 100
                    print()
                    print('---> This is the precautions of this medication. <---')
                    print('===========================================')
                    print(textwrap.fill(med_data[chose_categories][medicine]['precautions'])), 100
                    print()
                    print('---> This is the price :) <---')
                    print('===========================================')
                    print(f"---> {med_data[chose_categories][medicine]['price']} Baht <---")
                    print('===========================================')
                    return medicine, med_data[chose_categories][medicine]['price']

