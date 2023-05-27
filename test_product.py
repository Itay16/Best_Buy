import product
import pytest
import store
import promotions


def test_products():
    # setup initial stock of inventory
    product_list = [product.Product("MacBook Air M2", price=1450, quantity=100),
                    product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    product.Product("Google Pixel 7", price=500, quantity=250),
                    product.NonStockedProduct("Windows License", price=125),
                    product.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
