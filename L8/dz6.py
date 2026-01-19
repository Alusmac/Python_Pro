import pytest
from unittest.mock import MagicMock


class BankAccount:
    """class that implements methods:
    account replenishment
    withdrawal of funds
    current balance.
    """
    def __init__(self, initial_balance: float = 0.0):
        self._balance = initial_balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    def get_balance_from_api(self) -> float:
        raise NotImplementedError


@pytest.fixture
def account():
    return BankAccount(initial_balance=100.0)


@pytest.mark.parametrize(
    "amount, expected",
    [
        (50, 150),
        (0, 100),
        (25.5, 125.5)
    ]
)
def test_deposit(account, amount, expected):
    account.deposit(amount)
    assert account.get_balance() == expected


@pytest.mark.parametrize(
    "withdraw_amount, expected_balance",
    [
        (50, 50),
        (100, 0)
    ]
)
def test_withdraw(account, withdraw_amount, expected_balance):
    account.withdraw(withdraw_amount)
    assert account.get_balance() == expected_balance


def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(200)


@pytest.mark.skipif(
    condition=lambda: BankAccount().get_balance() == 0,
    reason="Cannot withdraw from empty account"
)
def test_skip_empty_account():
    acc = BankAccount()
    acc.deposit(50)
    acc.withdraw(50)
    assert acc.get_balance() == 0


def test_get_balance_from_api_mock(account, monkeypatch):
    mock_api = MagicMock(return_value=500.0)

    monkeypatch.setattr(account, "get_balance_from_api", mock_api)

    balance = account.get_balance_from_api()
    assert balance == 500.0
    mock_api.assert_called_once()
