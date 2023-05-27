class Product:

    def __init__(self, name, price, quantity, active=True):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = active

    def __str__(self):
        return f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}"

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def is_active(self):
        return self.active

    def activate(self):
        if not self.active:
            self.active = True

    def deactivate(self):
        if self.active:
            self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = self.price * quantity
            return f"The total price is: {total_price}$"
        else:
            return "There isn't enough of that product currently. Sorry!"