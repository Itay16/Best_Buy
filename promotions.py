from abc import ABC, abstractmethod


class Promotion(ABC):
    promotions_catalog = {}

    @classmethod
    def add_promotion(cls, promotion):
        cls.promotions_catalog[promotion.name] = promotion

    @classmethod
    def get_promotion(cls, promotion_name):
        return cls.promotions_catalog.get(promotion_name)

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            half_quantity = quantity // 2
            discounted_price = half_quantity * product.price + half_quantity * (product.price * 0.5)
        else:
            half_quantity = quantity // 2
            discounted_price = (half_quantity + 1) * product.price
        return discounted_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        group_of_three = quantity // 3
        remainder = quantity % 3
        discounted_price = (group_of_three * 2 * product.price) + (remainder * product.price)
        return discounted_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * quantity * (1 - self.percent / 100)
        return discounted_price
