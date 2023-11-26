from django.http import HttpRequest
def get_user_ip(request):
    client_address = request.META['HTTPS_X_FORWARDED_FOR']
    if your_ip == client_address:
        save_user_ip()
