
from Cashier import Transaction

# state dari program:
# input/update/delete order "input"
# confirm order "confirm"

state = "ordering"
trans = Transaction()
print("Welcome to Supermarket")

while True:
    match state: 
        case "ordering" : 
            #print("1.Add Item\n", "2.List Item\n")
            option = int(input("1.Add Item\n2.List Item\n"))
            match option: 
                case 1 :
                    print ("Adding Item (item name,quantity item, price item )")
                    item_name = str (input("Item Name: "))
                    item_count = int (input("Quantity: "))
                    item_price = int (input("Price: "))
                    trans.add_item (item_name, item_count, item_price)
                
                case 2: 
                    print ("Here are your items")
                    trans.check_order ()
                    state = "checking"

        case "checking":
            option = int(input("1. Update Item\n2. Update Quantity\n3. Update Price\n4.Delete Item \n5. List Item\n6.Clear Item\n7. Purchase Item\n"))

            match option:
                case 1: 
                    print("Update name of item (old name of item, new name of item)")
                    item_name = str(input("Old Item Name: "))
                    item_name_new = str (input("New Item Name: "))
                    trans.update_item_name(item_name, item_name_new)

                case 2: 
                    print ("Update quantity of item (name of  item, new quantity of item)")
                    item_name = str(input("Item Name: "))
                    item_count_new= str (input("New Quantity: "))
                    trans.update_item_qty (item_name, item_count_new)

                case 3: 
                    print ("Update price of item (name of item, new price of item)")
                    item_name = str(input("Item Name: "))
                    item_price_new = int(input("New Price: "))
                    trans.update_item_price(item_name, item_price_new)

                case 4:
                    print ("Delete Item in List (name of item)")
                    item_name = str(input("Item Name: "))
                    trans.delete_item(item_name)
                    if len(trans.keranjang) == 0:
                        print ("item empty")
                        state = "ordering"                
                case 5: 
                    print ("Here are your update list of item")
                    trans.check_order()

                case 6:
                    trans.reset_item()
                    print ("Item has been clear")
                    state = "ordering"
                    
                case 7:
                    state = "confirm"

        case "confirm" :
            print ("Here are your order list")
            trans.purchase()
            trans.after_discount()
            option = str(input ("Do you wish to process? y/n: " ))
            if option.lower() == 'y':
                print ("Thank you for shopping in our supermarket")
                break
            else:
                state = "ordering"


            



