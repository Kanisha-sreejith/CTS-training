class Circle:
    def draw(self):
        print("Drawing Circle")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

class Notification:
    def notify(self, message):
        raise NotImplementedError("Subclasses must implement notify()")

class SMSNotification(Notification):
    def notify(self, message):
        print(f"Sending SMS notification: {message}")

class EmailNotification(Notification):
    def notify(self, message):
        print(f"Sending Email notification: {message}")

class PushNotification(Notification):
    def notify(self, message):
        print(f"Sending Push notification: {message}")

class NotificationFactory:
    def create_notification(self, notification_type):
        if notification_type == "sms":
            return SMSNotification()
        elif notification_type == "email":
            return EmailNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            return None

if __name__ == "__main__":
    factory = NotificationFactory()

    notification = factory.create_notification("email")
    if notification:
        notification.notify("Your order has been shipped.")
    else:
        print("Invalid notification type")