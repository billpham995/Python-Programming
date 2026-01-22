# Python Script add a new row to the table of data

# Connect loadRecord python file
import loadRecord

### The Algorithm to add new row ###

print("\n---Please enter detail to add record---")

# To add new items: (Siu)
while True:
    sk = int(input("Enter sku: "))
    loadRecord.sku.append(sk) # add an element to (the end of) sku list

    it = str(input("Enter item name: "))
    loadRecord.it_name.append(it) # add an element to (the end of) it_name list

    cat = str(input("Enter category: "))
    loadRecord.category.append(cat) # add an element to (the end of) category list

    pr = float(input("Enter price: "))
    loadRecord.price.append(pr) # add an element to (the end of) price list

    qua = int(input("Enter quantity: "))
    loadRecord.quantity.append(qua) # add an element to (the end of) quantity list

    ans = input("Add another item? (Y/N): ") # prompt user to continue or stop
    if ans == "N": # The loop will exit if the user hits "N" (Siu)
        break

# Prompt the user that record added successfully
print("Record added successfully")



