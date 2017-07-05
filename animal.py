class Animal (object):
    def __init__ (self, name, health):
        self.name = name
        self.health = health

    def walk (self):
        self.health -= 1
        return self

    def run (self):
        self.health -= 5
        return self

    def display_health (self):
        if (self.health <= 0):
            print (str(self.name) + "'s dead, baby.")
        elif (self.health > 0):
            print (str(self.name) + "'s health level is " + str(self.health))
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet (self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly (self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a MF Dragon"

# Create instance of animal, make it walk 3x, run 2x, display health:
animal1 = Animal('Larry Hoover', 13)
animal1.walk().walk().walk().run().run().display_health()

# # Create instance of Dog, make it walk 3x, run 2x, display health:
# animal2 = Dog('Chopper')
# animal2.walk().pet().pet().walk().walk().run().run().display_health()

animal3 = Dragon('Jeff, The Huge Nerd Dragon')
animal3.fly().fly().display_health()