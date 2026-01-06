class InsufficientFundsException(Exception):
    """kлас який наступний від виключеного базового класу.

    Має наступні властивості:
    required_amount: грошова сума, необхідна для виконання операції.
    current_balance: поточний баланс рахунку.
    Опціонально:
    currency: валюта рахунку.
    transaction_type: тип транзакції (наприклад, "withdrawal", "purchase")
    """

    def __init__(self, required_amount, current_balance, currency="Euro", transaction_type="transaction"):
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
        super().__init__(self._generate_info())

    def _generate_info(self):
        return (f"Not enough money to {self.transaction_type}. "
                f"You need: {self.required_amount} {self.currency}, "
                f"You have only: {self.current_balance} {self.currency}.")


class BankAccount:
    def __init__(self, balance, currency="Euro"):
        self.balance = balance
        self.currency = currency

    def purchase(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="purchase"
            )
        self.balance -= amount
        print(f"You have get {amount} {self.currency}. Your New balance: {self.balance} {self.currency}")


card = BankAccount(balance=120, currency="Euro")

try:
    card.purchase(123)
except InsufficientFundsException as e:
    print(e)
