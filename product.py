import promotions


class Product:
    promotion = None

    def __init__(self, name, price, quantity, active=True):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.active = False
        else:
            self.active = active

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
        if self.quantity == 0:
            self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}\nPromotion: {self.promotion}")

    def buy(self, quantity):
        if self.quantity >= quantity:
            if self.promotion is not None:
                discounted_price = promotions.Promotion.apply_promotion(self, quantity)
                self.quantity -= quantity
                return f"The total price with promotion applied is: {discounted_price}$"
            else:
                total_price = self.price * quantity
                self.quantity -= quantity
                return f"The total price is: {total_price}$"
        else:
            print("There isn't enough of that product currently. Sorry!")

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def get_promotion_name(self):
        if self.promotion:
            return self.promotion.name
        else:
            return "None"

    def apply_promotion(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0, active=True):
        super().__init__(name, price, quantity, active=True)

    def show(self):
        print(f"{self.name}, Price: {self.price}$\n"
              f"This item is NOT physical.")

    def buy(self, quantity):
        return f"The total price is: {self.price}$"


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum=1, active=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.maximum = maximum
        self.active = active

    def show(self):
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}"
              f"This item is up for a limited time!")

    def buy(self, quantity):
        if quantity > 1:
            print("We're sorry, you can only order this item once.")
        else:
            if self.quantity >= quantity:
                self.quantity -= quantity
                total_price = self.price * quantity
                return f"The total price is: {total_price}$"
            elif self.quantity < quantity:
                print("There isn't enough of that product currently. Sorry!")
                return
