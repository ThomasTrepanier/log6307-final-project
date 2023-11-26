# Base class for all notifications
class Notification:
    def notify(self):
        return "Notifying..."


# Specific notification types
class EmailNotification(Notification):
    def notify(self):
        message = super().notify()  # Call the base notify method
        return message + " via Email"


class SMSNotification(Notification):
    def notify(self):
        message = super().notify()  # Call the base notify method
        return message + " via SMS"


# This class inherits from both Email and SMS notifications
class HybridNotification(EmailNotification, SMSNotification):
    def notify(self):
        message = super().notify()  # Which notify will it call? Email or SMS?
        return message + " and also via other means"


# Create a hybrid notification
hybrid = HybridNotification()
print(hybrid.notify())
