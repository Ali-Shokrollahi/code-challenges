from typing import Protocol
from dataclasses import dataclass
from decimal import Decimal


class BankAccount(Protocol):
    account_number: str
    balance: Decimal

    def deposit(self, amount: Decimal): ...

    def withdraw(self, amount: Decimal): ...


class PaymentService(Protocol):
    def process_payment(self, amount: Decimal) -> None: ...

    def process_payout(self, amount: Decimal) -> None: ...


@dataclass
class SavingsAccount:
    account_number: str
    balance: Decimal

    def deposit(self, amount: Decimal):
        print(f"Depositing {amount} into Savings Account {self.account_number}.")
        self.balance += amount

    def withdraw(self, amount: Decimal):
        print(f"Withdrawing {amount} from Savings Account {self.account_number}.")
        self.balance -= amount


@dataclass
class CheckingAccount:
    account_number: str
    balance: Decimal

    def deposit(self, amount: Decimal):
        print(f"Depositing {amount} into Checking Account {self.account_number}.")
        self.balance += amount

    def withdraw(self, amount: Decimal):
        print(f"Withdrawing {amount} from Checking Account {self.account_number}.")
        self.balance -= amount


class BankService:
    def __init__(self, payment_service: PaymentService) -> None:
        self.payment_service = payment_service

    def deposit(self, amount: Decimal, account: BankAccount) -> None:
        self.payment_service.process_payment(amount)
        account.deposit(amount=amount)

    def withdraw(self, amount: Decimal, account: BankAccount) -> None:
        self.payment_service.process_payout(amount)
        account.withdraw(amount=amount)
        
