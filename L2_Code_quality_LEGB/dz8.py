"""Зберігання налаштувань користувача"""


def create_user_settings():
    """ функція, яка повертає функцію для зберігання і отримання налаштувань
    """

    settings = {"Theme": "White", "Language": "Deutsch", "Notification": True}

    def save_user_settings(key=None, value=None):
        if key is not None and value is not None:
            settings[key] = value
        elif key is not None:
            return settings.get(key)
        else:
            return settings

    return save_user_settings


save_user_settings = create_user_settings()
print(save_user_settings())
print(save_user_settings("Language"))
print(save_user_settings("Theme"))
print(save_user_settings("Notification"))

save_user_settings("Theme", "Blue")
print(save_user_settings())

save_user_settings("Language", "English")
print(save_user_settings())

save_user_settings("Notification", "Muted")
print(save_user_settings())
