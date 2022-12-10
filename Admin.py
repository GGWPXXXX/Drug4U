import json
from time import sleep


class Admin:
    def __init__(self, username):
        self.__username = username
        self.__med_num = []

    def welcome_admin(self):
        with open('../Drug4U/Admin_file/Admin_data.json', 'r') as data:
            admin_data = json.load(data)
            print('=======================')
            print(f"Hello {self.__username} :) \n"
                  f"Welcome to admin panel ! \n"
                  f"Your role is {admin_data[self.__username]['role']}")
            print('=======================')

    def take_to_menu_animation(self):
        for time in range(5, 0, -1):
            print(f"We'll take you back in main menu in {time}")
            sleep(1)

    def clear(self):
        print('\n'*40)

    def add_new_category(self):
        print('What is the name of new category?')
        category_name = input(': ')
        while category_name == "" or category_name == ' ':
            print('Type something bruh :( ')
            category_name = input(': ')
        new_category = {
            category_name: {

            }
        }
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as med:
            med_data = json.load(med)
            med_data.update(new_category)
        with open('../Drug4U/Medicine/Medicine_Data.json', 'w') as med:
            json.dump(med_data, med, indent=4)

    def add_new_product(self):
        while True:
            with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as med:
                med_data = json.load(med)
                for each_categories in med_data.keys():
                    print(f'{each_categories}')

                print("Please type in name of the category.")
                add_to_this_categories = input(': ')

                # Check whether the categories input was the correct name of the categories.
                while add_to_this_categories not in med_data.keys():
                    print("Wrong Stock!!!")
                    add_to_this_categories = input(': ')
                print('Name of the medicine?')
                name_of_med = input(': ')

                # Check in case that input is blank.
                while name_of_med == "" or name_of_med == ' ':
                    print('Type something bruh :( ')
                    name_of_med = input(': ')

                # Ask and check the uses of medication in case it was blank.
                print("Uses?")
                uses = input(': ')
                while uses == "" or uses == ' ':
                    print('Type something bruh :( ')
                    uses = input(': ')

                # Ask and check the side effects of medication in case it was blank.
                print("Side-effects?")
                side_effect = input(': ')
                while side_effect == "" or side_effect == ' ':
                    print('Type something bruh :( ')
                    side_effect = input(': ')

                # Ask and check the precaution of medication in case it was blank.
                print("Precautions?")
                pre_caution = input(': ')
                while pre_caution == "" or pre_caution == ' ':
                    print('Type something bruh :( ')
                    pre_caution = input(': ')

                # Ask and check the price of medication in case it was blank.
                print("Price?")
                price = input(': ')
                while price == "" or price == ' ':
                    print('Type something bruh :( ')
                    price = input(': ')

                # Ask and check the amount of medication in case it was blank.
                print("Amount of medicine?")
                amount = input(': ')
                while amount == "" or amount == ' ':
                    print('Type something bruh :( ')
                    amount = input(': ')

                new_product = {
                    name_of_med:{
                        "uses": uses,
                        "side-effects": side_effect,
                        "precautions": pre_caution,
                        "price": int(price),
                        "amount": int(amount)
                    }
                }

                med_data[add_to_this_categories].update(new_product)
                with open('../Drug4U/Medicine/Medicine_Data.json', 'w') as med:
                    json.dump(med_data, med, indent=4)

                #Ask and check whether admin want to add anything else.
                print('Do you want to add anything else?')
                add_more_or_not = input('(y/n): ')
                while add_more_or_not == ' ' and add_more_or_not == '':
                    print('Type something bruh :( ')
                    add_more_or_not = input('(y/n): ')
                while add_more_or_not.lower() != 'y' and add_more_or_not.lower() != 'n':
                    print('Type (Y or N) only! :( ')
                    add_more_or_not = input('(y/n): ')

                if add_more_or_not == 'n'.lower():
                    self.take_to_menu_animation()
                    break
                else:
                    self.clear()


    def modify_stock(self):
        print('==================================')
        print("Which stock do you want to modify? ")
        print('==================================')
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as med:
            med_data = json.load(med)
            for each_categories in med_data.keys():
                print(f'{each_categories}')
            print()
            print("Please type in name of the category.")
            modify_this_categories = input(': ')

            # Check whether the categories input was wrong.
            while modify_this_categories not in med_data.keys():
                print("Wrong Stock!!!")
                modify_this_categories = input(': ')

            self.clear()
            # Print all the drug name from the specific category.
            for each_med in med_data[modify_this_categories].keys():
                print(each_med)
                self.__med_num.append(each_med[0])
            print('==================================')
            print('Which one would you like to change?')
            this_med = input("Type in number :) ")

            # Check in case of input is blank.
            while this_med == '' or this_med == ' ':
                print('WRONG NUMBER !')
                this_med = input("Type in number :( ")

            # Check in case of input is wrong menu number.
            while this_med[0] not in self.__med_num:
                print('WRONG NUMBER !')
                this_med = input("Type in number :( ")
            self.clear()

            print('What do you want to do')
            print(f'1. Check remaining stock')
            print(f'2. Modify the product')
            want_to_do = input(': ')

            # Check in case of input is wrong menu number.
            while want_to_do != '1' and want_to_do != '2':
                print('WRONG NUMBER !')
                want_to_do = input(': ')

            # If admin want to check remaining stock of the specific product.
            if want_to_do == '1':
                for each_med in med_data[modify_this_categories].keys():
                    if each_med[0] == this_med:
                        print('====================================')
                        print(f'{each_med}')
                        print('====================================')
                        print(f'The current stock of this product is ---> '
                              f'{med_data[modify_this_categories][each_med]["amount"]} <---')

            # If admin want to change uses, side-effects, precautions, price, amount of the specific product.
            if want_to_do == '2':
                for each_med in med_data[modify_this_categories].keys():
                    if each_med[0] == this_med:

                        print("What do you want to modify?")
                        print("uses, side-effects, precautions, price, amount")
                        print("Please type in ;)")
                        want_to_modify_this = input(':) ')
                        # Check input that
                        while want_to_modify_this != "uses" and want_to_modify_this != "side-effects" and \
                                want_to_modify_this != "precautions" and want_to_modify_this != "price" and \
                                want_to_modify_this != "amount":
                            print("Wrong Choice!!!")
                            want_to_modify_this = input(':( ')

                        print("And modify it to? ")
                        modify_to = input(':) ')

                        # Check input that is blank or not.
                        while modify_to == '' and modify_to == ' ':
                            print("You have to type in something !!")
                            modify_to = input(":) ")
                        if want_to_modify_this == "amount" or want_to_modify_this == "price":
                            modify_to = int(modify_to)
                        med_data[modify_this_categories][each_med][want_to_modify_this] = modify_to

            with open('../Drug4U/Medicine/Medicine_Data.json', 'w') as med:
                json.dump(med_data, med, indent=4)

    # Show all confirmed orders from customers.
    def show_all_orders(self):
        with open('../Drug4U/Admin_file/Orders.json', 'r') as order:
            order_data = json.load(order)

        # Loading animation
        print("Retrieving data please wait ",end='')
        for time in range(0, 5):
            print(".", end='')
            sleep(0.5)
        self.clear()
        print("All of the order are the following :)\n")
        print(f"{'| Username |':>10} | {'Order no.':>10} | {'| Medicine name |':>50}  {'| Price |':>45} "
              f"{'| Amount |'} {'| Address |':>13} {'| Telephone |':>33}")
        print('=========================================================================='
              '========================================================================='
              '======================================================')
        with open('../Drug4U/User_file/User_data.json', 'r')as user:
            user_file = json.load(user)
        for user_name, info in order_data.items():
            for num in info.keys():
                for order_num in order_data[user_name][num]:
                    print(f'{user_name:>8}', end='')
                    print(f'{num:>11}', end='')
                    print(f'{order_data[user_name][num][order_num][0]:^100}',end='')
                    print(f'{str(order_data[user_name][num][order_num][1]).rjust(3)}',end='')
                    print(f'{str(order_data[user_name][num][order_num][2]).rjust(10)}',end='')
                    print(user_file[user_name]["address"].rjust(21),end='')
                    print(user_file[user_name]["tel"].rjust(30))
            print('----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '---------------------------')
        print("Type 'back' to go back to the main menu :) ")
        back = input(': ')
        while back.lower() != "back":
            print("Type back bruh :(")
            back = input(': ')

    # Show order from username.
    def show_specific_order(self):
        with open('../Drug4U/User_file/User_data.json', 'r')as user:
            user_file = json.load(user)

        with open('../Drug4U/Admin_file/Orders.json', 'r') as order:
            order_data = json.load(order)

        print("Please type in username")
        username = input(":) ")

        while username not in user_file or username not in order_data:
            print(f"{username} not in the system.")
            print(f"Please try again.")
            username = input(":) ")
            while username not in order_data:
                print(f"{username} not ordering anything yet.")
                print(f"Please try again.")
                username = input(":) ")


        print("Retrieving data please wait ",end='')
        for time in range(0, 5):
            print(".", end='')
            sleep(0.5)
        self.clear()
        print("All of the order are the following :)\n")
        print(f"{'| Username |':>10} | {'Order no.':>10} | {'| Medicine name |':>50}  {'| Price |':>45} "
              f"{'| Amount |'} {'| Address |':>13} {'| Telephone |':>33}")
        print('=========================================================================='
              '========================================================================='
              '======================================================')

        for keys, info in order_data[username].items():
            for each_info in info.values():
                print(f'{username:>8}', end='')
                print(f'{keys:>11}', end='')
                print(f'{each_info[0]:^100}',end='')
                print(f'{str(each_info[1]).rjust(3)}',end='')
                print(f'{str(each_info[2]).rjust(10)}',end='')
                print(user_file[username]["address"].rjust(21),end='')
                print(user_file[username]["tel"].rjust(30))
            print('----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '---------------------------')
        print('\n')
        print("Type 'back' to go back to the main menu :) ")
        back = input(': ')
        while back.lower() != "back":
            print("Type back bruh :(")
            back = input(': ')

    def admin_menu(self):
        with open('../Drug4U/Admin_file/Admin_data.json', 'r')as data:
            admin_data = json.load(data)
            print(admin_data)
            if admin_data[self.__username]['role'] == 'Stock_manager':
                print("")


admin = Admin('stock')
admin.welcome_admin()
admin.show_all_orders()
