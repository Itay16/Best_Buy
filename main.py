import product
import promotions
import store

# setup initial stock of inventory
product_list = [product.Product("MacBook Air M2", price=1450, quantity=100),
                product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                product.Product("Google Pixel 7", price=500, quantity=250),
                product.NonStockedProduct("Windows License", price=125),
                product.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def start(store):
    while True:
        user_choice = input("""
    Store Menu
    ----------
    1. List all products in the store
    2. Show total amount in store
    3. Make an order
    4. Quit
    Please choose a number: """)

        if user_choice == '1':
            all_products = store.get_all_products()
            for i in range(len(all_products)):
                item = all_products[i]
                promotion_name = item.get_promotion().name if item.get_promotion() else "None"
                print(
                    f"{i + 1}. {item.name}, Price: ${item.price}, Quantity: {item.quantity}, Promotion: {promotion_name}")

        elif user_choice == '2':
            print(store.get_total_quantity())

        elif user_choice == '3':
            all_products = store.get_all_products()
            for i in range(len(all_products)):
                item = all_products[i]
                promotion_name = item.get_promotion().name if item.get_promotion() else "None"
                print(
                    f"{i + 1}. {item.name}, Price: ${item.price}, Quantity: {item.quantity}, Promotion: {promotion_name}")
            store.order(all_products)

        elif user_choice == '4':
            print("Goodbye!")
            break


start(best_buy)