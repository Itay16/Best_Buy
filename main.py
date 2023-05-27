import products
from best_buy.Best_Buy import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]

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
            for product in all_products:
                print(product)
        elif user_choice == '2':
            print(store.get_total_quantity())
        elif user_choice == '3':
            all_products = store.get_all_products()
            print()
            num = 1
            for product in all_products:
                print(f"{num}. {product}")
                num += 1
            store.order(all_products)
        elif user_choice == '4':
            print("Goodbye!")
            break


start(best_buy)
