
from Cashier import Transaction

# state dari program:
# input/update/delete order "input"
# confirm order "confirm"

state = "ordering"
trans = Transaction()
print("Welcome to Supermarket\n")

while True:
    match state: 
        case "ordering" : 
            #print("1.Add Item\n", "2.List Item\n")
            option = int(input("1.Add Item\n2.List Item\n"))
            match option: 
                case 1 :
                    print ("Adding Item (item name,quantity item, price item)\n")
                    item_name__ = str (input("Item Name: "))
                    item_count = int (input("Quantity: "))
                    item_price = int (input("Price: "))

                    item_name_ = item_name__.split()
                    item_name = " ".join(item_name_)

                    trans.add_item (item_name.lower(),item_count, item_price)
                
                case 2:
                    print ("\nHere are your items\n")
                    trans.check_order ()
                    state = "checking"

        case "checking":
            option = int(input("\n0. Start Menu\n1. Update Item\n2. Update Quantity\n3. Update Price\n4. Delete Item \n5. List Item\n6. Clear Item\n7. Purchase Item\n"))

            match option:
                case 0:
                    print ("You will be back to adding menu\n")
                    state = "ordering"

                case 1: 
                    if len(trans.keranjang) != 0 :
                        print("\nUpdate name of item (old name of item, new name of item)\n")
                        item_name__ = str(input("Old Item Name: "))
                        item_name_ = item_name__.split()
                        item_name = " ".join(item_name_)

                        item_name_new__ = str (input("New Item Name: "))
                        item_name_new_ = item_name_new__.split()
                        item_name_new = " ".join(item_name_new_)

                        trans.update_item_name(item_name.lower().rstrip().lstrip(), item_name_new.lower().rstrip().lstrip())
                    else:
                        print("\nYou dont have any item in cart list, please add item before update name of item, thank you\n")
                        state = "ordering"

                case 2: 
                    if len(trans.keranjang)!=0:
                        print ("\nUpdate quantity of item (name of  item, new quantity of item)\n")
                        item_name__ = str(input("Item Name: "))
                        item_name_ = item_name__.split()
                        item_name = " ".join(item_name_)

                        item_count_new= int (input("New Quantity: "))

                        trans.update_item_qty (item_name.lower().rstrip().lstrip(), item_count_new)

                    else:
                        print("\nYou dont have any item in cart list, please add item before update quantity of item, thank you\n")
                        state = "ordering"

                case 3: 
                    if len(trans.keranjang) != 0:
                        print ("\nUpdate price of item (name of item, new price of item)\n")
                        item_name__ = str(input("Item Name: "))
                        item_name_ = item_name__.split()
                        item_name = " ".join(item_name_)

                        item_price_new = int(input("New Price: "))

                        trans.update_item_price(item_name.lower().rstrip().lstrip(), item_price_new)

                    else: 
                        print("\nYou dont have any item in your cart list, please add item before update price of item, thank you\n")
                        state = "ordering"

                case 4:
                    if len(trans.keranjang) != 0:
                        print ("\nDelete Item in List (name of item)\n")
                        item_name__ = str(input("Item Name: "))
                        item_name_ = item_name__.split()
                        item_name = " ".join(item_name_)

                        trans.delete_item(item_name.lower().rstrip().lstrip())

                        if len(trans.keranjang) == 0:
                            print ("\nitem empty\n")
                            state = "ordering"
                    else:
                        print("\nYou dont have any item in your cart list\n")
                        state = "ordering"             
                
                case 5: 
                    if len(trans.keranjang) != 0:
                        print ("\nHere are your updated list of item\n")
                        trans.check_order()

                    else:
                        print("\nYou dont have any item in your cart list\n")
                        state = "ordering"


                case 6:
                    if len(trans.keranjang) != 0:
                        trans.reset_item()
                        print ("\nItem has been clear\n")
                        state = "ordering"

                    else:
                        print("\nYou dont have any item in your cart list\n")
                        state = "ordering"

                    
                case 7:
                    if len(trans.keranjang) != 0:
                        state = "confirm"
                    else:
                        print("\nYou dont have any item in cart list, please add item before purchasing, thank you\n")
                        state = "ordering"
                    

        case "confirm" :
            print ("\nHere are your order list\n")
            trans.purchase()
            trans.after_discount()
            option = str(input ("Do you wish to process? y/n: "))
            if option.lower() == 'y':
                print ("\nThank you for shopping in our supermarket\n")
                break
            else:
                print ("\nYou will be back to our menu\n")
                state = "ordering"


            



