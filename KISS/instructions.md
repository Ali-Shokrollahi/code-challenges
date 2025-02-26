## Challenge

You are given a list of strings that represent different types of fruits. You are required to count the frequency of each type of fruit and return a dictionary where the keys are the names of the fruits and the values are their respective counts.

Write a Python function named count_fruits that accomplishes this task in the simplest possible way. Follow the KISS principle to avoid unnecessary complexity in your solution.
After completing the function, write tests to ensure that it's working correctly.
Hint: You might want to look into Python's built-in data types and their methods to help solve this task efficiently.

Here's a start to the problem:

After you have completed the tasks, reflect on your solution and ask yourself the following questions:

Is your solution as simple as it could be, or is there a simpler approach?
Does your solution use language features and constructs appropriately and effectively?
Are your tests comprehensive enough to catch potential edge cases?
The goal of this exercise is to encourage you to write simple, straightforward, and easy-to-understand code.

## Solution

- First version uses nested loops, iterating over the list of fruits for each unique fruit found.
- Not very efficient, and more complex read and understand.
- It would also perform poorly for large lists of fruits, because of the nested loop.
- It doesn't use Python's built-in functions and data types that are designed for tasks like this.

- Second version is already much better. It uses the "in" keyword to check if a fruit is already in the dictionary, and if so, it increases its count by 1. If not, it adds the fruit to the dictionary with a count of 1.
- It's straightforward, easy to understand, and does not use any complex or unnecessary constructs.

- You can take this one step further and fully rely on Python's built-in functionality to solve this problem.
- Here's the third version, which uses Python's Counter class from the collections module.
