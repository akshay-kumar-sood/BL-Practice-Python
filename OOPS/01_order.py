from abc import ABC, abstractmethod
from dataclasses import dataclass


#  Discount Policy 

class DiscountPolicy(ABC):

    @abstractmethod
    def apply_discount(self, order_total: float) -> float:
        pass


class NoDiscount(DiscountPolicy):

    def apply_discount(self, amount: float) -> float:
        return amount


class PercentageDiscount(DiscountPolicy):

    def __init__(self, percentage: float):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100)


# Product 

# to provide init (constructor)
@dataclass
class Product:
    name: str
    _price: float
    quantity: int

    # Constructor ke baad validation
    def __post_init__(self):
        self.price = self._price

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Qty: {self.quantity}"



#  Order

class Order:

    def __init__(self, order_id, discount_policy):
        self.order_id = order_id
        self.products = []
        self.discount_policy = discount_policy

    # adding products
    def add_product(self, product):
        self.products.append(product)

    # counting total
    def total(self):
        total = 0

        for product in self.products:
            total += product.price * product.quantity

        return total

    # total after applying discount
    def final_total(self):
        return self.discount_policy.apply_discount(self.total())

    # Total quantity of items
    def number_of_items(self):
        total_items = 0

        for product in self.products:
            total_items += product.quantity

        return total_items

    # Number of Product Objects
    def __len__(self):
        return len(self.products)

    def __str__(self):
        result = f"\nOrder ID : {self.order_id}\n"
        result += "-" * 35 + "\n"

        for product in self.products:
            result += str(product) + "\n"

        result += "-" * 35 + "\n"
        result += f"Total Product Objects : {len(self)}\n"
        result += f"Total Items : {self.number_of_items()}\n"
        result += f"Total Amount : ₹{self.total()}\n"
        result += f"Final Amount : ₹{self.final_total():.2f}"

        return result




# Products
p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 1000, 2)
p3 = Product("Keyboard", 2000, 1)

# Order
order = Order(101, PercentageDiscount(10))

order.add_product(p1)
order.add_product(p2)
order.add_product(p3)

# Print Order
print(order)

print()

print("Number of Product Objects :", len(order))