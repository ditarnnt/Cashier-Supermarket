import pandas as pd
import tabulate

class Transaction():
    def __init__(self):
        #initialitation in dictionary 
        self.keranjang = dict ()

        """
        input: item_name(str), count(int), price(int), total(int)

        self.keranjang = item_name{
            count,
            price,
            total}

        example: 
        self.keranjang = shrimp{
            2,
            2000,
            4000}
        }
        """
    
    #method to add item 
    def add_item (self, item_name, item_count, item_price):
        #item total = price per item*count of item
        item_total = item_count*item_price
        self.keranjang.update({item_name:[item_count,item_price,item_total]})
    
    #method to update item name 
    #Input: item_name (str), item_name_new (str)
    def update_item_name (self, item_name, item_name_new):
        #temp is temporary variabel to accomodate item name old 
        temp = self.keranjang[item_name]
        #using pop to delete item_name 
        self.keranjang.pop(item_name)
        # change item_new_name in temp 
        self.keranjang.update({item_name_new: temp})

    #method to update quantity 
    #input: item_name (str), item_count_new(int)
    def update_item_qty (self,item_name,item_count_new):
        #self.self.keranjang[item_name][0] is item count old, switch it with the item count new
        self.keranjang[item_name][0] = item_count_new

        #self.keranjang[item_name][2] is total price
        #self.keranjang[item_name][1] is price per item 
        #total price is price per item*item count new 
        self.keranjang[item_name][2] = item_count_new*self.keranjang[item_name][1]

    #method to update price
    #input: item_name (str), item_count_new(int)
    def update_item_price (self, item_name, item_price_new):
        #self.keranjang[item_name][1] is price per item old, switch it with the item name new
        self.keranjang[item_name][1] = item_price_new

        #total price is price per item new*item count
        self.keranjang[item_name][2] = item_price_new*self.keranjang[item_name][0]

    #method to reset all the items in dictionary
    def delete_item (self):
        self.keranjang.clear ()
    
    #method to check order in list 
    def check_order (self):
        if len(self.keranjang) == 0: 
            print ("You have no item in order list")
        else:
            #make tabulate data in dataframe using pandas 
            data = pd.DataFrame(self.keranjang).T
            data.columns = ['Quantity', 'Item/Price', 'Total Price']
            print(data.to_markdown())
    
    #method to delete ite one by one 
    def delete_item (self, item_name):
        self.keranjang.pop(item_name)
    
    #method to reset all the items in dictionary
    def reset_item (self):
        self.keranjang.clear()

    #ex    
    def purchase (self):
        data = pd.DataFrame(self.keranjang).T
        data.columns = ['item_count', 'item/price', 'Total Price']
        print(data.to_markdown())
        print(f"\nGrand Total {sum(data['Total Price'])}")

    def after_discount (self):
        data = pd.DataFrame(self.keranjang).T
        data.columns = ['item_count', 'item/price', 'Total Price']
        total_price =  sum(data["Total Price"])
        discount = 0 
        if total_price > 500_000:
            discount = 0.1
            print ("You got 10% discount")
        elif total_price > 300_000:
            discount = 0.08
            print ("You got 8% discount")
        elif total_price > 200_000:
            discount = 0.05 
            print ("You got 5% discount")
        price_after_discount = total_price*(1-discount)
        print (price_after_discount)