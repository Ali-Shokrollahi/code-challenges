## Challenge

## Solution

- Discounts is directly coupled with the shopping cart class.
- On top of that, inheritance is used to extend the behavior.
- Instead, we can use composition and create a Discount class that is stored in the ShoppingCart class.
- Solution even has a list of discounts, so that we can apply multiple discounts.
- This is the power of composition over inheritance.
