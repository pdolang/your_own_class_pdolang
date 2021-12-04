# Priscella Dolang
# Assignment 10.1 : Your Own Class
# Acknowledgments : slides from class, w3schools, geeksforgeeks

# This program mimicks a bakery and lets you choose what you want to do and what you want to order.

# Creating the Bakery class
class Bakery:
    # Name as user input 
    name = input("What is your name?: ")
    print(f"Hello {name}!")
    # The __init__ method 
    def __init__(self, milk, eggs, butter, flour, sugar, frosting, money):
        self.milk = milk
        self.eggs = eggs
        self.butter = butter
        self.flour = flour
        self.sugar = sugar 
        self.frosting = frosting 
        self.money = 0
        self.goods_counter = 0 
    
    # The start method: welcomes user to the bakery and provides options on what to do 
    def start(self):
        print("welcome to the virtual bakery")
        self.choices = str(input("The options available are:\n- purchase (buys item)\n- take (takes ingredient)\n- refill (refills ingredient)\n- supply (checks current supply status)\n- exit (leaves bakery)\nEnter your option here: "))
        # Navigates the user to the specific method
        if self.choices == "purchase":
            self.purchase()
        elif self.choices == "take":
            self.take()
        elif self.choices == "refill":
            self.refill()
        elif self.choices == "supply":
            self.supply()
        elif self.choices == "exit":
            exit()
    
    # The options method: returns user back to the choices ^ as listed above
    def options(self):
        print()
        self.choices()

    # The set milk method: sets the amount of milk for the bakery 
    def set_milk(self, m):
        self._set_milk = m

    # The set eggs method: sets the amount of eggs for the bakery
    def set_eggs(self, e):
        self._set_eggs = e

    # The set butter method: sets the amount of butter for the bakery
    def set_butter(self, b):
        self._set_butter = b

    # The set flour method: sets the amount of flour for the bakery
    def set_flour(self, fl):
        self._set_flour = fl

    # The set sugar method: sets the amount of sugar for the bakery
    def set_sugar(self, s):
        self._set_sugar = s

    # The set frosting method: sets the amount of frosting for the bakery
    def set_frosting(self, f):
        self._set_frosting = f

    # The check ingredients method: checks if there are enough ingredients to take or purchase baked goods
    def check_ingredients(self):
        # Empty string that will contain whatever ingredient is missing 
        self.unavailable = ""
        # If any of the ingredients are below 0, then there is no more of that ingredient 
        if self._set_milk - self.subtract[0] < 0:
            self.unavailable = "milk"
        elif self._set_eggs - self.subtract[1] < 0:
            self.unavailable = "eggs"
        elif self._set_butter - self.subtract[2] < 0:
            self.unavailable = "butter"
        elif self._set_flour - self.subtract[3] < 0:
            self.unavailable = "flour"
        elif self._set_sugar - self.subtract[4] < 0:
            self.unavailable = "sugar"
        elif self._set_frosting - self.subtract[5] < 0:
            self.unavailable = "frosting"

        # These are the statements that will be printed if there are enough of each ingredient or if there isn't enough
        if self.unavailable != "":
            print(f"Oh no, there isn't enough {self.unavailable} in our storage.")
            return False
        else:
            print("Perfect! There are enough ingredients to make sweets.")
            return True 

    # The subtract ingredients method: subtracts from the storage depending on the baked goods that are made
    def subtract_ingredients(self):
        self._set_milk -= self.subtract[0]
        self._set_eggs -= self.subtract[1]
        self._set_butter -= self.subtract[2]
        self._set_butter -= self.subtract[3]
        self._set_flour -= self.subtract[4]
        self._set_sugar -= self.subtract[5]
        self._set_frosting -= self.subtract[6]
        # These following ones are added since the bakery earns money per baked good and the counter keeps track on how many are made
        self.money += self.subtract[7]
        self.goods_counter += self.subtract[8]

    # The purchase method: Depending on the user's input, a certain amount is subtracted from the ingredients
    def purchase(self):
        self.item = input(f"This is the menu for today:\n- cake\n- tart\n- bread\n- cupcakes\n cookies\n- pie\n- return to options")
        if self.item == "cake":
            # The variable for subtracting from the ingredients 
            self.subtract = [2, 6, 4, 8, 2, 4, 16, 1]
            # If the self.check_ingredients is returning True then it subtracts the ingredients 
            if self.check_ingredients():
                self.subtract_ingredients()

        elif self.item == "tart":
            # The variable for subtracting from the ingredients 
            self.subtract = [0, 2, 4, 3, 1, 0, 14, 1]
            # If the self.check_ingredients is returning True then it subtracts the ingredients 
            if self.check_ingredients():
                self.subtract_ingredients()

        elif self.item == "bread":
            # The variable for subtracting from the ingredients 
            self.subtract = [2, 0, 1, 5, 1, 0, 7, 1]
            # If the self.check_ingredients is returning True then it subtracts the ingredients 
            if self.check_ingredients():
                self.subtract_ingredients

        elif self.item == "cupcakes":
            # The variable for subtracting from the ingredients 
            self.subtract = [1, 3, 2, 4, 1, 2, 10, 1]
            # If the self.check_ingredients is returning True then it subtracts the ingredients 
            if self.check_ingredients():
                self.subtract_ingredients()

        elif self.item == "cookies":
            # The variable for subtracting from the ingredients 
            self.subtract = [0, 2, 3, 3, 2, 0, 5, 1]
            # If the self.check_ingredients is returning True then it subtracts the ingredients 
            if self.check_ingredients():
                self.subtract_ingredients()

        elif self.item == "pie":
            # The variable for subtracting from the ingredients 
            self.subtract = [3, 2, 4, 5, 3, 0, 18, 1]
            # If the self.check_ingredients is returning True then it subtracts the ingredients 
            if self.check_ingredients():
                self.subtract_ingredients()
        
        # Returns user to the options
        elif self.item == "return":
            self.options()

        # Returns user to the options at the end of their decision 
        self.options()

    # The take method: Depending on the user input, it subtracts the inputted amount from the ingredients 
    def take(self):
        self._set_milk -= int(input("How much milk (in cartons) would you like to take? Enter a numerical value here: "))
        self._set_eggs -= int(input("How many eggs would you like to take? Enter a numerical value here: "))
        self._set_butter -= int(input("How much butter (in sticks) would you like to take? Enter a numerical value here: "))
        self._set_flour -= int(input("How much flour (in cups) would you like to take? Enter a numerical value here: "))
        self._set_sugar -= int(input("How much sugar (in cups) would you like to take? Enter a numerical value here: "))
        self._set_frosting -= int(input("How much frosting (in cups) would you like to take? Enter a numerical value here: "))

        # Returns the user to the options at the end of their inputs 
        self.options()

    # The refill method: Depending on the user input, it adds the inputted amount to the ingredients 
    def refill(self):
        self._set_milk += int(input("How much milk (in cartons) would you like to add? Enter a numerical value here: "))
        self._set_eggs += int(input("How many eggs would you like to add? Enter a numerical value here: "))
        self._set_butter += int(input("How much butter (in sticks) would you like to add? Enter a numerical value here: "))
        self._set_flour += int(input("How much flour (in cups) would you like to add? Enter a numerical value here: "))
        self._set_sugar += int(input("How much sugar (in cups) would you like to add? Enter a numerical value here: "))
        self._set_frosting += int(input("How much frosting (in cups) would you like to add? Enter a numerical value here: "))

        # Returns the user to the options at the end of their inputs
        self.options()

    # The supply method: Displays a report on how many of each ingredient is left 
    # It also shows how much money is earned and how many baked goods were made
    def supply(self):
        print("Ingredient Supply/Sales Report: ")
        print(f"- {self._set_milk} milk cartons")
        print(f"- {self._set_eggs} eggs")
        print(f"- {self._set_butter} sticks of butter")
        print(f"- {self._set_flour} cups of flour")
        print(f"- {self._set_sugar} cups of sugar")
        print(f"- {self._set_frosting} cups of frosting")
        print(f"- ${self.money} earned")
        print(f"- {self.goods_counter} baked goods made")

        # Returns the user to the options at the end of their inputs 
        self.options() 

def main():
    # Setting the Bakery to the following set amounts of ingredients 
    milk = Bakery()
    milk._set_milk(15)
    eggs = Bakery()
    eggs._set_eggs(20)
    butter = Bakery()
    butter._set_butter(25)
    flour = Bakery()
    flour._set_flour(40)
    sugar = Bakery()
    sugar._set_sugar(30)
    frosting = Bakery()
    frosting._set_frosting(10)

if __name__ == "__main__":
    main()