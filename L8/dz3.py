import pytest


class UserManager:
    """class user management
    with users add, remove, all users list
    """
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, name: str, age: int) -> None:
        self.users[name] = age

    def remove_user(self, name: str) -> None:
        if name in self.users:
            del self.users[name]
        else:
            raise ValueError(f"User '{name}' not found")

    def get_all_users(self) -> list:
        return list(self.users.items())


@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_add_user(user_manager) -> None:
    user_manager.add_user("Charlie", 22)
    assert ("Charlie", 22) in user_manager.get_all_users()


def test_remove_user(user_manager) -> None:
    user_manager.remove_user("Alice")
    users = user_manager.get_all_users()
    assert ("Alice", 30) not in users
    assert ("Bob", 25) in users


def test_get_all_users(user_manager) -> None:
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert ("Alice", 30) in users
    assert ("Bob", 25) in users


@pytest.mark.skipif(
    condition=lambda: len(UserManager().get_all_users()) < 3,
    reason="Not enough users for the test (≥ 3 required))"
)
def test_requires_three_users(user_manager):
    assert len(user_manager.get_all_users()) >= 3
