""" Таймер для тренування """
default_time = 60


def training_session(rounds: int | float) -> None:
    """ Функція яка приймає кількість раундів тренування """
    time_per_round = default_time

    def adjust_time():
        nonlocal time_per_round
        time_per_round -= 5

    for round in range(1, rounds + 1):
        if round == 1:
            print(f"Раунд: {round}: {time_per_round} хвилин")
        else:
            adjust_time()
            print(f"Раунд: {round}: {time_per_round} хвилин (після коригування часу)")


training_session(3)
# Результат:
# Раунд 1: 60 хвилин
# Раунд 2: 55 хвилин (після коригування часу)
# Раунд 3: 50 хвилин (після коригування часу)
