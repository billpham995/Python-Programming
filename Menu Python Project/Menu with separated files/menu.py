## This python program displays menu for loading, adding and display records ##


# Display options for users
def menu_list():
    print("\nInventory options:")
    print("1. Load records")
    print("2. Add record")
    print("3. Display")
    print("4. Exit")

def main_menu():
    print("\n---Welcome to gwyn_hoang_siu program---")

    # Loop menu for user to do multiple tasks:
    while True:
        menu_list()
        choice = input("Please enter the option: ") # Ask user to choose an option

        if choice == "1": # if the input integer match with this number 1, it executes the function option_1()
            exec(open("loadRecord.py").read()) # open another python file, read and execute the codes within the file

        if choice == "2":
            exec(open("addRecord.py").read()) # open another python file, read and execute the codes within the file

        if choice == "3":
            exec(open("displayRecord.py").read())

        if choice == "4": # if this choice is chosen, the program stops
            print("\nExiting the program...")
            break

        # if user not entering digit 1 to 4, the program displays error and ask user to reenter. (Siu)
        if choice not in ["1", "2", "3", "4"]:
            print("\nError! Please enter the integer (1-4) for option.")

# Call the main function
main_menu()