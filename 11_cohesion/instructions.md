## Break single function in separate ones to increase cohesion

It is very common when coding and especially for beginners that people write very big functions with lots of different
functionalities inside. Although this might look very appealing approach because you can write the code faster,
it creates unnecessary coupling of functionalities, that becomes a headache later on when you try to test, debug,
or further develop your application.

For this challenge you need to separate (refactor) an extended function into smaller ones without -of course- affecting
the overall functionality.


## Challenge

The function you need to break into smaller ones receives some (environmental) sensor data that you can see in the 
`sensor_data.csv` file. Based on the sensor type `Temperature`, `Humidity` or `CO2` it needs to do some (different) 
processing:

- If `Temperature`, change the temperature fom Celcius to Kelvin
- If `Humidity`, the function converts the value to a scale between 0-1.
- If `CO2`, the function adds 23 to compensate for sensor bias.


Hint: While separating the function into smaller ones, try to do it so that it becomes easy to update/change
the actual processing functionality later on.


## Solution (this should be sent afterwards with your explanation video (if applicable)

To make this function easier to read and modify, we could break it down into smaller functions that handle each
processing rule. In this simplified (refactored) code, there's several new functions created to handle each processing
rule.
The `process_data function` now calls the `process_row function` for each row, which in turn calls the
appropriate processing function based on the sensor type. This makes the code easier to read and modify,
as each processing rule is now encapsulated in its own function. It also makes testing the code much simpler, even if
we decide to change the processing functionality. 








