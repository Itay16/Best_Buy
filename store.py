class Store:

    def __init__(self, products):
        self.store_list = products

    def add_product(self, product):
        self.store_list.append(product)

    def remove_product(self, product):
        if product in self.store_list:
            self.store_list.remove(product)
        else:
            print(f"{product} isn't on my list! Sorry.")

    def get_total_quantity(self):
        total_quantity = sum(product.get_quantity() for product in self.store_list)
        return f"Total products in the store: {total_quantity}"

    def get_all_products(self):
        all_products = []
        for product in self.store_list:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        print("\nWhen you want to finish the order, enter an empty text.")
        total_cost = 0

        while True:
            which_product = input("Which product # do you want? ")
            if not which_product.strip():  # Check if the input is an empty string
                break

            how_much = int(input("What amount do you want? "))
            if not str(how_much).strip():  # Check if the input is an empty string
                break

            product_index = int(which_product) - 1
            if 0 <= product_index < len(self.store_list):
                product = self.store_list[product_index]
                if product.is_active() and product in self.store_list:
                    if product.get_quantity() >= how_much:
                        # Apply promotions if available
                        promotion = product.get_promotion()
                        if promotion:
                            total_cost += promotion.apply_promotion(product, how_much)
                        else:
                            total_cost += product.price * how_much
                        product.set_quantity(product.get_quantity() - how_much)
            else:
                print("Invalid product number!")

        print(f"Order cost: {total_cost}$!")