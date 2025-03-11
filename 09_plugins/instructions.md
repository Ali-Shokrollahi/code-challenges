## Convert payments to use the plugin architecture

The plugin architecture allows to customize an application to meet specific needs without requiring to
(necessarily) have programming knowledge or modify the application's core code. It also makes it easier for developers
to maintain and update the software application, as changes made to the core code are less likely to affect the
plugins.

## Challenge

For this challenge you need to convert the payment strategy pattern to the plugin pattern. We recommend creating a
separate folder to create all the scripts and subdirectories inside as you will need to create many new scripts.

\*Important notes:

1. Make sure the naming of the modules and the class names is consistent since it will be used as an
   argument in the `set_payment_strategy` method.
2. Add the folder where the plugins reside in your python path in order for the `importlib` to be able to import it.
   You can use the `sys.path.append` method of the `sys` library for that.
3. We also created a function to convert the module name string to the class name string for using only the module name
   string as input for the `set_payment_strategy` method. This is connected to point 1.

## Solution

- The issue is that payment methods are hardcoded in the file.
- You can use importlib to dynamically import the payment methods.
- Create a separate folder plugins that contains the payment methods.
- Standard definition of a payment method module should contain 2 functions.
- One function to process the payment and one function to get the name of the payment method.
- Create plugin manager to load and manage these plugins.
- Use protocol class to represent a plugin.
- Add functions to easily load plugins and retrieve them.
- Adding another payment method is now simply a question of adding another file to the plugins folder.
- No need to change anything else in the code.
