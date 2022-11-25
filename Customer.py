import json
from Medicine import Medicine


class Customer:
    def __init__(self, username):
        self.__username = username

    # getter for username
    @property
    def username(self):
        return self.__username

    # setter for username
    @username.setter
    def username(self, new_value):
        self.__username = new_value

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
        menu_choice = int(input('Please input number:) '))

        # Check if user input is the correct menu number or not.
        menu_num_list = {1: "Digestive system", 2: "Pain", 3: "Infections and infestations", 4: "Allergic disorders",
                         5: "Nutrition", 6: "Setting"}
        while True:
            if menu_choice in menu_num_list.keys():
                return menu_choice
            print('---> Are you blind? <---')
            menu_choice = int(input('Please input the correct number :( '))

    def main(self):
        menu_num_list = {1: "Digestive system", 2: "Pain", 3: "Infections and infestations", 4: "Allergic disorders",
                         5: "Nutrition", 6: "Setting"}

        # show all categories then return chosen choice
        menu_num = self.menu()
        # This method allow user to choose each medicine from the chosen categories.
        chose_medicine_num = Medicine.show_medicine_from_user_choice(self.__username, menu_num)
        # Show information about the very specific medicine that user chose from categories.
        Medicine.show_detail_of_medicine(self.__username, menu_num_list[menu_num], chose_medicine_num)



# c = Customer('GG_WPX')
# c.show_chose_menu()
