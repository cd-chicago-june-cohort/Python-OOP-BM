class Store (object):
    def __init__(self, product_arr, location, owner):
        self.product_arr = product_arr
        self.location = location
        self.owner = owner

    def add_product (self, product):
        self.product_arr.append(product)
        print (str(product) + ' added.')
        return self

    def rem_product (self, product):
        for i in self.product_arr:
            if (i==product):
                self.product_arr.remove(i)
                print (str(i) + ' removed.')
        return self

    def inventory (self):
        print '-' * 30
        print (str(self.owner) + "'s House of " + str(self.product_arr))
        print ('Located in downtown ' + str(self.location))
        return self

    
wares = ['bunson burners', 'mannequin heads', 'bubble gum', 'jumper cables']

bald_mart = Store (wares, 'Poughkeepsie', 'Bald Mike')

bald_mart.add_product('banjo').inventory()


bald_mart.rem_product('bunson burners').add_product('fishnet stockings').inventory()