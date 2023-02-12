import pandas as pd
import tabulate

class Transaction():
    def __init__(self):
        self.keranjang = dict ()
    
    def add_item (self, item_name, item_count, item_price):
        item_total = item_count*item_price
        self.keranjang.update({item_name:[item_count,item_price,item_total]})
    
    def update_item_name (self, item_name, item_name_new):
        temp = self.keranjang[item_name]
        self.keranjang.pop(item_name)
        self.keranjang.update({item_name_new: temp})

    def update_item_qty (self,item_name,item_count_new):
        self.keranjang[item_name][0] = item_count_new
        self.keranjang[item_name][2] = item_count_new*self.keranjang[item_name][1]

    def update_item_price (self, item_name, item_price_new):
        self.keranjang[item_name][1] = item_price_new
        self.keranjang[item_name][2] = item_price_new*self.keranjang[item_name][0]

    def delete_item (self):
        self.keranjang.clear ()
    
    def check_order (self):
        if len(self.keranjang) == 0: 
            print ("You have no item in order list")
        else:
            data = pd.DataFrame(self.keranjang).T
            data.columns = ['Quantity', 'Item/Price', 'Total Price']
            print(data.to_markdown())
        
    def delete_item (self, item_name):
        self.keranjang.pop(item_name)
    
    def reset_item (self):
        self.keranjang.clear()
        
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