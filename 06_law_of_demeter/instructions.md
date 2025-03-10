## The demeter law challenge

The Demeter Law, also known as the Law of Demeter or principle of least knowledge, is a software design guideline that
suggests that an object should avoid direct interaction with other objects that are not directly related to its primary
purpose.

In simpler words, the Demeter Law states that an object should only communicate with its immediate friends and not
with the friends/attributes of its friends. Violating this principle can result in tightly coupled and brittle code that is
difficult to maintain and modify over time.

## Challenge

For this challenge you need to go through the `demeter_law_violation.py` script and try to write the code that would
have the exact same behavior but without violating the Demeter law.

## Solution (this should be sent afterwards with your explanation video (if applicable)

- The main function directly needs to know implementation details of the ShoppingCart class, when updating the price or quantity of an item or when removing an item.
- Move to functions that are part of ShoppingCart.
- Add convenience methods and properties to the Item class.
