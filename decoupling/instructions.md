## Challenge

In this challenge, you're going to work on a banking service.

The problem with the current code is that the BankService class in code_decoupling/bank.py is highly coupled with the payment service and the different account types. Also, the code has quite a bit of duplication. Your job is to refactor this code so that it's less coupled and has less duplicate code.

You have quite a bit of freedom in this challenge: it's okay to introduce new classes or replace existing classes by functions, feel free to experiment! However, the goal remains that banking operations should be decoupled from payment operations as much as possible.

## Solution

- Bank has isinstance checks which directly couple it to different types of accounts.
- Bank is directly dependent on a specific payment service and directly sets an API key.
- Make account more generic (account type + class)
- Bank turns into functions to deposit and withdraw that get a payment service as argument
- Payment service is a protocol class, so the functions are decoupled from a specific payment service.
- The payment service object is created in the main function, and that's also where the API key is set.
- Mention single dirty place.
