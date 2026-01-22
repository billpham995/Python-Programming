# Define parallel array to store shop items. (Siu)
sku = []
it_name = []
category = []
price = []
quantity = []

# data_loaded = False

# This program will load the arrays with existed data to parallel array to be used with other functions - Add Record and Display Record
def load_data() -> None:
    global sku
    global it_name
    global category
    global price
    global quantity

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
        sku.append(sku0[k])
        it_name.append(it_name0[k])
        category.append(category0[k])
        price.append(price0[k])
        quantity.append(quantity0[k])
        k = k + 1
    # data_loaded = True

    # Prompt the user data loaded successfully
    print("Data loaded successfully.")

# Call the function
load_data()

