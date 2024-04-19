import time
import os

def new_order(order, things):
    print("We have fries, burgers and cola for you. We recommend to try each of it")
    time.sleep(1)
    print(f"Creating order number {order}")
    print()
    order = {}
    for item in things:
        while True:
            amount = input(f"Enter the amount of '{item}': ")
            if amount.isdigit():
                order[item] = int(amount)
                break
            else:
                print("Please enter a valid number for quantity.")
    print ("Thanks for ordering. Next user please!")
    print()
    return order

def save_order(order_number, order):
    create_time = time.ctime().replace(' ', '-').split('.')[0].strip()
    filename = f"Orders1/{order_number}+{create_time}"
    with open(filename, 'a') as f:
        f.write(f"= = = = = = = = = = = = = = = = = =\n")
        f.write(f"Order #{order_number}\n")
        f.write(f"Created at: {create_time}\n")
        f.write(f"= = = = = = = = = = = = = = = = = =\n")
        f.write(f"The selected items:\n")
        for item, quantity in order.items():
            f.write(f"{item}: {quantity} \n")
        f.write(f"= = = = = = = = = = = = = = = = = =\n")

def main():
    menu_items = ["Cola", "Fries", "Burger"]
    order_number = 1
    orders = {}
    while True:
        user_ready = input("Hello! Are you ready to order? Answer with yes or no: ")
        try:
            if user_ready.lower() == "yes":
                orders_dir = 'Orders1'
                if not os.path.exists(orders_dir):
                    os.makedirs(orders_dir)
                orders[order_number] = new_order(order_number, menu_items)
                save_order(order_number, orders[order_number])
                order_number += 1
            elif user_ready.lower() == "no":
                print("Let us know when you're ready to order.")
                time.sleep(2)
                os.system("clear") 
                break
            else:
                print("I don't understand. Please enter 'yes' or 'no'.")
                time.sleep(2)
                print("...Are you still here? Please enter yes or no")
        except:
            print("Sorry, I didn't get that. Please answer 'yes' or 'no' starting with a small letter.")

main()



