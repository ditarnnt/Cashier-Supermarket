
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
**Adding Item**
![1 adding item](https://user-images.githubusercontent.com/68722344/218322040-65cbcd3a-e4fa-4236-9541-d40c7d3393e3.PNG)

**Cart of List Item**
![2 list item](https://user-images.githubusercontent.com/68722344/218322060-f17526ab-02af-4aaf-bd40-b64fa694ad5b.PNG)

**Update Item Name**
![3 update item](https://user-images.githubusercontent.com/68722344/218322064-42c50b68-b9be-4b55-8120-755b129eced9.png)

**Update Item Quantity**
![4 update quantity](https://user-images.githubusercontent.com/68722344/218322067-f5e5c6ee-cae6-4d85-ae7e-9daedd49bb69.png)

**Update Item Price**
![5 update price](https://user-images.githubusercontent.com/68722344/218322073-604ffd00-10fc-4cf0-863e-7d8335a0a919.png)

**Back to Starting Menu**
![6 back to 0 menu](https://user-images.githubusercontent.com/68722344/218322078-aef60021-26cd-4a99-958e-229e4592ee64.png)

**List of Item**
![7 list item](https://user-images.githubusercontent.com/68722344/218322083-60bc0355-bc82-4eca-b2a7-e33ce6260e53.png)

**Delete Item**
![8 delete item](https://user-images.githubusercontent.com/68722344/218322087-e1514a57-914f-4ef6-80ab-27c6e1d0598d.png)

**Purchase Item - Customer input no**
![9 purchase no](https://user-images.githubusercontent.com/68722344/218322090-bce6baf7-8c0a-4a43-b539-e5f7ac7425bb.png)

**Reset Cart of List**
![10 clear item](https://user-images.githubusercontent.com/68722344/218322092-7904e0b4-2e75-45fc-b386-53766ccdfa77.png)

**Purchase Zero Item**
![11 purchase no item](https://user-images.githubusercontent.com/68722344/218322096-4cd270a6-e8ab-4d47-b78a-8e6cfa86f9a2.png)

**Update Name of Zero Item**
![12 update item cant](https://user-images.githubusercontent.com/68722344/218322099-c4f60da8-d4c0-43bf-9bd1-8c7831c1a5f0.png)

**Update Quantity of Zero Item**
![13 update quantity cant](https://user-images.githubusercontent.com/68722344/218322102-92d0b2ef-fa2c-40e4-bc37-1aafdca20749.png)

**Update Price of Zero Item**
![14 update price cant](https://user-images.githubusercontent.com/68722344/218322105-9c6ba0b5-f387-49ca-830c-37f1760aafd5.png)

**Delete Zero of Item**
![15 cant delete](https://user-images.githubusercontent.com/68722344/218322112-0ce995e5-7c86-4322-9212-0f1c2a87ed72.png)

**Purchase cart of Item, Customer input yes**
![16 purchase yes](https://user-images.githubusercontent.com/68722344/218322117-c1707c25-5d3d-4203-84ac-69fa055ca419.png)

# Further Program
- Adding input of name only in alphabet 
- Integrate with databases such as SQL
