
from Cashier import Transaction

# program state:
# input/update/delete order "ordering"
# confirm order "checking"
# purchase "confirm"

#initial state 
state = "ordering" 
#call file transaction
trans = Transaction()
print("=== Welcome to Our Supermarket===\n")


while True:
    match state: 
        #This state imply to adding and also to list all the item of customer 
        case "ordering" :  
            #user input
            option = int(input("0. Exit Menu\n1. Add Item\n2. List Item\n"))
            
            #validated_string is a function to remove the space in the begining, in the middle, and at the end of item_name 
            def validated_string(msg):
                return " ".join(msg.split())
            match option: 
                case 0:
                    #exit program
                    print ("Thank You!") 
                    break
                case 1 :
                    #adding item (str), quantity (int), and item price(int)
                    print ("Adding Item (item name,quantity item, price item)\n")
                    item_name = str (input("Item Name: "))
                    item_count = int (input("Quantity: "))
                    item_price = int (input("Price: "))
                    trans.add_item (validated_string(item_name).lower(),item_count, item_price)
                
                case 2:
                    #checking order
                    print ("\nHere are your items!\n")
                    trans.check_order ()
                    #The break point of state ordering is when user choose to check their cart order  
                    state = "checking"
        
        # This state is imply to update's customer cart list 
        case "checking":
            #user input
            option = int(input("\n0. Start Menu\n1. Update Item\n2. Update Quantity\n3. Update Price\n4. Delete Item \n5. List Item\n6. Clear Item\n7. Purchase Item\n"))

            match option:
                case 0:
                    # This case when user wants to adding more of their item in cart list
                    print ("You will be back to first menu\n")
                    state = "ordering"

                case 1: 
                    #Customer decide to updating their name of item. 
                    #Input: item_name(str) and item_name_new(str)
                    #Updating name of item only works if customer's cart list is not empty.  
                    if len(trans.keranjang) != 0 :
                        print("\nUpdate name of item (old name of item, new name of item)\n")
                        item_name = str(input("Old Item Name: "))
                        item_name_new = str (input("New Item Name: "))

                        #Call validated_string function to remove the space 
                        trans.update_item_name(validated_string(item_name).lower(), validated_string(item_name_new).lower())
                    
                    else:
                        print("\nYou don't have any item in cart list, please add item before update name of item, thank you!\n")
                        #Customer move to state ordering, to fill their cart list
                        state = "ordering"

                case 2: 
                    #Customer decide to updating their quantity of item. 
                    #Input: item_name(str) and item_count_new(int).
                    #Updating quantity of item only works if customer's cart list is not empty. 
                    if len(trans.keranjang)!=0:
                        print ("\nUpdate quantity of item (name of  item, new quantity of item)\n")
                        item_name = str(input("Item Name: "))
                        item_count_new= int (input("New Quantity: "))

                        #Call validated_string function to remove the space 
                        trans.update_item_qty (validated_string(item_name).lower(), item_count_new)

                    else:
                        print("\nYou don't have any item in cart list, please add item before update quantity of item, thank you!\n")
                        #Customer move to state ordering, to fill their cart list
                        state = "ordering"

                case 3: 
                    #Customer decide to updating their price of item. 
                    #Input: item_name(str) and item_price_new(int).
                    #Updating price of item only works if customer's cart list is not empty. 
                    if len(trans.keranjang) != 0:
                        print ("\nUpdate price of item (name of item, new price of item)\n")
                        item_name = str(input("Item Name: "))
                        item_price_new = int(input("New Price: "))

                        #Call validated_string function to remove the space 
                        trans.update_item_price(validated_string(item_name).lower(), item_price_new)

                    else: 
                        print("\nYou don't have any item in your cart list, please add item before update price of item, thank you!\n")
                        #Customer move to state ordering, to fill their cart list
                        state = "ordering"

                case 4:
                    #Customer decide to delete item in cart. 
                    #Input: item_name(str).
                    #Delete only works if the customer's cart list is not empty.
                    if len(trans.keranjang) != 0:
                        print ("\nDelete Item in List (name of item)\n")
                        item_name = str(input("Item Name: "))
                        trans.delete_item(validated_string(item_name).lower())

                        #Customer delete item one by one until their cart = 0
                        if len(trans.keranjang) == 0:
                            print ("\nitem empty\n")
                            #Customer move to state ordering, to fill their cart list 
                            state = "ordering"
                    else:
                        #Since the beginning, customer don't have anything to delete. 
                        print("\nYou don't have any item in your cart list\n")
                        #Customer move to state ordering, to fill their cart list
                        state = "ordering"             
                
                case 5: 
                    #Customer check their updated cart list
                    if len(trans.keranjang) != 0:
                        print ("\nHere are your updated list of item\n")
                        trans.check_order()

                    else:
                        #Customer don't have anything in their cart, move to state ordering
                        print("\nYou don't have any item in your cart list\n")
                        state = "ordering"


                case 6:
                    #Customer wants to delete ALL of their item in their cart
                    #Reset can works only if customer have item in their cart
                    if len(trans.keranjang) != 0:
                        trans.reset_item()
                        print ("\nItem has been clear\n")
                        state = "ordering"

                    else:
                        #Customer don't have anything to reset in their cart, move to state ordering
                        print("\nYou don't have any item in your cart list\n")
                        state = "ordering"

                    
                case 7:
                    #Customer wants to purchase 
                    #Purchasing of item only works if customer's cart list is not empty. 
                    if len(trans.keranjang) != 0:
                        state = "confirm"
                    else:
                        #Customer don't have anything in their cart to purchase, move to state ordering
                        print("\nYou don't have any item in cart list, please add item before purchasing, thank you!\n")
                        state = "ordering"
                    

        case "confirm" :
            # This state is imply to check out customer's cart list
            print ("\nHere are your order list\n")
            #Show customer's cart list and sum prices of their item
            trans.purchase()
            #Show discount
            trans.after_discount()
            #Ask customer if they sure to purchase.
            #Option: input (str)
            option = str(input ("Do you wish to process? y/n: "))
            if option.lower() == 'y':
                print ("\nThank you for shopping in Our Supermarket!\n")
                break #Exit program
            else:
                #If Customer input == n, program will be back to ordering state 
                print ("\nYou will be back to adding menu\n")
                state = "ordering"


            



