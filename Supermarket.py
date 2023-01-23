print ("Welcome to supermarket")
print(input("Press Enter to Continue "))
def menu ():
    print ("1.Add item\n 2.Update Item\n 3.Delete Item\n 4.Reset Item\n")
    return

option = int(input("Enter the option: "))

items = []
item ={}
def add_item (): 
    print ("----- add groceries -----")
    while True:
        item['name'] = str(input('Enter item name to buy (q to menu) : '))
        if item['name'].lower() == 'q':
            break #back to menu 
        else: 
            while True:
                try:
                    item['jumlah item'] = str(input('count item : '))
                    break
                except ValueError:
                    print('count of item should in digits')
            while True:
                try:
                    item['prices per item'] = str(input('prices per item : '))
                    break
                except ValueError:
                    print('prices per item should in digits')
        return (items.append(item))

def view_item ():
    print("----- update groceries -----")
    print(f"These are the list of your Grocery, you have: {len({items})}")
    while len(items)!= 0:
        print ("Your Groceries's list")
        for item in items:
            for key,value in item.items():
                print(key,':',value)
            break
    








