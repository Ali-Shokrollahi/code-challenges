from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    pass


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total_price: Decimal) -> Decimal: ...


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class FixedDiscount(Discount):
    amount: Decimal

    def apply_discount(self, total_price: Decimal) -> Decimal:
        return total_price - self.amount


@dataclass
class PercentageDiscount(Discount):
    percentage: Decimal

    def apply_discount(self, total_price: Decimal) -> Decimal:
        return total_price - (total_price * self.percentage)


DISCOUNTS: dict[str, Discount] = {
    "SAVE10": PercentageDiscount(percentage=Decimal("0.1")),
    "5BUCKSOFF": FixedDiscount(amount=Decimal("5.00")),
    "FREESHIPPING": FixedDiscount(amount=Decimal("2.00")),
    "BLKFRIDAY": PercentageDiscount(percentage=Decimal("0.2")),
}


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount: Discount | None = None

    def add_discount(self, discount_code: str):
        if discount_code not in DISCOUNTS:
            print(f"Discount code '{discount_code}' is not valid!")
            return
        self.discount = DISCOUNTS[discount_code]

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    def calculate_final_price(self) -> Decimal:
        if self.discount:
            return self.discount.apply_discount(self.total)
        return self.total

    @property
    def total(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    def display(self) -> None:
        # Print the cart
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"total: ${self.total:>7.2f}")
        print(f"Discount: ${self.total - self.calculate_final_price():>7.2f}")
        print(f"you should pay:    ${self.calculate_final_price():>7.2f}")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )
    cart.add_discount("BLKFRIDAY")

    cart.display()


if __name__ == "__main__":
    main()
