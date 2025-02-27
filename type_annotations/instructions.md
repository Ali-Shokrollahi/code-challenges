## Add type hinting

Type hinting in Python is important because it allows developers to explicitly specify the data types of
function parameters and return values. This helps to improve code clarity, readability, and maintainability,
especially in large-scale projects where multiple developers may be working on the same codebase.
By using type hinting, developers can catch potential bugs early on in the development process, and also
help IDEs provide better code suggestions and error detection.

Although, python is quite permissive as a language and will allow variables of different types to be passed it is
one of the best practices to use type hinting for the reasons named above.

## Challenge

For this challenge, you will need to type hint the code given in `app.py` file. Keep in mind that since the dataclasses
have no type hinting, which is mandatory the code can't run.

## Solution

- Let's first look at the more basic functions: filter_odd_numbers, square_numbers, and count_chars.
- Works with either numbers of characters. You might be tempted to use lists for each of these types, but you'd be artificially limiting the function's flexibility. The only aspect of a list that these functions use is that they iterate over it.
- So, instead of using a list, you can use the more generic Iterable type, which can be used for any type of iterable object, including lists, tuples, sets, and more.
- For the return type, it does make sense to be more specific and use a list, because that's what the function actually returns. That way, the caller of the function knows that the return value is a list, and can use list-specific methods on it.

- Process_data is more complex. It expects a filter function and a process function. We don't know much about the types though. The only thing we can really say is that the filter function should return the same type it receives as input. And the process function takes something of that type, and then returns something of another type.
- You can also see this in how it's used in the main function (count_chars)
- To model this, I've used two generic types: T and U. T represents the type of the input to the filter function, and U represents the type of the output of the process function. Now we can define a FilterFunc and a ProcessFunc type alias.
- Show IDE type hinting suggestions.
