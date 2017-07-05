class car (object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if (price <= 10000):
            self.tax = .12
        elif (price > 10000): 
            self.tax = .15

    def display_all(self):
        print ('Price: ' + str(self.price))
        print ('Speed: ' + str(self.speed))
        print ('fuel: ' + str(self.fuel))
        print ('Mileage: ' + str(self.mileage))
        print ('Tax: ' + str(self.tax))
        print '*' * 30



car1 = car(2000, '35pmh', 'Full', '15mpg')
car2 = car(2000, '5mph', 'Not full', '105mpg')
car3 = car(2000, '15mph', 'Kind of full', '95mpg')
car4 = car(2000, '45mph', 'Full', '25mpg')
car5 = car(2000, '25mph', 'Empty', '25mpg')
car6 = car(20000000, '35mph', 'Empty', '15mpg')

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()