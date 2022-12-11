import json
from time import sleep

class Admin:
    """This class is the parent class of all admin."""
    def __init__(self, admin_name):
        self.__admin_name = admin_name
        self.__med_num = []

    def _welcome_admin(self):
        """This method display welcome text to admin"""
        self._clear()
        with open('../Drug4U/Admin_file/Admin_data.json', 'r' ,
                  encoding='utf-8') as data:
            admin_data = json.load(data)
            print('==============================')
            print(f"Hello {self.__admin_name} :) \n"
                  f"Welcome to admin panel ! \n"
                  f"Your role is {admin_data[self.__admin_name]['role']}")
            print('==============================')
            print()

    def _take_to_menu_animation(self):
        """This method is a little animation before taking admin back to main menu."""

        for time in range(5, 0, -1):
            print(f"We'll take you back in main menu in {time}")
            sleep(1)

    def _clear(self):
        """This method use to clear the console page."""
        print('\n'*40)

    def _add_new_category(self):
        """This method allow admin to add new category to the Medicine_Data.json"""

        print('What is the name of new category?')
        category_name = input(': ')
        while category_name in ('', ' '):
            print('Type something bruh :( ')
            category_name = input(': ')
        new_category = {
            category_name: {

            }
        }
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r', encoding='utf-8') as med:
            med_data = json.load(med)
            med_data.update(new_category)
        with open('../Drug4U/Medicine/Medicine_Data.json', 'w', encoding='utf-8') as med:
            json.dump(med_data, med, indent=4)

        print(f'{category_name} added!')
        self._take_to_menu_animation()
        self._clear()

    def _add_new_product(self):
        """This method allow admin to add new product to the specific category."""

        while True:
            print('===============================')
            print("Categories are the following :)")
            print('===============================')
            with open('../Drug4U/Medicine/Medicine_Data.json', 'r', encoding='utf-8') as med:
                med_data = json.load(med)
                for each_categories in med_data.keys():
                    print(f'{each_categories}')
                print('===================================')
                print("Please type in name of the category.")
                add_to_this_categories = input(': ')

                # Check whether the categories input was the correct name of the categories.
                while add_to_this_categories not in med_data.keys():
                    print("Wrong Stock!!!")
                    add_to_this_categories = input(': ')
                print('Name of the medicine?')
                name_of_med = input(': ')

                # Check in case that input is blank.
                while name_of_med in ('', ' '):
                    print('Type something bruh :( ')
                    name_of_med = input(': ')

                # Ask and check the uses of medication in case it was blank.
                print("Uses?")
                uses = input(': ')
                while uses in ('', ' '):
                    print('Type something bruh :( ')
                    uses = input(': ')

                # Ask and check the side effects of medication in case it was blank.
                print("Side-effects?")
                side_effect = input(': ')
                while side_effect in ('', ' '):
                    print('Type something bruh :( ')
                    side_effect = input(': ')

                # Ask and check the precaution of medication in case it was blank.
                print("Precautions?")
                pre_caution = input(': ')
                while pre_caution in ('', ' '):
                    print('Type something bruh :( ')
                    pre_caution = input(': ')

                # Ask and check the price of medication in case it was blank.
                print("Price?")
                price = input(': ')
                while price in ('', ' '):
                    print('Type something bruh :( ')
                    price = input(': ')

                # Ask and check the amount of medication in case it was blank.
                print("Amount of medicine?")
                amount = input(': ')
                while amount in ('', ' '):
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
                with open('../Drug4U/Medicine/Medicine_Data.json', 'w', encoding='utf-8') as med:
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
                    self._take_to_menu_animation()
                    self._clear()
                    break
                else:
                    self._clear()


    def _modify_product(self):
        """This method allows admin to check or modify each product elements such as uses price
        side effect or even stock of that product."""

        print('==================================')
        print("Which stock do you want to modify? ")
        print('==================================')
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r', encoding='utf-8') as med:
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

            self._clear()
            # Print all the drug name from the specific category.
            for each_med in med_data[modify_this_categories].keys():
                print(each_med)
                self.__med_num.append(each_med[0])
            print('==================================')
            print('Which one would you like to change?')
            this_med = input("Type in number :) ")

            # Check in case of input is blank.
            while this_med in ('', ' '):
                print('WRONG NUMBER !')
                this_med = input("Type in number :( ")

            # Check in case of input is wrong menu number.
            while this_med[0] not in self.__med_num:
                print('WRONG NUMBER !')
                this_med = input("Type in number :( ")
            self._clear()

            print('What do you want to do')
            print(f'1. Check remaining stock')
            print(f'2. Modify the product')
            want_to_do = input(': ')

            # Check in case of input is wrong menu number.
            while want_to_do not in ('1', '2'):
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

            # If admin want to change uses, side-effects, precautions,
            # price, amount of the specific product.
            if want_to_do == '2':
                for each_med in med_data[modify_this_categories].keys():
                    if each_med[0] == this_med:

                        print("What do you want to modify?")
                        print("uses, side-effects, precautions, price, amount")
                        print("Please type in ;)")
                        want_to_modify_this = input(':) ')
                        # Check input that
                        while want_to_modify_this not in \
                                ('uses', 'side-effects', 'precautions',
                                 'price', 'amount'):
                            print("Wrong Choice!!!")
                            want_to_modify_this = input(':( ')

                        print("And modify it to? ")
                        modify_to = input(':) ')

                        # Check input that is blank or not.
                        while modify_to == '' and modify_to == ' ':
                            print("You have to type in something !!")
                            modify_to = input(":) ")
                        if want_to_modify_this in ('amount', 'price'):
                            modify_to = int(modify_to)
                        med_data[modify_this_categories][each_med][want_to_modify_this] = modify_to

            with open('../Drug4U/Medicine/Medicine_Data.json', 'w', encoding='utf-8') as med:
                json.dump(med_data, med, indent=4)
        print("DONE!!")
        self._take_to_menu_animation()
        self._clear()

    def _show_all_orders(self):
        """Show all confirmed orders from customers."""

        with open('../Drug4U/Admin_file/Orders.json', 'r', encoding='utf-8') as order:
            order_data = json.load(order)
        # Loading animation
        print("Retrieving data please wait ",end='')
        for time in range(0, 5):
            print(".", end='')
            sleep(0.5)
        self._clear()
        print("All of the order are the following :)\n")
        print(f"{'| Username |':>10} | {'Order no.':>10} | {'| Medicine name |':>50}  "
              f"{'| Price |':>45} "
              f"{'| Amount |'} {'| Address |':>13} {'| Telephone |':>33}")
        print('=========================================================================='
              '========================================================================='
              '======================================================')
        with open('../Drug4U/User_file/User_data.json', 'r', encoding='utf-8')as user:
            user_file = json.load(user)

        # Display all the medicine including its category and amount.
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
        self._take_to_menu_animation()
        self._clear()


    def _show_specific_order(self):
        """Show order from the specific username."""

        with open('../Drug4U/User_file/User_data.json', 'r', encoding='utf-8')as user:
            user_file = json.load(user)

        with open('../Drug4U/Admin_file/Orders.json', 'r', encoding='utf-8') as order:
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
        self._clear()
        print("All of the order are the following :)\n")
        print(f"{'| Username |':>10} | {'Order no.':>10} | "
              f"{'| Medicine name |':>50}  {'| Price |':>45} "
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
        self._take_to_menu_animation()
        self._clear()

    def _create_admin(self):
        """Create new admin account but only role "Supreme-Admin" can use this method."""

        print('===================================')
        print('What role of this account would be?')
        print('===================================')
        print('Supreme-Admin')
        print('Stock_Manager')
        print('Sender')
        print('===================================')
        role = input(': ')
        while role.lower() != 'admin' and role.lower() != 'sender'.lower() \
            and role.lower() != 'stock_manager':
            print("Wrong choice !!")
            print("Please try again :(")
            role = input(': ')

        print("And what should we call him/her?")
        name = input(': ')
        while name in (' ', ''):
            print("Name blank?")
            print("Please try again :(")
            name = input(': ')

        print("Password? ")
        password = input(': ')
        while password in (' ', ''):
            print("Password blank?")
            print("Please try again :(")
            password = input(': ')

        new_acc  = {
            name: {
                "password": password,
                "role": role
            }
        }
        with open('../Drug4U/Admin_file/Admin_data.json', 'r', encoding='utf-8')as data:
            old_data = json.load(data)
            old_data.update(new_acc)
        with open('../Drug4U/Admin_file/Admin_data.json', 'w', encoding='utf-8')as new_data:
            json.dump(old_data, new_data, indent=4)
        print("Complete the account created :)")
        self._take_to_menu_animation()
        self._clear()

    def _delete_order(self):
        """This method allow sender to delete specific order from specific customer."""

        with open('../Drug4U/Admin_file/Orders.json', 'r', encoding='utf-8') as order:
            order_data = json.load(order)
        print("Retrieving data please wait ", end='')
        for time in range(0, 5):
            print(".", end='')
            sleep(0.5)
        self._clear()

        # Display all the order.
        print("All of the order are the following :)\n")
        print(f"{'| Username |':>10} | {'Order no.':>10} | "
              f"{'| Medicine name |':>50}  {'| Price |':>45} "
              f"{'| Amount |'} {'| Address |':>13} {'| Telephone |':>33}")
        print('=========================================================================='
              '========================================================================='
              '======================================================')
        with open('../Drug4U/User_file/User_data.json', 'r', encoding='utf-8') as user:
            user_file = json.load(user)
        for user_name, info in order_data.items():
            for num in info.keys():
                for order_num in order_data[user_name][num]:
                    print(f'{user_name:>8}', end='')
                    print(f'{num:>11}', end='')
                    print(f'{order_data[user_name][num][order_num][0]:^100}', end='')
                    print(f'{str(order_data[user_name][num][order_num][1]).rjust(3)}', end='')
                    print(f'{str(order_data[user_name][num][order_num][2]).rjust(10)}', end='')
                    print(user_file[user_name]["address"].rjust(21), end='')
                    print(user_file[user_name]["tel"].rjust(30))
            print('----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '---------------------------')
        print()
        print('==========================================================')
        print("Please type in username of the order you want to delete :)")
        print('==========================================================')

        # Check username in case it not in database.
        username = input(": ")
        while username not in order_data:
            print(f"{username} not in order database!")
            print("Please check and try again.")
            username = input(":( ")
        print('===================================================================')
        print(f"Please type Order no. you want to delete from account {username} :)")
        print('===================================================================')

        # Check order number in case it not match with order of username.
        order_num = input(": ")
        while order_num not in order_data[username]:
            print(f"Order no.{order_num} not in order {username} database!")
            print("Please check and try again.")
            order_num = input(":( ")

        # Delete order from user then update into Order.json
        order_data[username].pop(order_num)

        # If that user have no order left in Order.json the program will delete such
        # account from Orders.json to prevent any error.
        if len(order_data[username].keys()) <= 0:
            order_data.pop(username)

        order_data.update()
        with open('../Drug4U/Admin_file/Orders.json', 'w', encoding='utf-8') as new_data:
            json.dump(order_data, new_data, indent=4)

        print()
        print("Order Deleted! \n")
        sleep(2)
        print("Retrieving data please wait ", end='')
        for time in range(0, 5):
            print(".", end='')
            sleep(0.5)
        self._clear()


        # Display all the remaining orders.
        print("All of the order are the following :)\n")
        print(f"{'| Username |':>10} | {'Order no.':>10} | {'| Medicine name |':>50} "
              f" {'| Price |':>45} "
              f"{'| Amount |'} {'| Address |':>13} {'| Telephone |':>33}")
        print('=========================================================================='
              '========================================================================='
              '======================================================')
        with open('../Drug4U/User_file/User_data.json', 'r', encoding='utf-8') as user:
            user_file = json.load(user)
        for user_name, info in order_data.items():
            for num in info.keys():
                for order_num in order_data[user_name][num]:
                    print(f'{user_name:>8}', end='')
                    print(f'{num:>11}', end='')
                    print(f'{order_data[user_name][num][order_num][0]:^100}', end='')
                    print(f'{str(order_data[user_name][num][order_num][1]).rjust(3)}', end='')
                    print(f'{str(order_data[user_name][num][order_num][2]).rjust(10)}', end='')
                    print(user_file[user_name]["address"].rjust(21), end='')
                    print(user_file[user_name]["tel"].rjust(30))
            print('----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '---------------------------')
        print('==============================')
        print("Type back when you're ready :)")
        print('==============================')
        back = input(': ')
        while back.lower() != 'back':
            print("Type BACK when you're READY.")
            back = input(': ')
        self._take_to_menu_animation()
        self._clear()

    def _show_remaning_stock_of_all_product(self):
        """ This method will show all the remaining stock of every
        medicine."""

        # Loading animation
        print("Retrieving data please wait ",end='')
        for time in range(0, 5):
            print(".", end='')
            sleep(0.5)
        self._clear()
        print("All of stock are the following :)\n")
        print(f"{'| Category |':>10} {'| Amount |':>40}  {'| Medicine name |':>80}  ")
        print('=========================================================================='
              '========================================================================='
              '======================================================')
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r', encoding='utf-8')as med:
            med_data = json.load(med)
        for categories, all_meds in med_data.items():
            for med_name, med_info in all_meds.items():
                print(f'{categories:<0}', end='')
                print(f'{str(med_info["amount"]):>30}',end='')
                print(f'{med_name:^140}')

            print('----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '----------------------------------------------------------'
                  '---------------------------')
        print("Type 'back' to go back to the main menu :) ")
        back = input(': ')
        while back.lower() != "back":
            print("Type back bruh :(")
            back = input(': ')
        self._take_to_menu_animation()
        self._clear()

class Stock_Manager(Admin):
    """This class is a stock_manager class which is a sub-class from admin.Only role
    'Stock_Manager' can use this class."""

    def __init__(self, admin_name):
        super().__init__(admin_name)

    def operate(self):
        """This is the main method for stock_manger class which contains all the methods that
        stock_manager need."""

        self._welcome_admin()
        while True:
            print('==============================')
            print("Your Menu are the following :)")
            print('==============================')
            print("1.Modify product")
            print("2.Add new category")
            print("3.Add new product")
            print("4.Show all remaining products.")
            print("5.Exit")
            print('==============================')
            print('Please type in menu number :)')
            menu_num = input(': ')
            while menu_num not in ('1', '2', '3', '4', '5'):
                print("Wrong menu!")
                menu_num = input(': ')
            if menu_num == '5':
                exit()
            elif menu_num == '1':
                self._clear()
                self._modify_product()
            elif menu_num == '2':
                self._clear()
                self._add_new_category()
            elif menu_num == '3':
                self._clear()
                self._add_new_product()
            elif menu_num == '4':
                self._clear()
                self._show_remaning_stock_of_all_product()

class Sender(Admin):
    """This class is Sender class which is a sub-class from admin.Only role 'Sender'
    can access and use this class."""

    def __init__(self, admin_name):
        super().__init__(admin_name)

    def operate(self):
        """This is the main method for Sender class which contains all the methods that
        Sender need."""

        self._welcome_admin()
        while True:
            print('==============================')
            print("Your Menu are the following :)")
            print('==============================')
            print("1.Show all orders")
            print("2.Show the specific order")
            print("3.Delete order")
            print("4.Exit")
            print('==============================')
            print('Please type in menu number :)')
            menu_num = input(': ')
            while menu_num not in ('1', '2', '3', '4'):
                print("Wrong menu!")
                menu_num = input(': ')
            if menu_num == '4':
                exit()
            elif menu_num == '1':
                self._clear()
                self._show_all_orders()
            elif menu_num == '2':
                self._clear()
                self._show_specific_order()
            elif menu_num == '3':
                self._clear()
                self._delete_order()

class Supreme_Admin(Admin):
    """This is the class for Supreme-Admin which is basically the owner of the store.
    This class will contain all the methods from parent class admin including a special
    method that can crate new accounts  for admin."""
    def __init__(self, admin_name):
        super().__init__(admin_name)

    def operate(self):
        """This is the main method that opearte Supreme-Admin class only role 'Supreme-Admin'
        can access this class"""
        self._welcome_admin()
        while True:
            print('==============================')
            print("Your Menu are the following :)")
            print('==============================')
            print("1.Show all orders")
            print("2.Show the specific order")
            print("3.Delete order")
            print("4.Modify product")
            print("5.Add new category")
            print("6.Add new product")
            print("7.Create new admin")
            print("8.Show all remaining product")
            print("9.Exit")
            print('==============================')
            print('Please type in menu number :)')
            menu_num = input(': ')
            while menu_num not in ('1', '2', '3', '4', '5',
                                   '6', '7', '8', '9'):
                print("Wrong menu!")
                menu_num = input(': ')
            if menu_num == '9':
                exit()
            elif menu_num == '1':
                self._clear()
                self._show_all_orders()
            elif menu_num == '2':
                self._clear()
                self._show_specific_order()
            elif menu_num == '3':
                self._clear()
                self._delete_order()
            elif menu_num == '4':
                self._clear()
                self._modify_product()
            elif menu_num == '5':
                self._clear()
                self._add_new_category()
            elif menu_num == '6':
                self._clear()
                self._add_new_product()
            elif menu_num == '7':
                self._clear()
                self._create_admin()
            elif menu_num == '8':
                self._clear()
                self._show_remaning_stock_of_all_product()

