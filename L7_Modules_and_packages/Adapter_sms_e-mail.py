class MessageSender:
    def send_message(self, message: str) -> None:
        """ відправка тексту повідомлень """
        pass


class SMSService:
    def send_sms(self, phone_number: int | float, message: str) -> None:
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    def send_email(self, email_address: str | float, message: str) -> None:
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    def send_push(self, device_id: str | int, message: str) -> None:
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    def __init__(self, sms_service, phone_number: int | float) -> None:
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Помилка при відправці SMS: {e}")


class EmailAdapter(MessageSender):
    def __init__(self, email_service, email_address: str | float) -> None:
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Помилка при відправці Email: {e}")


class PushAdapter(MessageSender):
    def __init__(self, push_service, device_id: str | int) -> None:
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Помилка при відправці Push: {e}")


class SendingViaAllServers:
    """Клас для відправки повідомлення через усі доступні сервіси одночасно
    """

    def __init__(self, adapters) -> None:
        self.adapters = adapters

    def message_transfer(self, message: str) -> None:
        for adapter in self.adapters:
            adapter.send_message(message)


sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "+380123456789")
email_adapter = EmailAdapter(email_service, "user@example.com")
push_adapter = PushAdapter(push_service, "device123")

message = "Привіт! Це тестове повідомлення."
sms_adapter.send_message(message)
email_adapter.send_message(message)
push_adapter.send_message(message)

print("-" * 90)

sending_all_servers = SendingViaAllServers([sms_adapter, email_adapter, push_adapter])
sending_all_servers.message_transfer(" відправка цього повідомлення через усі сервіси!")
