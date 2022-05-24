# Introduction to Class
#   - Introduction to Object-Oriented Programming (OOP)

class Animal:
    # Constructor
    #   - Creates a new Animal object
    def __init__(self, name: str):
        self.name = name
        self.colour = ""
        self.age = 0        # in years
        self.weight = 0     # in kgs

        print("Created a new Animal!")

    def breathe(self):
        """Print '---{name} breathes in and out---'"""
        print(f"---{self.name} breathes in and out ---")


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name) # superclass constructor
        self.sassy = True

    def meow(self):
        print("Meow.")
        print(f"My name is {self.name}.")

    def breathe(self):
        print(f"--{self.name} purrs as it breathes")

class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.loyal_friend = True

    def bark(self):
        print(f"{self.name}: Woof Woof")

    def breathe(self):
        print(f"{self.name} pants as he breathes.")


# Create a new Animal object
fred = Animal("Fred")  # this is a call to __init__()

# Check fred's Type
print(type(fred))

# Change fred's properties
fred.colour = "Blue"
fred.age = 13
fred.weight = 5

print(f"Fred's colour: {fred.colour}") # Access properties

fred.colour = "Red"
print(f"Fred's colour: {fred.colour}") # Access properties

# Use the breathe() method on fred
fred.breathe()

fran = Animal("Fran")
fran.breathe()

# Create a new Cat object
chester = Cat("Chester")
chester.breathe()
chester.meow()

spot = Dog("Spot")
spot.bark()
spot.breathe()