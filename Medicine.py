import json


class Medicine:
    def __init__(self, username):
        self.__username = username

    # This method allow user to choose each medicine from the chosen categories.
    def show_medicine_from_user_choice(self, user_choice):
        menu_num_list = {1: "Digestive system", 2: "Pain", 3: "Infections and infestations", 4: "Allergic disorders",
                         5: "Nutrition", 6: "Setting"}
        print('====================')
        print(menu_num_list[user_choice])
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as medicine_data:
            data = json.load(medicine_data)
            for each_medicine_in_data, information in data[menu_num_list[user_choice]].items():
                print('====================')
                print(f"{each_medicine_in_data}")
                print()
                print(f"The price is {information['price']} Baht.")
            print('====================')
            choice = input('Which one would you like to see the information ? ')

            # list that counting how many medicine in that specific categories.
            num_med_list = [str(num) for num in range(1, len(data[menu_num_list[user_choice]].keys())+1)]

            # check that choice is correct or not.
            while True:
                if choice not in num_med_list:
                    print('Wrong choice amigo :)')
                    choice = input('Which one would you like to see the information ? ')
                else:
                    # method return choice of the specific medicine.
                    return choice

    # Show information about the very specific medicine that user chose from categories.
    def show_detail_of_medicine(self, chose_categories, chose_medicine_num):
        with open('../Drug4U/Medicine/Medicine_Data.json', 'r') as medicine_data:
            medi_data = json.load(medicine_data)
            for medicine in medi_data[chose_categories]:
                if int(medicine[0]) == int(chose_medicine_num):
                    print('===========================================')
                    print('---> Please read the prescription very carefully!. <---')
                    print('===========================================')
                    print()
                    print('---> What When and How to use this medication.')
                    print('===========================================')
                    print(medi_data[chose_categories][medicine]['uses'])
                    print()
                    print('---> This is side-effect of this medication. <---')
                    print('===========================================')
                    print(medi_data[chose_categories][medicine]['side-effect'])
                    print()
                    print('---> This is the precautions of this medication. <---')
                    print('===========================================')
                    print(medi_data[chose_categories][medicine]['precautions'])
                    print()
                    print('---> This is the price :) <---')
                    print('===========================================')
                    print(f"{medi_data[chose_categories][medicine]['price']} Baht")



# a = Medicine('GG_WPX')
# a.show_detail_of_medicine("Digestive system", 2)
