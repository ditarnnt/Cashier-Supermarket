class Transaction():
    def __init__(self):
        self.keranjang = dict ()
    
    def add_item (self, item_name, item_count, item_price):
        self.keranjang.update({item_name:[item_count,item_price,item_count*item_price]})
    
    def update_item_name (self, item_name, item_name_new):
        temp = self.keranjang[item_name]
        self.keranjang.pop[item_name]
        self.keranjang.update({item_name_new: temp})

    def update_item_qty (self,item_name,item_count_new):
        self.keranjang[item_name][0] == item_count_new

    def delete_item (self):
        self.keranjang.clear ()
    
    def check_order (self):
        data = pd.Dataframe(self.keranjang).T
        data.coloumns = ['item_name', 'item_count', 'item/price', 'Total Price']
        print(data.to_markdown())

    def order (self):
        a = str(input("Chekout y/n?"))
        if a.lower() == 'n':
            b = str(input('Adding more? y/n'))
            if b == 'y':
                self.update_item_name()
            else:
                



