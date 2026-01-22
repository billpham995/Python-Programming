## This python program displays menu for loading, adding and display records ##
## Made by: H.Thong Pham, Siu L, Gwyn K ##

# Define parallel array to store shop items. (Siu)
# Product identification number
sku = []

# Product name and description such as Sets, Spider-man themed and specific type of clothes (Fleece)
it_name = []

# Product category, 5 items: Shirt, Coat, Pants, Accessories and Lounge
category = []

# Price of product, in AUD currency with 2 decimal (float) numbers
price = []

# Quantity of product availability
quantity = []

# Assign variable to False, indicating data must be loaded before viewing the full record  (Hoang)
data_loaded = False

##############################################################################################################################################

# Load records function (Hoang)
def load_data() -> None:
    global sku
    global it_name
    global category
    global price
    global quantity
    global data_loaded

    # Arrays with existed data
    sku0 = [1001, 2001, 3001, 4001, 2002, 5001, 4002, 3002, 1002, 4003]
    it_name0 = ["T-Shirt", "Fleece Jacket", "Slim fit Jeans", "Gloves", "Trench Coat", "Sleep Sets", "Socks", "Shorts", "Polo Shirt", "Belts"]
    category0 = ["Shirt", "Coat", "Pants", "Accessories", "Coat", "Lounge", "Accessories", "Pants", "Shirt", "Accessories"]
    price0 = [20, 39.99, 50, 5, 70.8, 18.99, 4.99, 25, 16.69, 2]
    quantity0 = [10, 20, 14, 14, 5, 36, 25, 19, 47, 14]

    # Loop the entire arrays and input the value to the defined parallel arrays
    klen = len(sku0)
    k = 0

    while k < klen:
        sku.append(sku0[k]) # add an element to (the end of) sku defined array
        it_name.append(it_name0[k]) # add an element to (the end of) it_name defined array
        category.append(category0[k]) # add an element to (the end of) category defined array
        price.append(price0[k]) # add an element to (the end of) price defined array
        quantity.append(quantity0[k]) # add an element to (the end of) quantity defined array
        k = k + 1
    data_loaded = True # Flag indicating that the data has been successfully loaded (Hoang)

    # Prompt the user data loaded successfully
    print("\nData loaded successfully.")

##############################################################################################################################################

# Add Record function (Gwyn)
def add_data() -> None:
    print("\n---Please enter detail to add record---")

    # To add new items:
    while True:
        sk = int(input("Enter sku: "))
        sku.append(sk) # add an element to (the end of) sku list

        it = str(input("Enter item name: "))
        it_name.append(it) # add an element to (the end of) it_name list

        cat = str(input("Enter category: "))
        category.append(cat) # add an element to (the end of) category list

        pr = float(input("Enter price: "))
        price.append(pr) # add an element to (the end of) price list

        qua = int(input("Enter quantity: "))
        quantity.append(qua) # add an element to (the end of) quantity list

        ans = input("Add another item? (Y/N): ") # prompt user to continue or stop
        if ans == "N": # The loop will exit if the user hits "N" (Siu)
            break

    # Prompt the user that record added successfully
    print("Record added successfully")

##############################################################################################################################################

# Display record function
def display_data() -> None:

    # Print headers accordingly to array
    # Format: "{0:^7s}".format("abc") s is stands for string formatting syntax; ^ align value in the centre
    print("{0:^6s}".format("SKU"), end="|")
    print("{0:^30s}".format("Item Name"), end="|")
    print("{0:^14s}".format("Category"), end="|")
    print("{0:^13s}".format("Price (AUD)"), end="|")
    print("{0:^10s}".format("Quantity"), end="|")
    print()

    # Loop entire parallel arrays and extract the data
    i = 0
    n = len(sku)
    while i < n:
        print("{0:^6}".format(sku[i]), end="|")
        print("{0:^30}".format(it_name[i]), end="|")
        print("{0:^14}".format(category[i]), end="|")
        print("{0:>13.2f}".format(price[i]), end="|")
        print("{0:>10}".format(quantity[i]), end="|")
        print()
        i += 1

##############################################################################################################################################

# Display options for users
def menu_list():
    print("\nInventory Options:")
    print("1. Load Records")
    print("2. Add Record")
    print("3. Display")
    print("4. Exit")

##############################################################################################################################################

# Main function:
def main_menu():
    print("\n---Welcome to gwyn_hoang_siu program---")

    # Loop menu for user to do multiple tasks:
    while True:
        menu_list()
        choice = input("Please enter the option: ") # Ask user to choose an option

        if choice == "1": # this option loads the data and used to display full data table
            load_data()

        if choice == "2": # this option prompts user to input new data
            add_data()

        if choice == "3":   # this option outputs data table. If option 1 or 2 is not chosen prior, this outputs empty table
            display_data()  # if option 2 is chosen priors, this outputs newly added data
                            # if option 1 is chosen priors, this outputs existed data
                            # if both options 1 and 2 are chosen, this outputs both newly added data and existed data

        if choice == "4": # if this choice is chosen, the program stops
            print("\nExiting the program...")
            break

        # if user not entering digit 1 to 4, the program displays error and ask user to reenter. (Siu)
        if choice not in ["1", "2", "3", "4"]:
            print("\nError! Please enter the integer (1-4) for option.")

# Call the main function
main_menu()