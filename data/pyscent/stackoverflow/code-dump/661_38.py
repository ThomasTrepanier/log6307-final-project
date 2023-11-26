from django.dispatch import Signal, receiver
notification=Signal()
@receiver(notification)
def show_notification(sender, **kwargs):
    print("sender,", sender)
    print("Kwargs", kwargs)
    print("Notification")        
