class GameEventException(Exception):
    """клас, наступний від базового класу.

    Має: наступні властивості:
    event_type: рядок, який описує тип події (наприклад, "death", "levelUp").
    details: словник або об'єкт, що містить додаткову інформацію про події.
    """

    def __init__(self, event_type: str, details: dict):
        super().__init__(f"Game Event: {event_type}")
        self.event_type = event_type
        self.details = details


def event_death(event: GameEventException):
    print("You are dead(((")
    for key, value in event.details.items():
        print(f"{key}: {value}")
    print("-" * 10)


def event_level(event: GameEventException):
    print("You have level up!")
    for key, value in event.details.items():
        print(f"{key}: {value}")


my_events = {
    "death": event_death,
    "levelUp": event_level,

}


def play_game():
    """ Функція яка зберігає події але не зупиняє гру
    """
    all_events = []

    try:
        death_details = {"reason_of_death": "sword strike", "player_life": 0}
        raise GameEventException("death", death_details)
    except GameEventException as e:
        all_events.append(e)

    try:
        level_up_details = {"new_level": 3, "experience": 56}
        raise GameEventException("levelUp", level_up_details)
    except GameEventException as e:
        all_events.append(e)

    return all_events


for event in play_game():
    handler = my_events.get(event.event_type)
    if handler:
        handler(event)
    else:
        print(f"Unknow operation: {event.event_type}")
        for key, value in event.details.items():
            print(f"{key}: {value}")
        print("-" * 10)
