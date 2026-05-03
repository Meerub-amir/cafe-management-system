#Define the menu of restaurant
menu = {
    'pizza':2200,
    'coffee':500,
    'pasta':600,
    'steak':1200,
    'chicken burger':350,

}
#greating
print("welcome to my cafe")
print("pizza: Rs 2200\ncoffee: Rs 500\npasta: Rs 600\nsteak: Rs 1200\nchicken burger: Rs 350")
order_total = 0
#400 + 600 = 1000
item_1 = input("Enter the name of your item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 2200
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not avalaible yet!")
    another_order =  input("Do you want to add another item? (yes/No) ")
    if another_order == "yes":
        item_2 = input("Enter the name of your second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"item {item_2} has been added to order")
        else:
            print(f"ordered item {item_2} is not available!")
            
            print(f"The total amount of items to pay is {order_total}")