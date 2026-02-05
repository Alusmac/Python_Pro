"""Календар подій """
events = []


def calendar_events() -> str:
    """ функція яка створює календар подій

    """

    def add_calendar_events(event: str | list, date: str) -> None:
        events.append({"event": event, "date": date})
        print(f"Ваша подія записана: {event}, {date}")

    def remove_calendar_events(event: str) -> None:
        events.remove(next(e for e in events if e["event"] == event))
        print(f"Ваша подія видалена: {event}")

    def review_calendar_events() -> None:
        if not events:
            print(f"Подію не знайдено!")
        else:
            print(f"Вaші подіі: ")
            for e in events:
                print(f"- {e['event']}, {e['date']}")

    return add_calendar_events, remove_calendar_events, review_calendar_events


add_calendar_events, remove_calendar_events, review_calendar_events = calendar_events()
add_calendar_events("Happy birthday", "20 May")
add_calendar_events("Ski resort", "04 January")
add_calendar_events("Examination", "30 january")
review_calendar_events()
remove_calendar_events("Happy birthday")
review_calendar_events()
