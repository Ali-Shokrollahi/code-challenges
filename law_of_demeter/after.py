from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception): ...


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    def update_price(self, new_price: Decimal) -> None:
        self.price = new_price

    def update_quantity(self, updated_quantity: int) -> None:
        self.quantity = updated_quantity

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    _items: list[Item] = field(default_factory=list)

    def get_item(self, item_name: str) -> Item:
        for item in self._items:
            if item.name == item_name:
                return item

        raise ItemNotFoundException(f"Item with name {item_name} not found.")

    def add_item(self, item: Item) -> None:
        self._items.append(item)

    def update_item_quantity(self, item_name: str, new_quantity: int) -> None:
        item = self.get_item(item_name)
        item.update_quantity(new_quantity)

    def update_item_price(self, item_name: str, new_price: Decimal) -> None:
        item = self.get_item(item_name)
        item.update_price(new_price)

    def remove_item(self, item_name: str) -> None:
        item = self.get_item(item_name)
        self._items.remove(item)

    @property
    def total_price(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self._items))

    def display(self) -> None:
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self._items:
            total_price = item.subtotal
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${total_price:>7.2f}"
            )
        print("=" * 40)
        print(f"Total: ${self.total_price:>7.2f}")


def main() -> None:
    # Create a shopping cart and add some items to it

    cart = ShoppingCart()

    cart.add_item(Item("Apple", Decimal("1.5"), 10))
    cart.add_item(Item("Banana", Decimal("2"), 2))
    cart.add_item(Item("Pizza", Decimal("11.90"), 5))

    # Update some items' quantity and price
    cart.update_item_quantity("Apple", 10)
    cart.update_item_price("Pizza", Decimal("3.50"))

    # Remove an item
    cart.remove_item("Banana")

    # Print the cart
    cart.display()


if __name__ == "__main__":
    main()
