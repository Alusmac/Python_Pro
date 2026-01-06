class InsufficientResourcesException(Exception):
    """клас наступний від базового класу-вийнятку.

    Має наступні властивості:
    required_resource: рядок, що вказує на бракуючий ресурс (наприклад, "золото", "мана").
    required_amount: Число, що вказує потрібну кількість ресурсу.
    current_amount: Число, що вказує поточну кількість ресурсів у гравця.
    """

    def __init__(self, required_resource: str, required_amount: int, current_amount: int):
        super().__init__(f"Not enough {required_resource} (needed: {required_amount}, available: {current_amount})")
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount


def magic_events(player_resources, spell_cost):
    """ Функція яка відтворює магічну дію а також використовує на це ресурси які є в ігрока
    """

    resource_name = "Mana"
    current_mana = player_resources.get(resource_name, 0)

    if current_mana < spell_cost:
        raise InsufficientResourcesException(resource_name, spell_cost, current_mana)

    player_resources[resource_name] -= spell_cost
    print(f"Done! You have {player_resources[resource_name]} {resource_name} left.")


player_resources = {"Mana": 56, "Gold": 40}

spell_cost = 79
try:
    magic_events(player_resources, spell_cost)
except InsufficientResourcesException as e:
    print(f"Sorry but you have no more Mana!")
    print(f"You should have {e.required_amount} {e.required_resource}, but you only have {e.current_amount}.")
