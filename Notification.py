
class Notification:
    def send(self, recipient, message):
        """
        Base method to send notifications.
        :param recipient: Recipient details (e.g., email, phone, etc.).
        :param message: The message to be sent.
        """
        pass


class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"Email sent to {recipient}: {message}")


class SMSNotification(Notification):
    def send(self, recipient, message):
        print(f"SMS sent to {recipient}: {message}")


class PushNotification(Notification):
    def send(self, recipient, message):
        print(f"Push Notification sent to {recipient}: {message}")


def main():

    employee_preferences = {
        "John": {"type": "email", "recipient": "john@example.com"},
        "Jane": {"type": "sms", "recipient": "9876543210"},
        "Alice": {"type": "push", "recipient": "device_12345"},
    }

    
    notifications = [
        {"employee": "John", "message": "New Policy Update: Check your email."},
        {"employee": "Jane", "message": "Event Reminder: Office party tomorrow!"},
        {"employee": "Alice", "message": "System Alert: Server maintenance tonight."},
    ]


    for notif in notifications:
        employee = notif["employee"]
        message = notif["message"]

        if employee not in employee_preferences:
            print(f"Preferences not found for {employee}. Skipping.")
            continue

        preference = employee_preferences[employee]
        notification_type = preference["type"]
        recipient = preference["recipient"]

        if notification_type == "email":
            notifier = EmailNotification()
        elif notification_type == "sms":
            notifier = SMSNotification()
        elif notification_type == "push":
            notifier = PushNotification()
        else:
            print(f"Unknown notification type for {employee}. Skipping.")
            continue

        notifier.send(recipient, message)


if __name__ == "__main__":
    main()
