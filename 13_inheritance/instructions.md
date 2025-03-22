## Simplify inheritance relationship | Introduce polymorphishm

In the previous challenge we introduced multiple levels of abstraction to reduce code coupling.
We created the `HttpClient`, `RequestsClient` and `WeatherApi` to manage access to the api service.
With this implementation the `WeatherApi` is agnostic to the library (approach) we use to connect to the api 
service of `OpenWeatherMap`. This way it becomes very easy to replace `requests` librady with a different one if needed.

## Challenge

For this challenge you need to refactor the given code so that the inheritance relationship is simplified.
There's many ways to do so, but a good approach would be to further decouple the `WeatherApi` to work with any
`HttpClient` object and not only with `RequestClient` which is a subclass of the former. 

Hint: Try using a higher order function to avoid the need to pass the an http_client in the WeatherApi constructor.




## Solution (this should be sent afterwards with your explanation video (if applicable)

As mentioned before, one possible way to simplify the inheritance structure is to make the `WeatherApi` class take 
in an instance of `HttpClient` as an argument, instead of a specific subclass like 
`RequestsClient`. This way, the `WeatherApi` class can work with any implementation of the 
`HttpClient` interface, without being tied to a specific implementation like `RequestsClient`.

To make things even simpler we can create a function that returns an instance of the `RequestsClient`, which is 
called directly into the `get_complete_forecast` method the `WeatherApi` and not passed as an argument to the 
`WeatherApi` constructor as before.

Notice that, there is a form of polymorphism implemented in this code. 
The `WeatherApi` class takes an instance of `HttpClient` in its constructor. However, instead 
of passing an instance of `HttpClient`, an instance of `RequestsClient` is passed. 
Since `RequestsClient` is an implementation of `HttpClient` protocol class, it is a valid substitution for `HttpClient`, 
demonstrating polymorphism. 








