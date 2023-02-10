# Create a hello funtion that prints a greeting to the user with no return arguments

def hello()
    print("hello, how is your day?")
hello()

# A function named pack() that accepts three arguments, and returns a 
# single list with the three arguments inside as list elements.

def pack (item1,item2,item3):
    return = [item1, item2, item3]
print(pack("water_bottle","candy_bar","first_aid_kit"))

# A function called eat_lunch(). This function should accept a list of any length, and print out a series 
# of strings that say "First I eat __" (the first element of the list), and
#  "Next I eat ___" (for the following elements in the list). If the list
#  is empty, print "My lunchbox is empty!". The function should not return anything.

lunch_items = ["steak","dr.pepper","mashed_potatos","pie"]
forgot_lunch = []
quick_lunch = ["lunchable"]

def eat_lunch(list_item):
    if len(list_name) == 0:
        print("My lunchbox is empty!")
    else:
        for x in range(len(list_name)):
            if x == 0:
                print(f"First I eat {list_name[0]}.")
            else:
                print(f"Next I eat {list_name[x]}")

eat_lunch(lunch_items)
eat_lunch(forgot_lunch)
eat_lunch(quick_lunch)