class RetailItem: #Class for item
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price
        self.in_cart = 0

    def display_info(self):
        if self.units > 1:
            print(f"{self.description} : {self.units} units at ${self.price} each")
        elif self.units == 1:
            print(f"{self.description} : {self.units} unit at ${self.price}")
        else:
            print(f"{self.description} : None available.")

    def increment_in_cart(self): #keeps counter of units in cart
        self.in_cart += 1

    def clear_cart(self): #will add unpurchased items back to stock
        self.units += self.in_cart
        self.in_cart = 0

class CashRegister: #class for checkout
    def __init__(self):
        self.item_list = [] #list of RetailItem objects for purchase, see line 80

    def purchase_item(self, RetailItem):
        self.item_list.append(RetailItem)

    def get_total(self):
        total_price = 0
        for RetailItem in self.item_list:
            total_price += RetailItem.price * RetailItem.in_cart
        return total_price

    def show_items(self): #displays items for checkout
        for RetailItem in self.item_list:
            print(f"{RetailItem.in_cart} unit(s) of {RetailItem.description}(s)" +
                    " in cart.")

    def clear(self): #clears cart, calls RetailItem clear_cart method to restock
        for item in self.item_list:
            item.clear_cart()
        self.item_list.clear()
            

jackets = RetailItem("Jacket", 12, 59.95)

jeans = RetailItem("Designer Jeans", 40, 34.95)

shirt = RetailItem("Shirt", 20, 24.95)

checkout = CashRegister()

print("Hello, welcome to the store! We have the following items in stock today:\n")

jackets.display_info()
jeans.display_info()
shirt.display_info()

print("What would you like to buy? \"Check out\" to check out, \"clear\"" +
      " to clear cart.")

customer_input = input()

while customer_input.lower() != "check out": #Loop for customer to add items
    try: #Try block in case user uses invalid values
        if customer_input.lower() == "jacket":
            print("How many would you like to buy?")
            unit_input = int(input())
            if unit_input > jackets.units:
                raise ValueError("Not enough stock!")
            elif unit_input < 0:
                raise ValueError("Cannot buy a negative number!")
            elif unit_input == 0:
                print("None added.")
            else:
                print(f"{unit_input} Jacket(s) added to cart.")
                count = unit_input
                if jackets not in checkout.item_list: #Only putting item in list
                    checkout.purchase_item(jackets)   #once so that the check out
                while count > 0:                      #list is more readable
                    jackets.units -= 1
                    jackets.increment_in_cart()
                    count -= 1

        elif customer_input.lower() == "designer jeans":
            print("How many would you like to buy?")
            unit_input = int(input())
            if unit_input > jeans.units:
                raise ValueError("Not enough stock!")
            elif unit_input < 0:
                raise ValueError("Cannot buy a negative number!")
            elif unit_input == 0:
                print("None added.")
            else:
                print(f"{unit_input} Designer Jean(s) added to cart.")
                count = unit_input
                if jeans not in checkout.item_list:
                    checkout.purchase_item(jeans)
                while count > 0:
                    jeans.units -= 1
                    jeans.increment_in_cart()
                    count -= 1

        elif customer_input.lower() == "shirt":
            print("How many would you like to buy?")
            unit_input = int(input())
            if unit_input > shirt.units:
                raise ValueError("Not enough stock!")
            elif unit_input < 0:
                raise ValueError("Cannot buy a negative number!")
            elif unit_input == 0:
                print("None added.")
            else:
                print(f"{unit_input} Shirt(s) added to cart.")
                count = unit_input
                if shirt not in checkout.item_list:
                    checkout.purchase_item(shirt)
                while count > 0:
                    shirt.units -= 1
                    shirt.increment_in_cart()
                    count -= 1
                        
        elif customer_input.lower() == "check out": #checkout, ends loop
            break

        elif customer_input.lower() == "clear": #clears cart
            checkout.clear()
            print("Cart cleared.")

        else:
            print("Item not carried. Please select item in stock, type " +
                  "\"check out\" to check out, or \"clear\" to clear cart.")
                                      #to catch other inputs

    except ValueError as excpt: #catches invalid values
        print(excpt)
        print("Could not add item to cart. Please select item, type " +
              "\"check out\"\nto check out, or \"clear\" to clear cart.")
    

    customer_input = input()

checkout.show_items() #shows items

print(f"Your total today is ${checkout.get_total():.2f}. Thank you!") #total

p = input("Press \"ENTER\" to exit...")
