print ("Welcome to supermarket")
print(input("Press Enter to Continue "))
print ("1.Add item 2.Update Item 3.Delete Item 4.Reset Item")
option = int(input("Enter the option: "))

items = []
item ={}
def add_item (): 
    while True:
        item['name'] = str(input('Enter item name to buy (q to menu) : '))
        if item['name'].lower() == 'q':
            break
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

def 

add_item ()






