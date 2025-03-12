## Change object-oriented code into functional

The debate over functional vs object-oriented programming has been ongoing for decades, and both paradigms have their
proponents and detractors. At a high level, object-oriented programming (OOP) is a programming paradigm that models
real-world objects and their relationships, while functional programming (FP) is a programming paradigm that focuses
on the evaluation of functions and their application to data.

## Challenge

## Solution

- We need to somehow get rid of the different Shape classes as well as the ShapeCalculator class.
- ShapeCalculator is easy - we can simply turn that into two functions.
- As a first try, we could turn Shape into a tuple with two ShapeFn functions.
- Then rectangle, square and circle are turned into functions that return a tuple.
- But that's not yet fully functions, because we're still creating objects.
- Second version uses only functions, and relies on partial function application and a new calculate total function.
- It's a bit hypothetical, but it's a good exercise to see how for you can get with only functions (spoileralert: very far).
