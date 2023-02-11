
# Project Background

This project is to create cashier self service supermarket program. Where customer can add item that they want to buy, quantity of item, also the price. This project supposely for bootcamp program called PacManAI (Go check them here: https://pacmann.io/). 

This program has journey customer as follow: 
    
    1.  Adding Item
    2.  Update Item Name
    3.  Update Item Quantity
    4.  Update Item Price
    5.  Delete Item 
    6.  Reset Transaction 
    7.  Check Order
    8.  Purchase Item 
    9.  Purchase after Discount
    10. Reset item, or purchase item. 

# Tools
**Languages**: 

Python 
* Class 
* Function 
* Clean Code 
* Data Structure 
* Branching 
* Git 

**Library**: 

* Pandas 
* Tabular 

# Program Description 
This program have objective as follow:  
1. State Ordering 
State ordering contains 2 function 
-  Customer inputs their cart with item that they want to buy. They also have to insert item name, quantity item, and price item 

```
trans.add_item (item_name, item_count, item_price)
```

- Customer checks their cart list 

```
trans.check_order ()
state = "checking"
```
* This state will always reccuring to adding cart, until customer choose to review their cart list 

2. State Checking 
State Checking contain 7 function 
-  Customer wants to update their name of item, 
```
trans.update_item_name(item_name, item_name_new)
```
- Customer wants to update their quantity of item
```
trans.update_item_qty (item_name, item_count_new)
```
- Customer wants to update their price of item 
```
trans.update_item_price(item_name, item_price_new)
```

- Customer wants to delete item in cart list 

```
trans.delete_item(item_name)
```
- Customer wants to reset or delete all item in cart. 

```
trans.reset_item()
```

If the cart list is empty, customer will be back to ordering state to input their cart list.


- Customer wants to checks their updated cart list.

```
trans.check_order ()
```

- Customer wants to purchase their cart list
```
state = "checking"
```

This state will always reccuring, until customer choose to purchase item

3. State Confirm 
- State Confirm shows the sum of cart item 
```
trans.purchase()
```
- If the customer spending on the conditions that have been given, customer can get discount
```
trans.after_discount()
```
- If the customer wish to proceded the transaction, the program will finish, else the customer will be back to ordering state
```
option = str(input ("Do you wish to process? y/n: " ))
if option.lower() == 'y':
    print ("Thank you for shopping in our supermarket")
    break
else:
    state = "ordering"
```
# Try It by Yourself!
- Git Clone or download this repository 
- Open Cashier.py and main.py
- On Vscode terminal execute 

```bash
python main.py
```

# Test Case

