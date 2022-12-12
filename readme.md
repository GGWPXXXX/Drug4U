# Drug4U
## Overview
This program is an online drug store system which have (almost) everything to open legit store such as customer, medicine and admin class.

  --- Developed by GG_WPX (Under MIT-LICENSE) ---

## Requirements.txt
Please install the module in requirement.txt
>pip install -r requirements.txt

## Main.py
The file named "Main.py" is the "main" program that brings together the three classes and two subclasses from the three different Python files.

### Main Functions
#### 1.Register 
This function will write new data account into file User_file/User_data.json

#### 2.Login 
This function will read the customer's username and check User data.json to see if it exists. If not, the program will ask the customer to type in a new username. If the username is correct, the program will ask for the password. If the password doesn't match the username, the program will alert the customer and ask for a new password if all of that complete the function will return username.

## Customer.py
Customer.py will have the customer class, which is for customers, and it will include a total of six methods and have a single attribute for it, which is the customer's name.

### Methods

#### 1.Welcome user

-This just presents a greeting for the customer to see.

#### 2.Take to menu animation 

-This is a little animation that plays before the customer is taken back to the main menu.

#### 3.Menu

-The Menu method will display all the pharmaceutical categories, along with the settings ,checkout and exit, and it will return the customer's choice as an int.

#### 4.Setting

-The customer will be able to set his or her own password, address, and telephone number through the setting.

#### 5.Add to cart

-This method will add the product that the customer is interested in to the json file that is located in the medicine directory. The purpose of including this in a file is to prepare for the possibility that a customer did not complete their purchase, in which case the information will be saved in the file automatically.

#### 6.Checkout

-After adding all of the customer's products to the json file with the name Orders.json, this method will erase any stale data from the json file named Cart.json. The purpose for writing in to Order.json is so that the admin who controls the order may control and see what is written in to Order.json.

## Medicine.py

This class is a class for medicine all the methods about medication are in here.
Such as show detail of the specific product that customer chose etc. And have a single attribute for it, which is the customer's name.

### Methods

####  1.Show medicine from user choice

This method gives the user the ability to select each medicine from the selected categories but before that the program will look if the amount of that medicine is less than zero, the program will hide the name of that medicine from the display and return name of the chosen medication.

#### 2.Ask user customer like products

There's nothing much with this method, It will ask the customer whether they like the current and that's all.

#### 3.Ask customer want buy how many

Using this method, the customer will be asked how many pieces of the product they like to purchase, and they will be informed if the quantity ordered is insufficient to meet their needs.Then it will write down the information to the Cart.json and return the amount of the product that customer want.

#### 4.Show detail of medicine.

This method will show a prescription for the selected medication. It will also display what, when, and how to use the medication, as well as any potential side effects, safety concerns, and the price of the medication.

## Admin.py

Admin.py is  a parent class named Admin and three sub-classes named, respectively,

### Roles

1.Stock manager : This role can modify each medication in medication database, add new category, add new product and  show all remaining product.

2.Sender : This role can see all of incoming orders as well as the specific order that required username of the customer and can delete the specific order.

3.Supreme-Admin : This role has absolute control over everything, including the capability to create new accounts for administrators.

### Methods

#### 1.Add new category
This method allow admin to add new category to the Medicine_Data.json

#### 2.Add new product
This method allow admin to add new product to the specific category.

#### 3. Modify product
This method allows admin to check or modify each product elements such as uses price
side effect or even stock of that product.

#### 4.Show all orders
This method will show all confirmed orders from Orders.json

#### 5.Show specific order
This method will show order of specific customer which required customer username to find.

#### 6.Create admin
By using this method, Supreme-Admin will be able to set up new accounts for other administrators.

#### 7.Delete order 
This method enables the sender to delete a particular order placed by a certain customer.

#### 8.Show remaining stock of all product
This method will show every single in every category including its amount.

## Cart.json

Cart. json is the primary shopping cart system for each individual customer. When they add a product to their cart, it will immediately write the new product down in the customer's cart. In the event that a customer adds an item to their shopping cart but does not complete their purchase, the information will be saved in a JSON file.

## Orders.json

The primary database for a customer's confirmed order is stored in the Order.json file. The following steps describe the pattern that the information follows.

    "a123": {
        "1": [
            "2.Amazon Basic Care Loperamide Hydrochloride Tablets, 2 mg, Anti-Diarrheal, 24 Count",
            250,
            2
        ],
        "2": [
            "1.Amazon Elements Vitamin C 1000mg 300 Tablets",
            1000,
            1
    }

This shows that the customer with the username a123 placed two separate orders on their initial purchase. They first ordered Amazon Basic Care Loperamide Hydrochloride Tablets, which have a price of 250 baht for two pieces, and then they ordered Amazon Elements Vitamin C 1000mg, which has a price of 1000 baht for one piece.