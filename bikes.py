class Bike (object):
    def __init__(self, price, max_speed):
        self.dictionary = {}
        self.order = []
        self.price = price
        self.speed = max_speed
        self.miles = 0


    def display_info(self):
        print ('This bike was ' + str(self.price) + ', it goes ' + str(self.speed) + ' and it has ' + str(self.miles) + ' miles on it.')

    def ride(self):
        print 'riding'
        self.miles += 10
        return self.miles

    def reverse(self):
        print 'reversing'
        if (self.miles == 0):
            print "You're at ZERO, you can't go back..."
            return self.miles
        else:
            self.miles -= 5
            return self.miles


bike1 = Bike('$150', '150mph')
bike2 = Bike('$500', '500mph')
bike3 = Bike('$1000', '1000mph')



bike1.display_info()
bike1.ride()
bike1.ride()
bike1.ride()
bike1.display_info()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.reverse()
bike2.display_info()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.display_info()