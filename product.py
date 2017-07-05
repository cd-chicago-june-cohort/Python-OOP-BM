class product (object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item = item_name 
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'

    def sell (self):
        self.status = 'sold'
        return self.status

    def add_tax (self, tax):
        self.price = self.price*(float(tax)) + self.price
        return self.price

    def return_item (self, reason):
        if (reason == 'defective'):
            self.status = 'defective'
            self.price = 0
    
        elif (reason == 'like new'):
            self.status = 'for sale'
        
        elif (reason == 'open box'):
            self.status = 'used'
            self.price = self.price * (.8)
    
        return self

    def display_all (self):
        print '-' * 30
        print ('Product: ' + str(self.item))
        print ('Price: $' + str(self.price))
        print ('Weight: ' + str(self.weight))
        print ('Brand: ' + str(self.brand))
        print ('Cost: $' + str(self.cost))
        print ('Status: ' + str(self.status))




product1 = product(20, 'shirt', '20lbs', 'Gap', 4)

print product1.display_all()