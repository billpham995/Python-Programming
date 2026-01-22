# Load loadRecord python file (Siu)
import loadRecord

# To display message if loadRecord file cannot be loaded. (Siu)
# if not loadRecord.data_loaded:
#     print("No data found. Please load records first.")
#
# else:

# To display records. (Siu)
print("\nInventory Table:")

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
n = len(loadRecord.sku)
while i < n:
    print("{0:^6}".format(loadRecord.sku[i]), end="|")
    print("{0:^30}".format(loadRecord.it_name[i]), end="|")
    print("{0:^14}".format(loadRecord.category[i]), end="|")
    print("{0:>13.2f}".format(loadRecord.price[i]), end="|")
    print("{0:>10}".format(loadRecord.quantity[i]), end="|")
    print()
    i += 1
