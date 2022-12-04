import json


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

    def clear(self):
        print('\n'*40)

    def add_new_categories(self):
        print('What is the name of the new category?')
        category = input(': ')
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as med:
            med_data = json.load(med)


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

            # Check whether the categories input was right.
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




    def admin_menu(self):
        with open('../Drug4U/Admin_file/Admin_data.json', 'r')as data:
            admin_data = json.load(data)
            print(admin_data)
            if admin_data[self.__username]['role'] == 'Stock_manager':
                print("")

    def show_and_modify_orders(self):
        with open('../Drug4U/Admin_file/Orders.json', 'r') as order:
            order_data = json.load(order)
        print(order_data)







admin = Admin('stock')
admin.modify_stock()
